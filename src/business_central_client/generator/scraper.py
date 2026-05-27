from __future__ import annotations

import re
from collections.abc import Iterable
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup, Tag

from business_central_client.generator.ir import DocsSnapshot, Endpoint, Example
from business_central_client.generator.names import pascal_case, singularize, snake_case

DEFAULT_INDEX_URL = (
    "https://learn.microsoft.com/en-us/dynamics365/business-central/"
    "dev-itpro/api-reference/v2.0/"
)
OPERATION_LINK_PATTERN = re.compile(r"/api/dynamics_[^/#?]+(?:[#?].*)?$", re.I)
HTTP_REQUEST_PATTERN = re.compile(
    r"\b(GET|POST|PATCH|PUT|DELETE)\s+([^\n\r<`]+)",
    re.I | re.MULTILINE,
)


class DocsScraper:
    """Scrape Microsoft Learn Business Central API pages into a normalized IR."""

    def __init__(self, *, timeout_seconds: float = 30.0, user_agent: str | None = None) -> None:
        headers = {
            "Accept": "text/html,application/xhtml+xml",
            "User-Agent": user_agent
            or "business-central-client-generator/0.1 (+https://github.com/)",
        }
        self._http = httpx.Client(timeout=timeout_seconds, headers=headers, follow_redirects=True)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> DocsScraper:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def scrape(self, index_url: str = DEFAULT_INDEX_URL) -> DocsSnapshot:
        index_html = self.fetch_html(index_url)
        operation_urls = self.parse_index(index_html, index_url=index_url)
        endpoints: list[Endpoint] = []
        for operation_url in operation_urls:
            endpoint = self.parse_operation_page(
                self.fetch_html(operation_url),
                docs_url=operation_url,
            )
            if endpoint:
                endpoints.append(endpoint)
        endpoints.extend(_synthetic_list_endpoints(endpoints))
        return DocsSnapshot.create(source_url=index_url, endpoints=endpoints)

    def fetch_html(self, url: str) -> str:
        response = self._http.get(url)
        response.raise_for_status()
        return response.text

    def parse_index(self, html: str, *, index_url: str) -> list[str]:
        soup = BeautifulSoup(html, "html.parser")
        links: set[str] = set()
        for anchor in soup.find_all("a", href=True):
            href = str(anchor["href"])
            absolute = _without_fragment(urljoin(index_url, href))
            parsed = urlparse(absolute)
            if parsed.netloc and "learn.microsoft.com" not in parsed.netloc:
                continue
            if OPERATION_LINK_PATTERN.search(parsed.path):
                links.add(absolute)
        if links:
            return sorted(links)
        return self._discover_github_operation_urls(soup, index_url=index_url)

    def _discover_github_operation_urls(self, soup: BeautifulSoup, *, index_url: str) -> list[str]:
        edit_url = _github_edit_url(soup)
        if not edit_url:
            return []

        api_url = _github_api_directory_url(edit_url)
        if not api_url:
            return []

        response = self._http.get(api_url, headers={"Accept": "application/vnd.github+json"})
        response.raise_for_status()
        files = response.json()
        if not isinstance(files, list):
            return []

        operation_urls: list[str] = []
        for item in files:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", ""))
            if not re.fullmatch(r"dynamics_[^/]+\.md", name, re.I):
                continue
            operation = name.removesuffix(".md")
            operation_urls.append(urljoin(index_url, f"api/{operation}"))
        return sorted(operation_urls)

    def parse_operation_page(self, html: str, *, docs_url: str) -> Endpoint | None:
        soup = BeautifulSoup(html, "html.parser")
        title = _first_text(soup, ["h1"]) or _title_from_url(docs_url)
        summary = _summary_text(soup)
        operation_id = _title_from_url(docs_url)
        action = _action_from_operation_id(operation_id)
        resource = _resource_from_operation_id(operation_id)

        http_request = _section_code_text(soup, "HTTP request") or soup.get_text("\n")
        match = HTTP_REQUEST_PATTERN.search(http_request)
        if not match:
            return None

        method = match.group(1).upper()
        path = normalize_business_central_path(match.group(2))
        resource = _resource_from_path(path) or resource
        examples = tuple(_extract_examples(soup))
        return Endpoint(
            operation_id=operation_id,
            method=method,
            path=path,
            resource=resource,
            action=action,
            title=title,
            docs_url=docs_url,
            summary=summary,
            examples=examples,
        )


def normalize_business_central_path(raw_path: str) -> str:
    path = _normalize_doc_quotes(raw_path.strip().strip("`"))
    path = re.sub(r"^https://api\.businesscentral\.dynamics\.com/[^/]+/[^/]+/api/v2\.0", "", path)
    path = re.sub(r"^businesscentralPrefix", "", path)
    path = re.sub(r"^/api/v2\.0", "", path)
    path = re.sub(r"\(([A-Za-z][A-Za-z0-9_]*)\)", r"({\1})", path)
    path = re.sub(
        r"\{([A-Za-z][A-Za-z0-9_]*)\}",
        lambda m: "{" + _normalize_param_name(m.group(1)) + "}",
        path,
    )
    if not path.startswith("/"):
        path = f"/{path}"
    return _rename_generic_id_params(path)


def _without_fragment(url: str) -> str:
    parsed = urlparse(url)
    return parsed._replace(fragment="").geturl()


def _normalize_doc_quotes(text: str) -> str:
    return (
        text.replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )


def _github_edit_url(soup: BeautifulSoup) -> str | None:
    for anchor in soup.find_all("a", href=True):
        href = str(anchor["href"])
        if "github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/blob/" in href:
            return href
    return None


def _github_api_directory_url(edit_url: str) -> str | None:
    match = re.search(
        r"github\.com/MicrosoftDocs/dynamics365smb-devitpro-pb/blob/([^/]+)/(.*/)"
        r"index\.md$",
        edit_url,
    )
    if not match:
        return None
    branch = match.group(1)
    directory = match.group(2)
    return (
        "https://api.github.com/repos/MicrosoftDocs/dynamics365smb-devitpro-pb/"
        f"contents/{directory}api?ref={branch}"
    )


def _rename_generic_id_params(path: str) -> str:
    renamed_segments: list[str] = []
    for segment in path.split("/"):
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_]*)\(\{id\}\)", segment)
        if match:
            param = _id_param_name_for_collection(match.group(1))
            renamed_segments.append(f"{match.group(1)}({{{param}}})")
        else:
            renamed_segments.append(segment)
    return "/".join(renamed_segments)


def _id_param_name_for_collection(collection: str) -> str:
    singular = singularize(snake_case(collection))
    pascal = pascal_case(singular)
    return f"{pascal[0].lower()}{pascal[1:]}Id" if pascal else "id"


def _normalize_param_name(name: str) -> str:
    if name == "id":
        return name
    if name.islower() and name.endswith("id"):
        return f"{name[:-2]}Id"
    return name


def _first_text(soup: BeautifulSoup, selectors: Iterable[str]) -> str | None:
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            text = node.get_text(" ", strip=True)
            if text:
                return text
    return None


def _summary_text(soup: BeautifulSoup) -> str | None:
    description = soup.find("meta", attrs={"name": "description"})
    if description and description.get("content"):
        return str(description["content"]).strip()
    h1 = soup.find("h1")
    if isinstance(h1, Tag):
        sibling = h1.find_next_sibling()
        while isinstance(sibling, Tag):
            if sibling.name == "p":
                text = sibling.get_text(" ", strip=True)
                if text:
                    return text
            sibling = sibling.find_next_sibling()
    return None


def _section_code_text(soup: BeautifulSoup, heading_text: str) -> str | None:
    heading = _find_heading(soup, heading_text)
    if not heading:
        return None
    for sibling in heading.find_all_next():
        if isinstance(sibling, Tag) and sibling.name in {"h1", "h2", "h3"}:
            return None
        if isinstance(sibling, Tag) and sibling.name in {"pre", "code"}:
            text = sibling.get_text("\n", strip=True)
            if text:
                return text
    return None


def _find_heading(soup: BeautifulSoup, heading_text: str) -> Tag | None:
    expected = heading_text.casefold()
    for heading in soup.find_all(re.compile(r"^h[1-6]$")):
        if heading.get_text(" ", strip=True).casefold() == expected:
            return heading
    return None


def _extract_examples(soup: BeautifulSoup) -> list[Example]:
    examples: list[Example] = []
    for heading in soup.find_all(re.compile(r"^h[2-4]$")):
        title = heading.get_text(" ", strip=True)
        if "example" not in title.casefold():
            continue
        code_blocks: list[str] = []
        for sibling in heading.find_all_next():
            if (
                isinstance(sibling, Tag)
                and sibling.name in {"h1", "h2", "h3"}
                and sibling is not heading
            ):
                break
            if isinstance(sibling, Tag) and sibling.name == "pre":
                code_text = sibling.get_text("\n", strip=True)
                if code_text:
                    code_blocks.append(code_text)
        examples.append(
            Example(
                title=title,
                request=code_blocks[0] if code_blocks else None,
                response=code_blocks[1] if len(code_blocks) > 1 else None,
            )
        )
    return examples


def _title_from_url(url: str) -> str:
    return urlparse(url).path.rstrip("/").rsplit("/", 1)[-1]


def _action_from_operation_id(operation_id: str) -> str:
    suffix = operation_id.rsplit("_", 1)[-1].lower()
    if suffix in {"list", "getall"}:
        return "list"
    if suffix == "defaultdimensions":
        return "default_dimensions"
    if suffix == "pdfdocument":
        return "pdf_document"
    return snake_case(suffix)


def _resource_from_operation_id(operation_id: str) -> str:
    parts = operation_id.split("_")
    if parts and parts[0].lower() == "dynamics":
        parts = parts[1:]
    if parts and parts[-1].lower() in {
        "create",
        "delete",
        "get",
        "list",
        "post",
        "update",
    }:
        parts = parts[:-1]
    resource = snake_case("_".join(parts))
    return singularize(resource)


def _resource_from_path(path: str) -> str | None:
    path_no_query = path.split("?", 1)[0]
    segments = [segment for segment in path_no_query.split("/") if segment]
    if not segments:
        return None

    last = segments[-1]
    collection = re.sub(r"\([^)]*\)$", "", last)
    if collection.startswith("{") and len(segments) > 1:
        collection = re.sub(r"\([^)]*\)$", "", segments[-2])
    resource = singularize(snake_case(collection))
    return resource or None


def _synthetic_list_endpoints(endpoints: list[Endpoint]) -> list[Endpoint]:
    synthetic: list[Endpoint] = []
    existing_keys = {(endpoint.method, endpoint.path) for endpoint in endpoints}
    for endpoint in endpoints:
        if endpoint.method != "GET" or endpoint.action != "get":
            continue
        list_path = _collection_path_from_get_path(endpoint.path)
        if not list_path or ("GET", list_path) in existing_keys:
            continue
        collection_name = _collection_name_from_path(list_path)
        synthetic.append(
            Endpoint(
                operation_id=_list_operation_id(endpoint),
                method="GET",
                path=list_path,
                resource=endpoint.resource,
                action="list",
                title=f"List {collection_name}",
                docs_url=endpoint.docs_url,
                summary=f"List {collection_name} objects.",
                examples=(),
            )
        )
        existing_keys.add(("GET", list_path))
    return synthetic


def _collection_path_from_get_path(path: str) -> str | None:
    path_no_query = path.split("?", 1)[0]
    match = re.fullmatch(r"(.+)/([A-Za-z][A-Za-z0-9_]*)\([^)]*\)", path_no_query)
    if not match:
        return None
    return f"{match.group(1)}/{match.group(2)}"


def _collection_name_from_path(path: str) -> str:
    segments = [segment for segment in path.split("/") if segment]
    return segments[-1] if segments else "items"


def _list_operation_id(endpoint: Endpoint) -> str:
    if endpoint.operation_id.endswith("_get"):
        return f"{endpoint.operation_id[:-4]}_list"
    return f"{endpoint.operation_id}_list"

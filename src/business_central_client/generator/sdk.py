from __future__ import annotations

import re
from collections import defaultdict
from textwrap import indent

from business_central_client.generator.ir import DocsSnapshot, Endpoint
from business_central_client.generator.names import pascal_case, pluralize, snake_case

HEADER = '''from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from urllib.parse import quote

from business_central_client.client import BusinessCentralClient
from business_central_client.odata import ODataQuery


def _path_value(value: str) -> str:
    return quote(str(value), safe="")


class _EntityClient:
    def __init__(self, client: BusinessCentralClient) -> None:
        self._client = client


class BusinessCentralAPI:
    """Generated entity-scoped facade for Microsoft Dynamics 365 Business Central API v2.0."""

    def __init__(self, client: BusinessCentralClient) -> None:
        self._client = client
'''


def render_sdk(snapshot: DocsSnapshot) -> str:
    endpoints = sorted(
        snapshot.all_endpoints(),
        key=lambda endpoint: (
            endpoint.resource,
            endpoint.action,
            endpoint.method,
            endpoint.path,
            endpoint.operation_id,
        ),
    )
    grouped = _group_endpoints(endpoints)

    body = HEADER
    if not grouped:
        return body + "\n"

    for resource in grouped:
        body += _render_api_property(resource)
    body += "\n"

    for resource, resource_endpoints in grouped.items():
        body += "\n" + _render_entity_class(resource, resource_endpoints)
    return body


def _group_endpoints(endpoints: list[Endpoint]) -> dict[str, list[Endpoint]]:
    grouped: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints:
        grouped[endpoint.resource].append(endpoint)
    return dict(sorted(grouped.items()))


def _render_api_property(resource: str) -> str:
    property_name = pluralize(snake_case(resource))
    class_name = _entity_class_name(resource)
    return f'''
    @property
    def {property_name}(self) -> {class_name}:
        """Operations for ``{property_name}``."""

        return {class_name}(self._client)
'''


def _render_entity_class(resource: str, endpoints: list[Endpoint]) -> str:
    class_name = _entity_class_name(resource)
    body = f'''class {class_name}(_EntityClient):
    """Generated operations for ``{pluralize(snake_case(resource))}``."""
'''

    used_names: set[str] = set()
    for endpoint in endpoints:
        body += "\n" + _render_endpoint_method(endpoint, used_names)
    return body


def _render_endpoint_method(endpoint: Endpoint, used_names: set[str]) -> str:
    method_name = _method_name(endpoint)
    if method_name in used_names:
        method_name = f"{method_name}_{_operation_suffix(endpoint)}"
    used_names.add(method_name)

    path_params = endpoint.path_params
    signature_params = "".join(f"        {snake_case(param)}: str,\n" for param in path_params)
    body_param = _body_param(endpoint)
    etag_param = _etag_param(endpoint)
    docstring = _docstring(endpoint)
    path_expression = _path_expression(endpoint.path)
    call = _client_call(endpoint)
    return_type = _return_type(endpoint)

    source = f'''    def {method_name}(
        self,
{signature_params}{body_param}        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
{etag_param}    ) -> {return_type}:
{indent(docstring, "        ")}

        path = {path_expression}
{call}
'''
    return source


def _method_name(endpoint: Endpoint) -> str:
    if endpoint.action == "list":
        return "list"
    return snake_case(endpoint.action)


def _operation_suffix(endpoint: Endpoint) -> str:
    operation = snake_case(endpoint.operation_id)
    resource = snake_case(endpoint.resource)
    operation = operation.removeprefix("dynamics_")
    operation = operation.removeprefix(f"{resource}_")
    return operation or snake_case(endpoint.method.lower())


def _body_param(endpoint: Endpoint) -> str:
    if endpoint.method in {"POST", "PATCH", "PUT"}:
        return "        body: Mapping[str, Any] | None = None,\n"
    return ""


def _etag_param(endpoint: Endpoint) -> str:
    if endpoint.method in {"PATCH", "DELETE"}:
        return "        etag: str | None = None,\n"
    return ""


def _client_call(endpoint: Endpoint) -> str:
    if endpoint.method == "GET" and endpoint.action == "list":
        return "        return self._client.get_value(path, query=query, params=params)"
    if endpoint.method == "GET":
        return "        return self._client.get(path, query=query, params=params)"
    if endpoint.method == "POST":
        return "        return self._client.post(path, json=body, query=query, params=params)"
    if endpoint.method in {"PATCH", "PUT"}:
        return (
            "        return self._client.patch(\n"
            "            path,\n"
            "            json=body,\n"
            "            query=query,\n"
            "            params=params,\n"
            "            etag=etag,\n"
            "        )"
        )
    if endpoint.method == "DELETE":
        return "        return self._client.delete(path, query=query, params=params, etag=etag)"
    return (
        f'        return self._client.request("{endpoint.method}", '
        "path, query=query, params=params)"
    )


def _return_type(endpoint: Endpoint) -> str:
    if endpoint.method == "DELETE":
        return "None"
    if endpoint.method == "GET" and endpoint.action == "list":
        return "list[dict[str, Any]]"
    return "dict[str, Any]"


def _docstring(endpoint: Endpoint) -> str:
    lines = [f'"""{endpoint.title}']
    if endpoint.summary:
        lines.extend(["", _escape_docstring(endpoint.summary)])
    lines.extend(
        [
            "",
            f"HTTP method: {endpoint.method}",
            f"Docs: {endpoint.docs_url}",
            f"Operation id: {endpoint.operation_id}",
        ]
    )
    example = endpoint.examples[0] if endpoint.examples else None
    if example and example.request:
        snippet = _escape_docstring(_trim_example(example.request))
        lines.extend(["", "Example request:", snippet])
    if example and example.response:
        snippet = _escape_docstring(_trim_example(example.response))
        lines.extend(["", "Example response:", snippet])
    lines.append('"""')
    return "\n".join(lines)


def _path_expression(path: str) -> str:
    parts: list[str] = []
    cursor = 0
    for match in re.finditer(r"{([A-Za-z_][A-Za-z0-9_]*)}", path):
        if match.start() > cursor:
            parts.append(repr(path[cursor : match.start()]))
        parts.append(f"_path_value({snake_case(match.group(1))})")
        cursor = match.end()
    if cursor < len(path):
        parts.append(repr(path[cursor:]))
    if not parts:
        return repr(path)
    expression = " + ".join(parts)
    if len(expression) <= 80:
        return expression
    return "(\n            " + "\n            + ".join(parts) + "\n        )"


def _entity_class_name(resource: str) -> str:
    return f"{pascal_case(pluralize(resource))}Client"


def _trim_example(text: str, *, max_lines: int = 12) -> str:
    lines = [_trim_line(line.rstrip()) for line in text.strip().splitlines()]
    if len(lines) > max_lines:
        lines = [*lines[:max_lines], "..."]
    return "\n".join(lines)


def _trim_line(text: str, *, max_chars: int = 88) -> str:
    if len(text) <= max_chars:
        return text
    return f"{text[: max_chars - 3]}..."


def _escape_docstring(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"""', r"\"\"\"")


__all__ = ["render_sdk"]

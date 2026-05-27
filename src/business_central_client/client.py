from __future__ import annotations

from collections.abc import Iterator, Mapping
from typing import TYPE_CHECKING, Any

import httpx

from business_central_client.auth import CertificateTokenProvider, TokenProvider
from business_central_client.config import BusinessCentralConfig
from business_central_client.errors import BusinessCentralAPIError
from business_central_client.odata import ODataQuery, merge_query_params

if TYPE_CHECKING:
    from business_central_client.generated import BusinessCentralAPI


class BusinessCentralClient:
    """HTTP client for Microsoft Dynamics 365 Business Central API v2.0."""

    def __init__(
        self,
        config: BusinessCentralConfig,
        *,
        token_provider: TokenProvider | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.config = config
        self._token_provider = token_provider or CertificateTokenProvider(config)
        self._owns_http_client = http_client is None
        self._http = http_client or httpx.Client(
            base_url=config.base_url,
            timeout=config.timeout_seconds,
            headers={"Accept": "application/json", **dict(config.extra_headers)},
        )

    def __enter__(self) -> BusinessCentralClient:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def close(self) -> None:
        if self._owns_http_client:
            self._http.close()

    @property
    def api(self) -> BusinessCentralAPI:
        """Generated entity-scoped Business Central API facade."""

        from business_central_client.generated import BusinessCentralAPI

        return BusinessCentralAPI(self)

    @property
    def read(self) -> BusinessCentralAPI:
        """Backward-compatible alias for :attr:`api`."""

        return self.api

    def get(
        self,
        path: str,
        *,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Perform a GET request and return the decoded JSON object."""

        response = self._request("GET", path, params=merge_query_params(query, params))
        return _json_object(response)

    def get_value(
        self,
        path: str,
        *,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Perform a GET request and return the OData ``value`` collection."""

        data = self.get(path, query=query, params=params)
        value = data.get("value")
        if not isinstance(value, list):
            raise BusinessCentralAPIError("Business Central response did not contain a list value")
        return [item for item in value if isinstance(item, dict)]

    def iter_pages(
        self,
        path: str,
        *,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Yield decoded response pages, following ``@odata.nextLink`` when present."""

        request_path = path
        request_params: Mapping[str, Any] | None = merge_query_params(query, params)
        while True:
            page = self.get(request_path, params=request_params)
            yield page
            next_link = page.get("@odata.nextLink")
            if not isinstance(next_link, str) or not next_link:
                return
            request_path = next_link
            request_params = None

    def iter_values(
        self,
        path: str,
        *,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Yield items from all pages in a collection response."""

        for page in self.iter_pages(path, query=query, params=params):
            value = page.get("value", [])
            if not isinstance(value, list):
                raise BusinessCentralAPIError(
                    "Business Central response did not contain a list value"
                )
            for item in value:
                if isinstance(item, dict):
                    yield item

    def post(
        self,
        path: str,
        *,
        json: Mapping[str, Any] | None = None,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Perform a POST request and return the decoded JSON object."""

        response = self._request(
            "POST",
            path,
            params=merge_query_params(query, params),
            json=json,
        )
        return _json_object(response)

    def patch(
        self,
        path: str,
        *,
        json: Mapping[str, Any] | None = None,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        etag: str | None = None,
    ) -> dict[str, Any]:
        """Perform a PATCH request and return the decoded JSON object."""

        headers = {"If-Match": etag} if etag else None
        response = self._request(
            "PATCH",
            path,
            params=merge_query_params(query, params),
            json=json,
            headers=headers,
        )
        if response.status_code == 204 or not response.content:
            return {}
        return _json_object(response)

    def delete(
        self,
        path: str,
        *,
        query: ODataQuery | Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Perform a DELETE request."""

        headers = {"If-Match": etag} if etag else None
        self._request(
            "DELETE",
            path,
            params=merge_query_params(query, params),
            headers=headers,
        )

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        request_headers = {"Authorization": f"Bearer {self._token_provider.get_token()}"}
        if headers:
            request_headers.update(headers)
        response = self._http.request(
            method,
            path,
            params=params,
            json=json,
            headers=request_headers,
        )
        if response.is_success:
            return response

        request_id = response.headers.get("request-id") or response.headers.get("x-ms-request-id")
        try:
            body: Any = response.json()
            message = _extract_error_message(body)
        except ValueError:
            body = response.text
            message = response.text or response.reason_phrase

        raise BusinessCentralAPIError(
            message,
            status_code=response.status_code,
            response_body=body,
            request_id=request_id,
        )


def _json_object(response: httpx.Response) -> dict[str, Any]:
    data = response.json()
    if not isinstance(data, dict):
        raise BusinessCentralAPIError("Business Central returned a non-object JSON response")
    return data


def _extract_error_message(body: Any) -> str:
    if isinstance(body, dict):
        error = body.get("error")
        if isinstance(error, dict):
            message = error.get("message")
            if isinstance(message, str):
                return message
        message = body.get("message")
        if isinstance(message, str):
            return message
    return "Business Central API request failed"

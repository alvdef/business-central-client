import json

import httpx

from business_central_client.auth import StaticTokenProvider
from business_central_client.client import BusinessCentralClient
from business_central_client.config import BusinessCentralConfig
from business_central_client.odata import ODataQuery


def test_client_sends_bearer_token_and_query_params() -> None:
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["authorization"] = request.headers["authorization"]
        seen["url"] = str(request.url)
        return httpx.Response(200, json={"value": [{"id": "1"}]})

    http_client = httpx.Client(
        base_url="https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0",
        transport=httpx.MockTransport(handler),
    )
    client = BusinessCentralClient(
        _config(),
        token_provider=StaticTokenProvider("token"),
        http_client=http_client,
    )

    value = client.get_value(
        "/companies",
        query=ODataQuery(select=("id", "name"), top=1),
    )

    assert value == [{"id": "1"}]
    assert seen["authorization"] == "Bearer token"
    assert "%24select=id%2Cname" in seen["url"]
    assert "%24top=1" in seen["url"]


def test_client_iter_values_follows_next_link() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        if len(calls) == 1:
            return httpx.Response(
                200,
                json={
                    "value": [{"id": "1"}],
                    "@odata.nextLink": "/companies?$skip=1",
                },
            )
        return httpx.Response(200, json={"value": [{"id": "2"}]})

    http_client = httpx.Client(
        base_url="https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0",
        transport=httpx.MockTransport(handler),
    )
    client = BusinessCentralClient(
        _config(),
        token_provider=StaticTokenProvider("token"),
        http_client=http_client,
    )

    assert list(client.iter_values("/companies")) == [{"id": "1"}, {"id": "2"}]
    assert len(calls) == 2


def test_client_write_methods_send_body_and_etag() -> None:
    seen: list[tuple[str, str, str | None, dict[str, object] | None]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        json_body = None
        if request.content:
            json_body = json.loads(request.content.decode("utf-8"))
        seen.append(
            (
                request.method,
                str(request.url),
                request.headers.get("if-match"),
                json_body,
            )
        )
        status_code = 204 if request.method == "DELETE" else 200
        return httpx.Response(status_code, json={} if request.method != "DELETE" else None)

    http_client = httpx.Client(
        base_url="https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0",
        transport=httpx.MockTransport(handler),
    )
    client = BusinessCentralClient(
        _config(),
        token_provider=StaticTokenProvider("token"),
        http_client=http_client,
    )

    client.post("/companies(company)/salesQuotes", json={"number": "SQ1"})
    client.patch("/companies(company)/salesQuotes(quote)", json={"number": "SQ2"}, etag="etag")
    client.delete("/companies(company)/salesQuotes(quote)", etag="etag")

    assert seen == [
        (
            "POST",
            "https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0"
            "/companies(company)/salesQuotes",
            None,
            {"number": "SQ1"},
        ),
        (
            "PATCH",
            "https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0"
            "/companies(company)/salesQuotes(quote)",
            "etag",
            {"number": "SQ2"},
        ),
        (
            "DELETE",
            "https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0"
            "/companies(company)/salesQuotes(quote)",
            "etag",
            None,
        ),
    ]


def _config() -> BusinessCentralConfig:
    return BusinessCentralConfig(
        tenant_id="tenant",
        client_id="client",
        certificate_path=None,
        certificate_thumbprint=None,
    )

from typing import Any

from business_central_client.generated import BusinessCentralAPI
from business_central_client.generated.models import SalesQuote, SalesQuoteCreate


class FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []

    def get(
        self,
        path: str,
        *,
        query: object | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        self.calls.append(("get", path))
        return {"path": path}

    def get_value(
        self,
        path: str,
        *,
        query: object | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        self.calls.append(("get_value", path))
        return [{"path": path}]

    def post(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        query: object | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        self.calls.append(("post", path))
        return {"path": path, "json": json}


def test_checked_in_generated_sales_quote_methods_build_paths() -> None:
    client = FakeClient()
    endpoints = BusinessCentralAPI(client)  # type: ignore[arg-type]

    quote = endpoints.sales_quotes.get("company id", "quote/id")
    quotes = endpoints.sales_quotes.list("company id")
    created = endpoints.sales_quotes.create("company id", SalesQuoteCreate(number="SQ1001"))

    assert quote.model_extra == {"path": "/companies(company%20id)/salesQuotes(quote%2Fid)"}
    assert [item.model_extra for item in quotes] == [
        {"path": "/companies(company%20id)/salesQuotes"}
    ]
    assert created.model_extra == {
        "path": "/companies(company%20id)/salesQuotes",
        "json": {"number": "SQ1001"},
    }
    assert isinstance(quote, SalesQuote)
    assert isinstance(created, SalesQuote)
    assert client.calls == [
        ("get", "/companies(company%20id)/salesQuotes(quote%2Fid)"),
        ("get_value", "/companies(company%20id)/salesQuotes"),
        ("post", "/companies(company%20id)/salesQuotes"),
    ]

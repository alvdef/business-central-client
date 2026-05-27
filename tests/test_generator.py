from business_central_client.generator.ir import DocsSnapshot, Endpoint
from business_central_client.generator.sdk import render_sdk


def test_render_sdk_generates_entity_scoped_methods_with_doc_links() -> None:
    snapshot = DocsSnapshot.create(
        source_url="https://learn.microsoft.com/example",
        endpoints=[
            Endpoint(
                operation_id="dynamics_salesquote_create",
                method="POST",
                path="/companies({companyId})/salesQuotes",
                resource="sales_quote",
                action="create",
                title="Create salesQuote",
                docs_url="https://learn.microsoft.com/create",
                summary="Create one sales quote.",
            ),
            Endpoint(
                operation_id="dynamics_salesquote_get",
                method="GET",
                path="/companies({companyId})/salesQuotes({salesQuoteId})",
                resource="sales_quote",
                action="get",
                title="Get salesQuote",
                docs_url="https://learn.microsoft.com/get",
                summary="Retrieve one sales quote.",
            ),
        ],
    )

    generated = render_sdk(snapshot)

    assert "def sales_quotes(self) -> SalesQuotesClient:" in generated
    assert "class SalesQuotesClient(_EntityClient):" in generated
    assert "def create(" in generated
    assert "def get(" in generated
    assert "company_id: str" in generated
    assert "sales_quote_id: str" in generated
    assert "body: Mapping[str, Any] | None = None" in generated
    assert "Docs: https://learn.microsoft.com/get" in generated
    assert "return self._client.post(path, json=body, query=query, params=params)" in generated


def test_render_sdk_is_deterministic() -> None:
    endpoints = [
        Endpoint(
            operation_id="dynamics_customer_get",
            method="GET",
            path="/companies({companyId})/customers({customerId})",
            resource="customer",
            action="get",
            title="Get customer",
            docs_url="https://learn.microsoft.com/customer",
        )
    ]
    first = render_sdk(DocsSnapshot.create(source_url="x", endpoints=endpoints))
    second = render_sdk(DocsSnapshot.create(source_url="x", endpoints=endpoints))

    assert first == second

from business_central_client.generator.contract import build_contract
from business_central_client.generator.ir import DocsSnapshot, Endpoint, Example
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
                examples=(
                    Example(
                        title="Example",
                        request='POST /salesQuotes\n{"number": "SQ1001"}',
                        response=(
                            '{"id": "00000000-0000-0000-0000-000000000000", '
                            '"number": "SQ1001"}'
                        ),
                    ),
                ),
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
                examples=(
                    Example(
                        title="Example",
                        request="GET /salesQuotes({id})",
                        response=(
                            '{"id": "00000000-0000-0000-0000-000000000000", '
                            '"number": "SQ1001"}'
                        ),
                    ),
                ),
            ),
        ],
    )

    generated = render_sdk(build_contract(snapshot))

    assert "def sales_quotes(self) -> SalesQuotesClient:" in generated
    assert "class SalesQuotesClient(_EntityClient):" in generated
    assert "def create(" in generated
    assert "def get(" in generated
    assert "company_id: str" in generated
    assert "sales_quote_id: str" in generated
    assert "body: _models.SalesQuoteCreate | Mapping[str, Any] | None = None" in generated
    assert "Docs: https://learn.microsoft.com/get" in generated
    assert "return _models.SalesQuote.model_validate(data)" in generated


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
    first = render_sdk(build_contract(DocsSnapshot.create(source_url="x", endpoints=endpoints)))
    second = render_sdk(build_contract(DocsSnapshot.create(source_url="x", endpoints=endpoints)))

    assert first == second

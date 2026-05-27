from business_central_client.generator.contract import build_contract
from business_central_client.generator.ir import DocsSnapshot, Endpoint, Example


def test_contract_infers_response_and_request_models_from_examples() -> None:
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
                examples=(
                    Example(
                        title="Example",
                        request='POST /salesQuotes\n{"documentDate": "2024-01-31"}',
                        response='{"id": "quote-id", "totalAmountIncludingTax": 10.5}',
                    ),
                ),
            )
        ],
    )

    contract = build_contract(snapshot)
    operation = contract.operations[0]
    models = contract.model_by_name()

    assert operation.request_model == "SalesQuoteCreate"
    assert operation.response_model == "SalesQuote"
    create_fields = {field.name: field for field in models["SalesQuoteCreate"].fields}
    response_fields = {field.name: field for field in models["SalesQuote"].fields}
    assert create_fields["document_date"].type == "date"
    assert response_fields["total_amount_including_tax"].type == "Decimal"

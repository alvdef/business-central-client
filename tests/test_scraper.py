from pathlib import Path

from business_central_client.generator.ir import Endpoint
from business_central_client.generator.scraper import (
    DocsScraper,
    _synthetic_list_endpoints,
    normalize_business_central_path,
)

FIXTURES = Path(__file__).parent / "fixtures"
INDEX_URL = "https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/"


def test_parse_index_discovers_operation_links() -> None:
    html = (FIXTURES / "index.html").read_text(encoding="utf-8")
    scraper = DocsScraper()
    try:
        links = scraper.parse_index(html, index_url=INDEX_URL)
    finally:
        scraper.close()

    assert links == [
        "https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_create",
        "https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_get",
        "https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_list",
    ]


def test_parse_operation_page_extracts_read_endpoint() -> None:
    html = (FIXTURES / "salesquote_get.html").read_text(encoding="utf-8")
    scraper = DocsScraper()
    try:
        endpoint = scraper.parse_operation_page(
            html,
            docs_url=(
                "https://learn.microsoft.com/en-us/dynamics365/business-central/"
                "dev-itpro/api-reference/v2.0/api/dynamics_salesquote_get"
            ),
        )
    finally:
        scraper.close()

    assert endpoint is not None
    assert endpoint.method == "GET"
    assert endpoint.path == "/companies({companyId})/salesQuotes({salesQuoteId})"
    assert endpoint.path_params == ("companyId", "salesQuoteId")
    assert endpoint.resource == "sales_quote"
    assert endpoint.action == "get"
    assert endpoint.summary is not None


def test_normalize_business_central_path_handles_full_api_url() -> None:
    assert (
        normalize_business_central_path(
            "https://api.businesscentral.dynamics.com/v2.0/production/api/v2.0/companies({id})/customers"
        )
        == "/companies({companyId})/customers"
    )


def test_synthetic_list_endpoints_are_derived_from_get_paths() -> None:
    endpoints = [
        Endpoint(
            operation_id="dynamics_salesquote_get",
            method="GET",
            path="/companies({companyId})/salesQuotes({salesQuoteId})",
            resource="sales_quote",
            action="get",
            title="Get salesQuote",
            docs_url="https://learn.microsoft.com/get",
        )
    ]

    synthetic = _synthetic_list_endpoints(endpoints)

    assert len(synthetic) == 1
    assert synthetic[0].operation_id == "dynamics_salesquote_list"
    assert synthetic[0].path == "/companies({companyId})/salesQuotes"
    assert synthetic[0].action == "list"

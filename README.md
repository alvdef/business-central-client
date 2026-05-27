# Business Central Client

Generated Python SDK for Microsoft Dynamics 365 Business Central API v2.0.

The project is built around a deterministic pipeline:

```text
Microsoft Learn docs -> normalized IR JSON -> generated SDK methods
```

That keeps scraping concerns out of the runtime client and makes daily regeneration reviewable in pull requests.

## Current Scope

- Certificate-based client credentials auth through Microsoft Entra ID.
- HTTP runtime for Business Central API v2.0, including GET, POST, PATCH, and DELETE.
- Scraper for Microsoft Learn API operation pages.
- Normalized intermediate representation.
- Deterministic entity-scoped Python method generator.
- CLI commands for scraping, generating, and regenerating.
- GitHub Actions workflow for daily regeneration.

## Install For Development

```bash
uv sync --extra dev
```

or:

```bash
python -m pip install -e ".[dev]"
```

## Usage

```python
from business_central_client import BusinessCentralClient, BusinessCentralConfig
from business_central_client.generated.models import SalesQuoteCreate

config = BusinessCentralConfig(
    tenant_id="00000000-0000-0000-0000-000000000000",
    client_id="00000000-0000-0000-0000-000000000000",
    certificate_path="./certificate.pem",
    certificate_thumbprint="ABCDEF123456...",
    environment="production",
)

with BusinessCentralClient(config) as client:
    companies = client.api.companies.list()
    sales_quotes = client.api.sales_quotes.list(company_id="company-guid")
    sales_quote = client.api.sales_quotes.get(
        company_id="company-guid",
        sales_quote_id="quote-guid",
    )
    created = client.api.sales_quotes.create(
        company_id="company-guid",
        body=SalesQuoteCreate(customer_number="10000"),
    )
```

Generated methods are exposed through `client.api`, grouped by entity. Generated
Pydantic models are exposed through `business_central_client.generated.models`.

## Regenerate From Microsoft Learn

```bash
bc-client regenerate \
  --index-url https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/ \
  --ir-path docs/business-central-v2.ir.json \
  --contract-path docs/business-central-v2.contract.json \
  --models-output src/business_central_client/generated/models.py \
  --output src/business_central_client/generated/resources.py
```

The scraper stores docs URLs and examples in the endpoint IR. The contract graph
then infers request/response models, field aliases, field types, and operation
return types before rendering the SDK.

## Development Checks

```bash
pytest
ruff check .
```

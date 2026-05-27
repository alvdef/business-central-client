from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from urllib.parse import quote

from business_central_client.client import BusinessCentralClient
from business_central_client.generated import models as _models
from business_central_client.odata import ODataQuery


def _path_value(value: str) -> str:
    return quote(str(value), safe="")


def _body_payload(
    body: _models.BusinessCentralModel | Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if body is None:
        return None
    if isinstance(body, _models.BusinessCentralModel):
        return body.model_dump(by_alias=True, exclude_none=True)
    return body


class _EntityClient:
    def __init__(self, client: BusinessCentralClient) -> None:
        self._client = client


class BusinessCentralAPI:
    """Generated entity-scoped facade for Microsoft Dynamics 365 Business Central API v2.0."""

    def __init__(self, client: BusinessCentralClient) -> None:
        self._client = client

    @property
    def accounts(self) -> AccountsClient:
        """Operations for ``accounts``."""

        return AccountsClient(self._client)

    @property
    def accounting_periods(self) -> AccountingPeriodsClient:
        """Operations for ``accounting_periods``."""

        return AccountingPeriodsClient(self._client)

    @property
    def aged_accounts_payables(self) -> AgedAccountsPayablesClient:
        """Operations for ``aged_accounts_payables``."""

        return AgedAccountsPayablesClient(self._client)

    @property
    def aged_accounts_receivables(self) -> AgedAccountsReceivablesClient:
        """Operations for ``aged_accounts_receivables``."""

        return AgedAccountsReceivablesClient(self._client)

    @property
    def apply_vendor_entries(self) -> ApplyVendorEntriesClient:
        """Operations for ``apply_vendor_entries``."""

        return ApplyVendorEntriesClient(self._client)

    @property
    def attachments(self) -> AttachmentsClient:
        """Operations for ``attachments``."""

        return AttachmentsClient(self._client)

    @property
    def attachment_contents(self) -> AttachmentContentsClient:
        """Operations for ``attachment_contents``."""

        return AttachmentContentsClient(self._client)

    @property
    def balance_sheets(self) -> BalanceSheetsClient:
        """Operations for ``balance_sheets``."""

        return BalanceSheetsClient(self._client)

    @property
    def bank_accounts(self) -> BankAccountsClient:
        """Operations for ``bank_accounts``."""

        return BankAccountsClient(self._client)

    @property
    def cash_flow_statements(self) -> CashFlowStatementsClient:
        """Operations for ``cash_flow_statements``."""

        return CashFlowStatementsClient(self._client)

    @property
    def companies(self) -> CompaniesClient:
        """Operations for ``companies``."""

        return CompaniesClient(self._client)

    @property
    def company_informations(self) -> CompanyInformationsClient:
        """Operations for ``company_informations``."""

        return CompanyInformationsClient(self._client)

    @property
    def contacts(self) -> ContactsClient:
        """Operations for ``contacts``."""

        return ContactsClient(self._client)

    @property
    def contacts_informations(self) -> ContactsInformationsClient:
        """Operations for ``contacts_informations``."""

        return ContactsInformationsClient(self._client)

    @property
    def contents(self) -> ContentsClient:
        """Operations for ``contents``."""

        return ContentsClient(self._client)

    @property
    def countries_regions(self) -> CountriesRegionsClient:
        """Operations for ``countries_regions``."""

        return CountriesRegionsClient(self._client)

    @property
    def currencies(self) -> CurrenciesClient:
        """Operations for ``currencies``."""

        return CurrenciesClient(self._client)

    @property
    def currency_exchange_rates(self) -> CurrencyExchangeRatesClient:
        """Operations for ``currency_exchange_rates``."""

        return CurrencyExchangeRatesClient(self._client)

    @property
    def customers(self) -> CustomersClient:
        """Operations for ``customers``."""

        return CustomersClient(self._client)

    @property
    def customer_contacts(self) -> CustomerContactsClient:
        """Operations for ``customer_contacts``."""

        return CustomerContactsClient(self._client)

    @property
    def customer_financial_details(self) -> CustomerFinancialDetailsClient:
        """Operations for ``customer_financial_details``."""

        return CustomerFinancialDetailsClient(self._client)

    @property
    def customer_payments(self) -> CustomerPaymentsClient:
        """Operations for ``customer_payments``."""

        return CustomerPaymentsClient(self._client)

    @property
    def customer_payment_journals(self) -> CustomerPaymentJournalsClient:
        """Operations for ``customer_payment_journals``."""

        return CustomerPaymentJournalsClient(self._client)

    @property
    def customer_return_reasons(self) -> CustomerReturnReasonsClient:
        """Operations for ``customer_return_reasons``."""

        return CustomerReturnReasonsClient(self._client)

    @property
    def customer_sales(self) -> CustomerSalesClient:
        """Operations for ``customer_sales``."""

        return CustomerSalesClient(self._client)

    @property
    def default_dimensions(self) -> DefaultDimensionsClient:
        """Operations for ``default_dimensions``."""

        return DefaultDimensionsClient(self._client)

    @property
    def dimensions(self) -> DimensionsClient:
        """Operations for ``dimensions``."""

        return DimensionsClient(self._client)

    @property
    def dimension_set_lines(self) -> DimensionSetLinesClient:
        """Operations for ``dimension_set_lines``."""

        return DimensionSetLinesClient(self._client)

    @property
    def dimension_values(self) -> DimensionValuesClient:
        """Operations for ``dimension_values``."""

        return DimensionValuesClient(self._client)

    @property
    def dispute_status(self) -> DisputeStatusClient:
        """Operations for ``dispute_status``."""

        return DisputeStatusClient(self._client)

    @property
    def document_attachments(self) -> DocumentAttachmentsClient:
        """Operations for ``document_attachments``."""

        return DocumentAttachmentsClient(self._client)

    @property
    def employees(self) -> EmployeesClient:
        """Operations for ``employees``."""

        return EmployeesClient(self._client)

    @property
    def fixed_assets(self) -> FixedAssetsClient:
        """Operations for ``fixed_assets``."""

        return FixedAssetsClient(self._client)

    @property
    def fixed_asset_locations(self) -> FixedAssetLocationsClient:
        """Operations for ``fixed_asset_locations``."""

        return FixedAssetLocationsClient(self._client)

    @property
    def general_ledger_entries(self) -> GeneralLedgerEntriesClient:
        """Operations for ``general_ledger_entries``."""

        return GeneralLedgerEntriesClient(self._client)

    @property
    def general_ledger_setups(self) -> GeneralLedgerSetupsClient:
        """Operations for ``general_ledger_setups``."""

        return GeneralLedgerSetupsClient(self._client)

    @property
    def general_product_posting_groups(self) -> GeneralProductPostingGroupsClient:
        """Operations for ``general_product_posting_groups``."""

        return GeneralProductPostingGroupsClient(self._client)

    @property
    def income_statements(self) -> IncomeStatementsClient:
        """Operations for ``income_statements``."""

        return IncomeStatementsClient(self._client)

    @property
    def inventory_posting_groups(self) -> InventoryPostingGroupsClient:
        """Operations for ``inventory_posting_groups``."""

        return InventoryPostingGroupsClient(self._client)

    @property
    def items(self) -> ItemsClient:
        """Operations for ``items``."""

        return ItemsClient(self._client)

    @property
    def item_categories(self) -> ItemCategoriesClient:
        """Operations for ``item_categories``."""

        return ItemCategoriesClient(self._client)

    @property
    def item_ledger_entries(self) -> ItemLedgerEntriesClient:
        """Operations for ``item_ledger_entries``."""

        return ItemLedgerEntriesClient(self._client)

    @property
    def item_variants(self) -> ItemVariantsClient:
        """Operations for ``item_variants``."""

        return ItemVariantsClient(self._client)

    @property
    def job_queue_entries(self) -> JobQueueEntriesClient:
        """Operations for ``job_queue_entries``."""

        return JobQueueEntriesClient(self._client)

    @property
    def job_queue_log_entries(self) -> JobQueueLogEntriesClient:
        """Operations for ``job_queue_log_entries``."""

        return JobQueueLogEntriesClient(self._client)

    @property
    def journals(self) -> JournalsClient:
        """Operations for ``journals``."""

        return JournalsClient(self._client)

    @property
    def journal_lines(self) -> JournalLinesClient:
        """Operations for ``journal_lines``."""

        return JournalLinesClient(self._client)

    @property
    def locations(self) -> LocationsClient:
        """Operations for ``locations``."""

        return LocationsClient(self._client)

    @property
    def opportunities(self) -> OpportunitiesClient:
        """Operations for ``opportunities``."""

        return OpportunitiesClient(self._client)

    @property
    def payment_methods(self) -> PaymentMethodsClient:
        """Operations for ``payment_methods``."""

        return PaymentMethodsClient(self._client)

    @property
    def payment_terms(self) -> PaymentTermsClient:
        """Operations for ``payment_terms``."""

        return PaymentTermsClient(self._client)

    @property
    def pdf_documents(self) -> PdfDocumentsClient:
        """Operations for ``pdf_documents``."""

        return PdfDocumentsClient(self._client)

    @property
    def pictures(self) -> PicturesClient:
        """Operations for ``pictures``."""

        return PicturesClient(self._client)

    @property
    def picture_contents(self) -> PictureContentsClient:
        """Operations for ``picture_contents``."""

        return PictureContentsClient(self._client)

    @property
    def projects(self) -> ProjectsClient:
        """Operations for ``projects``."""

        return ProjectsClient(self._client)

    @property
    def purchase_credit_memos(self) -> PurchaseCreditMemosClient:
        """Operations for ``purchase_credit_memos``."""

        return PurchaseCreditMemosClient(self._client)

    @property
    def purchase_credit_memo_lines(self) -> PurchaseCreditMemoLinesClient:
        """Operations for ``purchase_credit_memo_lines``."""

        return PurchaseCreditMemoLinesClient(self._client)

    @property
    def purchase_invoices(self) -> PurchaseInvoicesClient:
        """Operations for ``purchase_invoices``."""

        return PurchaseInvoicesClient(self._client)

    @property
    def purchase_invoice_lines(self) -> PurchaseInvoiceLinesClient:
        """Operations for ``purchase_invoice_lines``."""

        return PurchaseInvoiceLinesClient(self._client)

    @property
    def purchase_orders(self) -> PurchaseOrdersClient:
        """Operations for ``purchase_orders``."""

        return PurchaseOrdersClient(self._client)

    @property
    def purchase_order_lines(self) -> PurchaseOrderLinesClient:
        """Operations for ``purchase_order_lines``."""

        return PurchaseOrderLinesClient(self._client)

    @property
    def purchase_receipts(self) -> PurchaseReceiptsClient:
        """Operations for ``purchase_receipts``."""

        return PurchaseReceiptsClient(self._client)

    @property
    def purchase_receipt_lines(self) -> PurchaseReceiptLinesClient:
        """Operations for ``purchase_receipt_lines``."""

        return PurchaseReceiptLinesClient(self._client)

    @property
    def retained_earnings_statements(self) -> RetainedEarningsStatementsClient:
        """Operations for ``retained_earnings_statements``."""

        return RetainedEarningsStatementsClient(self._client)

    @property
    def sales_credit_memos(self) -> SalesCreditMemosClient:
        """Operations for ``sales_credit_memos``."""

        return SalesCreditMemosClient(self._client)

    @property
    def sales_credit_memo_lines(self) -> SalesCreditMemoLinesClient:
        """Operations for ``sales_credit_memo_lines``."""

        return SalesCreditMemoLinesClient(self._client)

    @property
    def sales_invoices(self) -> SalesInvoicesClient:
        """Operations for ``sales_invoices``."""

        return SalesInvoicesClient(self._client)

    @property
    def sales_invoice_lines(self) -> SalesInvoiceLinesClient:
        """Operations for ``sales_invoice_lines``."""

        return SalesInvoiceLinesClient(self._client)

    @property
    def sales_orders(self) -> SalesOrdersClient:
        """Operations for ``sales_orders``."""

        return SalesOrdersClient(self._client)

    @property
    def sales_order_lines(self) -> SalesOrderLinesClient:
        """Operations for ``sales_order_lines``."""

        return SalesOrderLinesClient(self._client)

    @property
    def sales_quotes(self) -> SalesQuotesClient:
        """Operations for ``sales_quotes``."""

        return SalesQuotesClient(self._client)

    @property
    def sales_quote_lines(self) -> SalesQuoteLinesClient:
        """Operations for ``sales_quote_lines``."""

        return SalesQuoteLinesClient(self._client)

    @property
    def sales_shipments(self) -> SalesShipmentsClient:
        """Operations for ``sales_shipments``."""

        return SalesShipmentsClient(self._client)

    @property
    def sales_shipment_lines(self) -> SalesShipmentLinesClient:
        """Operations for ``sales_shipment_lines``."""

        return SalesShipmentLinesClient(self._client)

    @property
    def salespeople_purchasers(self) -> SalespeoplePurchasersClient:
        """Operations for ``salespeople_purchasers``."""

        return SalespeoplePurchasersClient(self._client)

    @property
    def shipment_methods(self) -> ShipmentMethodsClient:
        """Operations for ``shipment_methods``."""

        return ShipmentMethodsClient(self._client)

    @property
    def subscriptions(self) -> SubscriptionsClient:
        """Operations for ``subscriptions``."""

        return SubscriptionsClient(self._client)

    @property
    def tax_areas(self) -> TaxAreasClient:
        """Operations for ``tax_areas``."""

        return TaxAreasClient(self._client)

    @property
    def tax_groups(self) -> TaxGroupsClient:
        """Operations for ``tax_groups``."""

        return TaxGroupsClient(self._client)

    @property
    def time_registration_entries(self) -> TimeRegistrationEntriesClient:
        """Operations for ``time_registration_entries``."""

        return TimeRegistrationEntriesClient(self._client)

    @property
    def trial_balances(self) -> TrialBalancesClient:
        """Operations for ``trial_balances``."""

        return TrialBalancesClient(self._client)

    @property
    def units_of_measures(self) -> UnitsOfMeasuresClient:
        """Operations for ``units_of_measures``."""

        return UnitsOfMeasuresClient(self._client)

    @property
    def vendors(self) -> VendorsClient:
        """Operations for ``vendors``."""

        return VendorsClient(self._client)

    @property
    def vendor_payments(self) -> VendorPaymentsClient:
        """Operations for ``vendor_payments``."""

        return VendorPaymentsClient(self._client)

    @property
    def vendor_payment_journals(self) -> VendorPaymentJournalsClient:
        """Operations for ``vendor_payment_journals``."""

        return VendorPaymentJournalsClient(self._client)

    @property
    def vendor_purchases(self) -> VendorPurchasesClient:
        """Operations for ``vendor_purchases``."""

        return VendorPurchasesClient(self._client)


class AccountsClient(_EntityClient):
    """Generated operations for ``accounts``."""

    def get(
        self,
        company_id: str,
        account_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Account:
        """Get accounts

        Gets an account object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_account_get
        Operation id: dynamics_account_get
        Response model: Account

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/accounts({id})

        Example response:
        {
            "id": "a2a5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "10100",
            "displayName": "Bank Account - Operating",
            "category": "Assets",
            "subCategory": "Current Assets",
            "blocked": false,
            "accountType": "Posting",
            "directPosting": true,
            "incomeBalance": "Balance Sheet",
            "debitCreditBalance": "Debit",
            "netChange": 125476.82,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/accounts('
            + _path_value(account_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Account.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Account]:
        """List accounts

        List accounts objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_account_get
        Operation id: dynamics_account_list
        Response model: list[Account]
        """

        path = '/companies(' + _path_value(company_id) + ')/accounts'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Account.model_validate(item) for item in items]

class AccountingPeriodsClient(_EntityClient):
    """Generated operations for ``accounting_periods``."""

    def get(
        self,
        company_id: str,
        accounting_period_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.AccountingPeriod:
        """Get accountingPeriods

        Gets an accounting period object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_accountingperiod_get
        Operation id: dynamics_accountingperiod_get
        Response model: AccountingPeriod

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/accountingPeriods({id})

        Example response:
        {
            "id": "12345",
            "startingDate": "2025-01-01",
            "name": "Q1 2025",
            "newFiscalYear": false,
            "closed": false,
            "dateLocked": "2025-03-31",
            "lastModifiedDateTime": "2025-04-01T12:00:00Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/accountingPeriods('
            + _path_value(accounting_period_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.AccountingPeriod.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.AccountingPeriod]:
        """List accountingPeriods

        List accountingPeriods objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_accountingperiod_get
        Operation id: dynamics_accountingperiod_list
        Response model: list[AccountingPeriod]
        """

        path = '/companies(' + _path_value(company_id) + ')/accountingPeriods'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.AccountingPeriod.model_validate(item) for item in items]

class AgedAccountsPayablesClient(_EntityClient):
    """Generated operations for ``aged_accounts_payables``."""

    def get(
        self,
        company_id: str,
        vendor_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.AgedAccountsPayable:
        """Get agedAccountsPayable

        Gets an aged accounts payable object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_agedaccountspayable_get
        Operation id: dynamics_agedaccountspayable_get
        Response model: AgedAccountsPayable

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/agedAccountsPayables({ve...

        Example response:
        {
            "vendorId": "f7a5738a-44e3-ea11-bb43-000d3a2feca1",
            "vendorNumber": "10000",
            "name": "Fabrikam, Inc.",
            "currencyCode": "",
            "balanceDue": 2071.13,
            "currentAmount": 0,
            "period1Amount": 0,
            "period2Amount": 0,
            "period3Amount": 2071.13,
            "agedAsOfDate": "2020-08-21",
            "periodLengthFilter": "30D"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/agedAccountsPayables('
            + _path_value(vendor_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.AgedAccountsPayable.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.AgedAccountsPayable]:
        """List agedAccountsPayables

        List agedAccountsPayables objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_agedaccountspayable_get
        Operation id: dynamics_agedaccountspayable_list
        Response model: list[AgedAccountsPayable]
        """

        path = '/companies(' + _path_value(company_id) + ')/agedAccountsPayables'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.AgedAccountsPayable.model_validate(item) for item in items]

class AgedAccountsReceivablesClient(_EntityClient):
    """Generated operations for ``aged_accounts_receivables``."""

    def get(
        self,
        company_id: str,
        customer_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.AgedAccountsReceivable:
        """Get agedAccountsReceivable

        Gets an aged accounts receivable object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_agedaccountsreceivable_get
        Operation id: dynamics_agedaccountsreceivable_get
        Response model: AgedAccountsReceivable

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/agedAccountsReceivables(...

        Example response:
        {
            "customerId": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
            "customerNumber": "10000",
            "name": "Adatum Corporation",
            "currencyCode": "",
            "balanceDue": 0,
            "currentAmount": 0,
            "period1Amount": 0,
            "period2Amount": 0,
            "period3Amount": 0,
            "agedAsOfDate": "2020-08-21",
            "periodLengthFilter": "30D"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/agedAccountsReceivables('
            + _path_value(customer_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.AgedAccountsReceivable.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.AgedAccountsReceivable]:
        """List agedAccountsReceivables

        List agedAccountsReceivables objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_agedaccountsreceivable_get
        Operation id: dynamics_agedaccountsreceivable_list
        Response model: list[AgedAccountsReceivable]
        """

        path = '/companies(' + _path_value(company_id) + ')/agedAccountsReceivables'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.AgedAccountsReceivable.model_validate(item) for item in items]

class ApplyVendorEntriesClient(_EntityClient):
    """Generated operations for ``apply_vendor_entries``."""

    def get(
        self,
        company_id: str,
        vendor_payment_journal_id: str,
        vendor_payment_id: str,
        apply_vendor_entry_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ApplyVendorEntry:
        """Get applyVendorEntries

        Gets an apply vendor entry object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_applyvendorentry_get
        Operation id: dynamics_applyvendorentry_get
        Response model: ApplyVendorEntry

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/applyVendorEntries({id})

        Example response:
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "applied" : true,
            "appliesToId" : "1e8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "postingDate" : "2020-10-05",
            "documentType" : "Invoice",
            "documentNumber" : "2001",
            "externalDocumentNumber" : "2001",
            "vendorNumber" : "10000",
            "vendorName" : "First Up Consultants",
            "description" : "",
            "remainingAmount" : 0
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPaymentJournals('
            + _path_value(vendor_payment_journal_id)
            + ')/vendorPayments('
            + _path_value(vendor_payment_id)
            + ')/applyVendorEntries('
            + _path_value(apply_vendor_entry_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.ApplyVendorEntry.model_validate(data)

    def list(
        self,
        company_id: str,
        vendor_payment_journal_id: str,
        vendor_payment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.ApplyVendorEntry]:
        """List applyVendorEntries

        List applyVendorEntries objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_applyvendorentry_get
        Operation id: dynamics_applyvendorentry_list
        Response model: list[ApplyVendorEntry]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPaymentJournals('
            + _path_value(vendor_payment_journal_id)
            + ')/vendorPayments('
            + _path_value(vendor_payment_id)
            + ')/applyVendorEntries'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.ApplyVendorEntry.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        vendor_payment_journal_id: str,
        vendor_payment_id: str,
        apply_vendor_entry_id: str,
        body: _models.ApplyVendorEntryUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.ApplyVendorEntry:
        """Update applyVendorEntries

        Updates an  apply vendor entry object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_applyvendorentry_update
        Operation id: dynamics_applyvendorentry_update
        Request model: ApplyVendorEntryUpdate
        Response model: ApplyVendorEntry

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/applyVendorEntries({id})
        Content-type: application/json
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "applied" : true
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "applied" : true,
            "appliesToId" : "1e8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "postingDate" : "2020-10-05",
            "documentType" : "Invoice",
            "documentNumber" : "2001",
            "externalDocumentNumber" : "2001",
            "vendorNumber" : "10000",
            "vendorName" : "First Up Consultants",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPaymentJournals('
            + _path_value(vendor_payment_journal_id)
            + ')/vendorPayments('
            + _path_value(vendor_payment_id)
            + ')/applyVendorEntries('
            + _path_value(apply_vendor_entry_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.ApplyVendorEntry.model_validate(data)

class AttachmentsClient(_EntityClient):
    """Generated operations for ``attachments``."""

    def create(
        self,
        company_id: str,
        body: _models.AttachmentCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Attachment:
        """Create attachments

        Creates an attachment object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_attachment_create
        Operation id: dynamics_attachment_create
        Request model: AttachmentCreate
        Response model: Attachment

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/attachments({id})

        Content-type: application/json
        ```json
        {
            "parentId" : "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "fileName": "myPDF.pdf",
            "parentType": "Journal"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "b282a6f1-bfe3-ea11-aa60-000d3ad7cacb",
            "parentId": "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "fileName": "myPDF.pdf",
            "byteSize": 0,
            "lastModifiedDateTime": "2020-08-21T15:06:53Z",
            "parentType": "Journal"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/attachments'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Attachment.model_validate(data)

    def delete(
        self,
        company_id: str,
        attachment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete attachments

        Deletes attachments in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_attachment_delete
        Operation id: dynamics_attachment_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({companyId})/attachments({p...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/attachments('
            + _path_value(attachment_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        journal_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Attachment:
        """Get attachments

        Gets an attachments object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_attachment_get
        Operation id: dynamics_attachment_get
        Response model: Attachment

        Example request:
        GET https://{businesscentralPrefix}/api/v1.0/companies({id})/attachments?$filter=pare...

        Example response:
        {
            "id": "b282a6f1-bfe3-ea11-aa60-000d3ad7cacb",
            "parentId": "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "fileName": "myPDF.pdf",
            "byteSize": 0,
            "lastModifiedDateTime": "2020-08-21T15:06:53Z",
            "parentType": "Journal"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/attachments?$filter=parentId eq '
            + _path_value(journal_line_id)
            + " and parentType eq 'Journal'"
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Attachment.model_validate(data)

class AttachmentContentsClient(_EntityClient):
    """Generated operations for ``attachment_contents``."""

    def update(
        self,
        company_id: str,
        attachment_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.AttachmentContent:
        """Update attachments

        Uploads the attachment in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_attachment_update
        Operation id: dynamics_attachment_update
        Response model: AttachmentContent

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({companyId})/attachments(par...

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "67890",
            "parentId": "12345",
            "fileName": "invoice.pdf",
            "byteSize": 2048,
            "attachmentContent": "VGhpcyBpcyBhIGRlbW8gY29udGVudCBmb3IgdGhlIGF0dGFjaG1lbnQu",
            "lastModifiedDateTime": "2025-04-29T10:00:00Z",
            "parentType": "Incoming Document"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/attachments('
            + _path_value(attachment_id)
            + ')/attachmentContent'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.AttachmentContent.model_validate(data)

class BalanceSheetsClient(_EntityClient):
    """Generated operations for ``balance_sheets``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.BalanceSheet:
        """Get balanceSheet

        Gets a balance sheet object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_balancesheet_get
        Operation id: dynamics_balancesheet_get
        Response model: BalanceSheet

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/balanceSheet?$orderby=li...

        Example response:
        {
            "id": "a0fbf171-44e3-ea11-bb43-000d3a2feca1",
            "lineNumber": 10000,
            "display": "Assets",
            "balance": 0,
            "lineType": "header",
            "indentation": 0,
            "dateFilter": "2020-08-21"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/balanceSheets'
        data = self._client.get(path, query=query, params=params)
        return _models.BalanceSheet.model_validate(data)

class BankAccountsClient(_EntityClient):
    """Generated operations for ``bank_accounts``."""

    def create(
        self,
        company_id: str,
        body: _models.BankAccountCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.BankAccount:
        """Create bankAccounts

        Creates a bankAccount object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_bankaccount_create
        Operation id: dynamics_bankaccount_create
        Request model: BankAccountCreate
        Response model: BankAccount

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/bankAccounts
        Content-type: application/json

        {
            "number": "NBL",
            "displayName": "New Bank of London"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "26049aad-bde4-ea11-bbf2-00155df3a615",
            "number": "NBL",
            "displayName": "New Bank of London"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/bankAccounts'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.BankAccount.model_validate(data)

    def delete(
        self,
        company_id: str,
        bank_account_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete bankAccounts

        Deletes bankAccount  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_bankaccount_delete
        Operation id: dynamics_bankaccount_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/bankAccounts({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/bankAccounts('
            + _path_value(bank_account_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        bank_account_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.BankAccount:
        """Get bankAccounts

        Gets a bankAccount object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_bankaccount_get
        Operation id: dynamics_bankaccount_get
        Response model: BankAccount

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/bankAccounts({id})

        Example response:
        {
            "id": "26049aad-bde4-ea11-bbf2-00155df3a615",
            "number": "NBL",
            "displayName": "New Bank of London"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/bankAccounts('
            + _path_value(bank_account_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.BankAccount.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.BankAccount]:
        """List bankAccounts

        List bankAccounts objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_bankaccount_get
        Operation id: dynamics_bankaccount_list
        Response model: list[BankAccount]
        """

        path = '/companies(' + _path_value(company_id) + ')/bankAccounts'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.BankAccount.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        bank_account_id: str,
        body: _models.BankAccountUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.BankAccount:
        """Update bankAccounts

        Updates a bankAccount object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_bankaccount_update
        Operation id: dynamics_bankaccount_update
        Request model: BankAccountUpdate
        Response model: BankAccount

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/bankAccounts({id})
        Content-type: application/json

        {
            "displayName": "New Bank of Paris"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "26049aad-bde4-ea11-bbf2-00155df3a615",
            "number": "NBL",
            "displayName": "New Bank of Paris"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/bankAccounts('
            + _path_value(bank_account_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.BankAccount.model_validate(data)

class CashFlowStatementsClient(_EntityClient):
    """Generated operations for ``cash_flow_statements``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CashFlowStatement:
        """Get cashFlowStatements

        Gets a cash flow statement object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_cashflowstatement_get
        Operation id: dynamics_cashflowstatement_get
        Response model: CashFlowStatement

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/cashFlowStatements?$orde...

        Example response:
        {
            "id": "e0fbf171-44e3-ea11-bb43-000d3a2feca1",
            "lineNumber": 10000,
            "display": "Operating Activities",
            "netChange": 0,
            "lineType": "header",
            "indentation": 0,
            "dateFilter": "2020-08-21"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/cashFlowStatements'
        data = self._client.get(path, query=query, params=params)
        return _models.CashFlowStatement.model_validate(data)

class CompaniesClient(_EntityClient):
    """Generated operations for ``companies``."""

    def get(
        self,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Company:
        """Get companies

        Gets a company object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_company_get
        Operation id: dynamics_company_get
        Response model: Company

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies

        Example response:
        {
            "id": "824820a2-508c-ed11-aada-000d3a298ab3",
            "systemVersion": "21.2.49946.51685",
            "timestamp": 50516,
            "name": "CRONUS US",
            "displayName": "CRONUS USA, Inc.",
            "businessProfileId": "",
            "systemCreatedAt": "2023-01-04T16:55:47.367Z",
            "systemCreatedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
            "systemModifiedAt": "2023-01-04T16:55:47.367Z",
            "systemModifiedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1"
        }
        """

        path = '/companies'
        data = self._client.get(path, query=query, params=params)
        return _models.Company.model_validate(data)

class CompanyInformationsClient(_EntityClient):
    """Generated operations for ``company_informations``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CompanyInformation:
        """Get companyInformation

        Gets a company information object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_companyinformation_get
        Operation id: dynamics_companyinformation_get
        Response model: CompanyInformation

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/companyInformation

        Example response:
        {
            "id": "86f5f171-44e3-ea11-bb43-000d3a2feca1",
            "displayName": "CRONUS USA, Inc.",
            "addressLine1": "7122 South Ashford Street",
            "addressLine2": "Westminster",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
            "postalCode": "31772",
            "phoneNumber": "+1 425 555 0100",
            "faxNumber": "+1 425 555 0101",
            "email": "",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/companyInformation'
        data = self._client.get(path, query=query, params=params)
        return _models.CompanyInformation.model_validate(data)

    def update(
        self,
        company_id: str,
        company_information_id: str,
        body: _models.CompanyInformationUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.CompanyInformation:
        """Update companyInformation

        Updates a company information object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_companyinformation_update
        Operation id: dynamics_companyinformation_update
        Request model: CompanyInformationUpdate
        Response model: CompanyInformation

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/companyInformation({id})
        Content-type: application/json

        {
          "displayName": "CRONUS USA, Inc.",
          "website": "www.cronuscorp.net"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "86f5f171-44e3-ea11-bb43-000d3a2feca1",
            "displayName": "CRONUS USA, Inc.",
            "addressLine1": "7122 South Ashford Street",
            "addressLine2": "Westminster",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
            "postalCode": "31772",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/companyInformation('
            + _path_value(company_information_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.CompanyInformation.model_validate(data)

class ContactsClient(_EntityClient):
    """Generated operations for ``contacts``."""

    def create(
        self,
        company_id: str,
        contact_id: str,
        body: _models.ContactCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Contact:
        """Create contacts

        Creates a contact object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_contact_create
        Operation id: dynamics_contact_create
        Request model: ContactCreate
        Response model: Contact

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/contacts({id})
        Content-type: application/json
        {
            "number" : "108001",
            "type" : "Company",
            "displayName": "CRONUS USA, Inc.",
            "companyNumber" : "17806",
            "companyName" : "CRONUS US",
            "addressLine1": "7122 South Ashford Street",
            "addressLine2": "Westminster",
            "city": "Atlanta",
            "state": "GA",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number" : "108001",
            "type" : "Company",
            "displayName": "CRONUS USA, Inc.",
            "companyNumber" : "17806",
            "companyName" : "CRONUS US",
            "addressLine1": "7122 South Ashford Street",
            "addressLine2": "Westminster",
            "city": "Atlanta",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/contacts('
            + _path_value(contact_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Contact.model_validate(data)

    def delete(
        self,
        company_id: str,
        contact_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete contacts

        Deletes a contact object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_contact_delete
        Operation id: dynamics_contact_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/contacts({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/contacts('
            + _path_value(contact_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        contact_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Contact:
        """Get contacts

        Gets a contact object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_contact_get
        Operation id: dynamics_contact_get
        Response model: Contact

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/contacts({id})

        Example response:
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number" : "108001",
            "type" : "Company",
            "displayName": "CRONUS USA, Inc.",
            "companyNumber" : "17806",
            "companyName" : "CRONUS US",
            "addressLine1": "7122 South Ashford Street",
            "addressLine2": "Westminster",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/contacts('
            + _path_value(contact_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Contact.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Contact]:
        """List contacts

        List contacts objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_contact_get
        Operation id: dynamics_contact_list
        Response model: list[Contact]
        """

        path = '/companies(' + _path_value(company_id) + ')/contacts'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Contact.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        contact_id: str,
        body: _models.ContactUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Contact:
        """Update contacts

        Updates a  contact object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_contact_update
        Operation id: dynamics_contact_update
        Request model: ContactUpdate
        Response model: Contact

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/contacts({id})
        Content-type: application/json
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number" : "108001"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id" : "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number" : "108001",
            "type" : "Company",
            "displayName": "CRONUS USA, Inc.",
            "companyNumber" : "17806",
            "companyName" : "CRONUS US",
            "addressLine1": "7122 South Ashford Street",
            "addressLine2": "Westminster",
            "city": "Atlanta",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/contacts('
            + _path_value(contact_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Contact.model_validate(data)

class ContactsInformationsClient(_EntityClient):
    """Generated operations for ``contacts_informations``."""

    def get(
        self,
        company_id: str,
        vendor_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ContactsInformation:
        """Get contactInformation

        Gets a contact information object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_contactinformation_get
        Operation id: dynamics_contactinformation_get
        Response model: ContactsInformation

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/customers({id})/contacts...

        Example response:
        {
            {
                "contactId": "8f253caa-82de-ed11-884e-6045bdac97e2",
                "contactNumber": "CT000001",
                "contactName": "Adatum Corporation",
                "contactType": "Company",
                "relatedId": "8e253caa-82de-ed11-884e-6045bdac97e2",
                "relatedType": "Customer"
            },
            {
                "contactId": "91253caa-82de-ed11-884e-6045bdac97e2",
                "contactNumber": "CT000002",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')/contactsInformation'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.ContactsInformation.model_validate(data)

class ContentsClient(_EntityClient):
    """Generated operations for ``contents``."""

    def pdf_document(
        self,
        company_id: str,
        invoice_id: str,
        pdf_document_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Content:
        """Get purchaseInvoice pdfDocument

        Gets a PDF document on a purchaseInvoice in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoice_pdfdocument
        Operation id: dynamics_purchaseinvoice_pdfdocument
        Response model: Content

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({invoic...

        Example response:
        {

            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0O0tQNUdjaUtZcU8rcUNCQTdXOUxIZVEwalA0clhjSmlXU1pqWj...
                    "id":"94913756-80e9-47bc-995a-048a655b8cdd",
                    "content@odata.mediaReadLink":"https:// api.businesscentral.dynamics.com/...
                }
            ]
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(invoice_id)
            + ')/pdfDocument('
            + _path_value(pdf_document_id)
            + ')/content'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Content.model_validate(data)

    def pdf_document_salescreditmemo_pdfdocument(
        self,
        company_id: str,
        credit_memo_id: str,
        pdf_document_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Content:
        """Get salesCreditMemo pdfDocument

        Gets a PDF document on a salesCreditMemo in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemo_pdfdocument
        Operation id: dynamics_salescreditmemo_pdfdocument
        Response model: Content

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({credit...

        Example response:
        {

            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0O0tQNUdjaUtZcU8rcUNCQTdXOUxIZVEwalA0clhjSmlXU1pqWj...
                    "id":"94913756-80e9-47bc-995a-048a655b8cdd",
                    "content@odata.mediaReadLink":"https:// api.businesscentral.dynamics.com/...
                }
            ]
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(credit_memo_id)
            + ')/pdfDocument('
            + _path_value(pdf_document_id)
            + ')/content'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Content.model_validate(data)

    def pdf_document_salesinvoice_pdfdocument(
        self,
        company_id: str,
        invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Content:
        """Get salesInvoice pdfDocument

        Gets a PDF document on a salesInvoice in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_pdfdocument
        Operation id: dynamics_salesinvoice_pdfdocument
        Response model: Content

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})/pdfD...

        Example response:
        {

            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0O0tQNUdjaUtZcU8rcUNCQTdXOUxIZVEwalA0clhjSmlXU1pqWj...
                    "id":"94913756-80e9-47bc-995a-048a655b8cdd",
                    "content@odata.mediaReadLink":"https:// api.businesscentral.dynamics.com/...
                }
            ]
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(invoice_id)
            + ')/pdfDocument('
            + _path_value(invoice_id)
            + ')/content'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Content.model_validate(data)

    def pdf_document_salesquote_pdfdocument(
        self,
        company_id: str,
        quote_id: str,
        invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Content:
        """Get salesQuote pdfDocument

        Gets a PDF document on a salesQuote in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_pdfdocument
        Operation id: dynamics_salesquote_pdfdocument
        Response model: Content

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({quoteId})/p...

        Example response:
        {

            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0O0tQNUdjaUtZcU8rcUNCQTdXOUxIZVEwalA0clhjSmlXU1pqWj...
                    "id":"94913756-80e9-47bc-995a-048a655b8cdd",
                    "content@odata.mediaReadLink":"https:// api.businesscentral.dynamics.com/...
                }
            ]
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(quote_id)
            + ')/pdfDocument('
            + _path_value(invoice_id)
            + ')/content'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Content.model_validate(data)

class CountriesRegionsClient(_EntityClient):
    """Generated operations for ``countries_regions``."""

    def create(
        self,
        company_id: str,
        body: _models.CountriesRegionCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CountriesRegion:
        """Create countriesRegions

        Creates a countryRegion object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_countryregion_create
        Operation id: dynamics_countryregion_create
        Request model: CountriesRegionCreate
        Response model: CountriesRegion

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/countriesRegions
        Content-type: application/json

        {
          "code": "AE",
          "displayName": "United Arab Emirates",
          "addressFormat": "City+ZIP Code"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "44a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "AE",
            "displayName": "United Arab Emirates",
            "addressFormat": "City+ZIP Code",
            "lastModifiedDateTime": "2020-08-21T00:24:13.54Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/countriesRegions'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.CountriesRegion.model_validate(data)

    def delete(
        self,
        company_id: str,
        countries_region_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete countriesRegions

        Deletes a countries/regions object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_countryregion_delete
        Operation id: dynamics_countryregion_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/countriesRegions({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/countriesRegions('
            + _path_value(countries_region_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        countries_region_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CountriesRegion:
        """Get countriesRegions

        Gets a countryRegion object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_countryregion_get
        Operation id: dynamics_countryregion_get
        Response model: CountriesRegion

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/countriesRegions({id})

        Example response:
        {
            "id": "44a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "AE",
            "displayName": "United Arab Emirates",
            "addressFormat": "City+ZIP Code",
            "lastModifiedDateTime": "2020-08-21T00:24:13.54Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/countriesRegions('
            + _path_value(countries_region_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.CountriesRegion.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.CountriesRegion]:
        """List countriesRegions

        List countriesRegions objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_countryregion_get
        Operation id: dynamics_countryregion_list
        Response model: list[CountriesRegion]
        """

        path = '/companies(' + _path_value(company_id) + ')/countriesRegions'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.CountriesRegion.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        countries_region_id: str,
        body: _models.CountriesRegionUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.CountriesRegion:
        """Update countriesRegions

        Updates a countryRegion object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_countryregion_update
        Operation id: dynamics_countryregion_update
        Request model: CountriesRegionUpdate
        Response model: CountriesRegion

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/countriesRegions({id})
        Content-type: application/json

        {
          "displayName": "United Arab Emirates"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "44a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "AE",
            "displayName": "United Arab Emirates",
            "addressFormat": "City+ZIP Code",
            "lastModifiedDateTime": "2020-08-21T00:24:13.54Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/countriesRegions('
            + _path_value(countries_region_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.CountriesRegion.model_validate(data)

class CurrenciesClient(_EntityClient):
    """Generated operations for ``currencies``."""

    def create(
        self,
        company_id: str,
        body: _models.CurrencyCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Currency:
        """Create currencies

        Creates a currency object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currency_create
        Operation id: dynamics_currency_create
        Request model: CurrencyCreate
        Response model: Currency

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/currencies
        Content-type: application/json

        {
            "id": "0ca5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CAD",
            "displayName": "Canadian dollar",
            "symbol": "$",
            "amountDecimalPlaces": "2:2",
            "amountRoundingPrecision": 0.01,
            "lastModifiedDateTime": "2020-08-21T00:24:12.793Z"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "0ca5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CAD",
            "displayName": "Canadian dollar",
            "symbol": "$",
            "amountDecimalPlaces": "2:2",
            "amountRoundingPrecision": 0.01,
            "lastModifiedDateTime": "2020-08-21T00:24:12.793Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/currencies'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Currency.model_validate(data)

    def delete(
        self,
        company_id: str,
        currency_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete currencies

        Deletes currency  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currency_delete
        Operation id: dynamics_currency_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/currencies({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/currencies('
            + _path_value(currency_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        currency_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Currency:
        """Get currencies

        Gets a currency object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currency_get
        Operation id: dynamics_currency_get
        Response model: Currency

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/currencies({id})

        Example response:
        {
            "id": "0ca5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CAD",
            "displayName": "Canadian dollar",
            "symbol": "$",
            "amountDecimalPlaces": "2:2",
            "amountRoundingPrecision": 0.01,
            "lastModifiedDateTime": "2020-08-21T00:24:12.793Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/currencies('
            + _path_value(currency_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Currency.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Currency]:
        """List currencies

        List currencies objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currency_get
        Operation id: dynamics_currency_list
        Response model: list[Currency]
        """

        path = '/companies(' + _path_value(company_id) + ')/currencies'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Currency.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        currency_id: str,
        body: _models.CurrencyUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Currency:
        """Update currencies

        Updates a currency object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currency_update
        Operation id: dynamics_currency_update
        Request model: CurrencyUpdate
        Response model: Currency

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/currencies({id})
        Content-type: application/json

        {
            "displayName": "Canadian dollar"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "0ca5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CAD",
            "displayName": "Canadian dollar",
            "symbol": "$",
            "amountDecimalPlaces": "2:2",
            "amountRoundingPrecision": 0.01,
            "lastModifiedDateTime": "2020-08-21T00:24:12.793Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/currencies('
            + _path_value(currency_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Currency.model_validate(data)

class CurrencyExchangeRatesClient(_EntityClient):
    """Generated operations for ``currency_exchange_rates``."""

    def get(
        self,
        company_id: str,
        currency_exchange_rate_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CurrencyExchangeRate:
        """Get currencyExchangeRates

        Gets a currency exchange rate object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currencyexchangerate_get
        Operation id: dynamics_currencyexchangerate_get
        Response model: CurrencyExchangeRate

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/currencyExchangeRates({id})

        Example response:
        {
            "id": "USD-230501",
            "currencyCode": "USD",
            "startingDate": "2023-05-01",
            "exchangeRateAmount": 1.08,
            "relationalCurrencyCode": "EUR",
            "relationalExchangeRateAmount": 0.93,
            "lastModifiedDateTime": "2023-05-01T10:15:32Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/currencyExchangeRates('
            + _path_value(currency_exchange_rate_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.CurrencyExchangeRate.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.CurrencyExchangeRate]:
        """List currencyExchangeRates

        List currencyExchangeRates objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_currencyexchangerate_get
        Operation id: dynamics_currencyexchangerate_list
        Response model: list[CurrencyExchangeRate]
        """

        path = '/companies(' + _path_value(company_id) + ')/currencyExchangeRates'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.CurrencyExchangeRate.model_validate(item) for item in items]

class CustomersClient(_EntityClient):
    """Generated operations for ``customers``."""

    def create(
        self,
        company_id: str,
        body: _models.CustomerCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Customer:
        """Create customers

        Creates a customer object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_create
        Operation id: dynamics_customer_create
        Request model: CustomerCreate
        Response model: Customer

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/customers
        Content-type: application/json

        {
            "displayName": "Adatum Corporation",
            "type": "Company",
            "addressLine1": "192 Market Square",
            "addressLine2": "",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
            "postalCode": "31772",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "number": "10000",
            "displayName": "Adatum Corporation",
            "type": "Company",
            "addressLine1": "192 Market Square",
            "addressLine2": "",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/customers'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Customer.model_validate(data)

    def delete(
        self,
        company_id: str,
        customer_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete customers

        Deletes a customers object from Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_delete
        Operation id: dynamics_customer_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/customers({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        customer_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Customer:
        """Get customers

        Gets a customer object with properties and relationships in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_get
        Operation id: dynamics_customer_get
        Response model: Customer
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Customer.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Customer]:
        """List customers

        List customers objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_get
        Operation id: dynamics_customer_list
        Response model: list[Customer]
        """

        path = '/companies(' + _path_value(company_id) + ')/customers'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Customer.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        customer_id: str,
        body: _models.CustomerUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Customer:
        """Update customers

        Updates a customer object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_update
        Operation id: dynamics_customer_update
        Request model: CustomerUpdate
        Response model: Customer

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/customers({id})
        Content-type: application/json

        {
          "displayName": "Coho Winery Inc.",
          "phoneNumber": "(555) 555-1234"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "10000",
            "displayName": "Coho Winery Inc.",
            "type": "Company",
            "addressLine1": "192 Market Square",
            "addressLine2": "",
            "city": "Atlanta",
            "state": "GA",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Customer.model_validate(data)

class CustomerContactsClient(_EntityClient):
    """Generated operations for ``customer_contacts``."""

    def delete(
        self,
        company_id: str,
        customer_contact_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete customerContacts

        Deletes a customer contact object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customercontact_delete
        Operation id: dynamics_customercontact_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/customerContacts({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerContacts('
            + _path_value(customer_contact_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        customer_contact_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerContact:
        """Get customerContacts

        Gets a customer contact object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customercontact_get
        Operation id: dynamics_customercontact_get
        Response model: CustomerContact

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/customerContacts({id})

        Example response:
        {
            "id": "CONT00123",
            "email": "john.smith@contoso.com",
            "firstName": "John",
            "lastName": "Smith",
            "professionalTitle": "Purchasing Manager",
            "customerId": "CUST1042",
            "customerName": "Contoso Ltd.",
            "primaryPhoneNumber": "+1 425-555-0174"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerContacts('
            + _path_value(customer_contact_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.CustomerContact.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.CustomerContact]:
        """List customerContacts

        List customerContacts objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customercontact_get
        Operation id: dynamics_customercontact_list
        Response model: list[CustomerContact]
        """

        path = '/companies(' + _path_value(company_id) + ')/customerContacts'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.CustomerContact.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        customer_contact_id: str,
        body: _models.CustomerContactUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.CustomerContact:
        """Update customerContacts

        Updates a  customer contact object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customercontact_update
        Operation id: dynamics_customercontact_update
        Request model: CustomerContactUpdate
        Response model: CustomerContact

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/customerContacts({id})
        Content-type: application/json
        {
            "id": "CONT00123",
            "email": "john.smith@contoso.com",
            "professionalTitle": "Senior Purchasing Manager"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "CONT00123",
            "email": "john.smith@contoso.com",
            "firstName": "John",
            "lastName": "Smith",
            "professionalTitle": "Senior Purchasing Manager",
            "customerId": "CUST1042",
            "customerName": "Contoso Ltd.",
            "primaryPhoneNumber": "+1 425-555-0174"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerContacts('
            + _path_value(customer_contact_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.CustomerContact.model_validate(data)

class CustomerFinancialDetailsClient(_EntityClient):
    """Generated operations for ``customer_financial_details``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerFinancialDetail:
        """Get customerFinancialDetails

        Gets a customerFinancialDetail object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerfinancialdetail_get
        Operation id: dynamics_customerfinancialdetail_get
        Response model: CustomerFinancialDetail

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/customerFinancialDetails

        Example response:
        {
            "id": "52f556f8-e0e4-ea11-9305-000d3a482952",
            "number": "GL00000000",
            "balance": 0,
            "totalSalesExcludingTax": 0,
            "overdueAmount": 0
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/customerFinancialDetails'
        data = self._client.get(path, query=query, params=params)
        return _models.CustomerFinancialDetail.model_validate(data)

class CustomerPaymentsClient(_EntityClient):
    """Generated operations for ``customer_payments``."""

    def create(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        customer_payment_id: str,
        body: _models.CustomerPaymentCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerPayment:
        """Create customerPayments

        Creates a customer payment object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerPayment_create
        Operation id: dynamics_customerPayment_create
        Request model: CustomerPaymentCreate
        Response model: CustomerPayment

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/customerPayment
        Content-type: application/json

        {
            "lineNumber": 10000,
            "customerId": "customerId-value",
            "customerNumber": "10400",
            "contactId": "string",
            "postingDate": "2015-12-31",
            "documentNumber": "1234",
            "externalDocumentNumber": "",
            "amount": 1500,
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "17cce948-c6a5-4861-8ff5-30428ed83207",
            "lineNumber": 10000,
            "customerId": "customerId-value",
            "customerNumber": "10400",
            "contactId": "string",
            "postingDate": "2015-12-31",
            "documentNumber": "1234",
            "externalDocumentNumber": "",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentJournals('
            + _path_value(customer_payment_journal_id)
            + ')/customerPayment('
            + _path_value(customer_payment_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.CustomerPayment.model_validate(data)

    def delete(
        self,
        company_id: str,
        customer_payments_journal_id: str,
        customer_payment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete customerPayments

        Deletes a customer payment object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpayment_delete
        Operation id: dynamics_customerpayment_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/customerPaymentsJourn...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentsJournals('
            + _path_value(customer_payments_journal_id)
            + ')/customerPayments('
            + _path_value(customer_payment_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        customer_payments_journal_id: str,
        customer_payment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerPayment:
        """Get customerPayments

        Gets a customer payment object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpayment_get
        Operation id: dynamics_customerpayment_get
        Response model: CustomerPayment

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/customerPaymentsJournals...

        Example response:
        {
            "id": "17cce948-c6a5-4861-8ff5-30428ed83207",
            "lineNumber": 10000,
            "customerId": "customerId-value",
            "customerNumber": "10400",
            "contactId": "string",
            "postingDate": "2015-12-31",
            "documentNumber": "1234",
            "externalDocumentNumber": "",
            "amount": 1500,
            "appliesToInvoiceId": "appliesToInvoiceId-value",
            "appliesToInvoiceNumber": "100000",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentsJournals('
            + _path_value(customer_payments_journal_id)
            + ')/customerPayments('
            + _path_value(customer_payment_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.CustomerPayment.model_validate(data)

    def list(
        self,
        company_id: str,
        customer_payments_journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.CustomerPayment]:
        """List customerPayments

        List customerPayments objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpayment_get
        Operation id: dynamics_customerpayment_list
        Response model: list[CustomerPayment]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentsJournals('
            + _path_value(customer_payments_journal_id)
            + ')/customerPayments'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.CustomerPayment.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        customer_payments_journal_id: str,
        customer_payment_id: str,
        body: _models.CustomerPaymentUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.CustomerPayment:
        """Update customerPayments

        Updates a customer payment object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpayment_update
        Operation id: dynamics_customerpayment_update
        Request model: CustomerPaymentUpdate
        Response model: CustomerPayment

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/customerPaymentsJourna...
        Content-type: application/json

        {
          "amount": 1500
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "17cce948-c6a5-4861-8ff5-30428ed83207",
            "lineNumber": 10000,
            "customerId": "customerId-value",
            "customerNumber": "10400",
            "contactId": "string",
            "postingDate": "2015-12-31",
            "documentNumber": "1234",
            "externalDocumentNumber": "",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentsJournals('
            + _path_value(customer_payments_journal_id)
            + ')/customerPayments('
            + _path_value(customer_payment_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.CustomerPayment.model_validate(data)

class CustomerPaymentJournalsClient(_EntityClient):
    """Generated operations for ``customer_payment_journals``."""

    def create(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        body: _models.CustomerPaymentJournalCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerPaymentJournal:
        """Create customerPaymentJournals

        Creates a customerPaymentJournal object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpaymentjournal_create
        Operation id: dynamics_customerpaymentjournal_create
        Request model: CustomerPaymentJournalCreate
        Response model: CustomerPaymentJournal

        Example request:
        POST https://{businesscentralPrefix}/api/v1.0/companies({id})/customerPaymentJournals
        Content-type: application/json

        {
            "code": "GENERAL",
            "displayName": "GENERAL",
            "balancingAccountId": "00000000-0000-0000-0000-000000000000"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "dc1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "GENERAL",
            "displayName": "GENERAL",
            "lastModifiedDateTime": "2020-08-21T00:24:35.687Z",
            "balancingAccountId": "00000000-0000-0000-0000-000000000000",
            "balancingAccountNumber": "10100"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentJournals('
            + _path_value(customer_payment_journal_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.CustomerPaymentJournal.model_validate(data)

    def delete(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete customerPaymentJournals

        Deletes customerPaymentJournal  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpaymentjournal_delete
        Operation id: dynamics_customerpaymentjournal_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/customerPaymentJourna...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentJournals('
            + _path_value(customer_payment_journal_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerPaymentJournal:
        """Get customerPaymentJournals

        Gets a customerPaymentJournal object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpaymentjournal_get
        Operation id: dynamics_customerpaymentjournal_get
        Response model: CustomerPaymentJournal

        Example request:
        GET https://{businesscentralPrefix}/api/v1.0/companies({id})/customerPaymentJournals(...

        Example response:
        {
            "id": "dc1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "GENERAL",
            "displayName": "GENERAL",
            "lastModifiedDateTime": "2020-08-21T00:24:35.687Z",
            "balancingAccountId": "00000000-0000-0000-0000-000000000000",
            "balancingAccountNumber": "10100"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentJournals('
            + _path_value(customer_payment_journal_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.CustomerPaymentJournal.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.CustomerPaymentJournal]:
        """List customerPaymentJournals

        List customerPaymentJournals objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpaymentjournal_get
        Operation id: dynamics_customerpaymentjournal_list
        Response model: list[CustomerPaymentJournal]
        """

        path = '/companies(' + _path_value(company_id) + ')/customerPaymentJournals'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.CustomerPaymentJournal.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        body: _models.CustomerPaymentJournalUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.CustomerPaymentJournal:
        """Update customerPaymentJournals

        Updates a customerPaymentJournal object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerpaymentjournal_update
        Operation id: dynamics_customerpaymentjournal_update
        Request model: CustomerPaymentJournalUpdate
        Response model: CustomerPaymentJournal

        Example request:
        PATCH https://{businesscentralPrefix}/api/v1.0/companies({id})/customerPaymentJournal...
        Content-type: application/json

        {
          "code": "GENERAL",
          "displayName": "GENERAL"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "dc1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "GENERAL",
            "displayName": "GENERAL",
            "lastModifiedDateTime": "2020-08-21T00:24:35.687Z",
            "balancingAccountId": "00000000-0000-0000-0000-000000000000",
            "balancingAccountNumber": "10100"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerPaymentJournals('
            + _path_value(customer_payment_journal_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.CustomerPaymentJournal.model_validate(data)

class CustomerReturnReasonsClient(_EntityClient):
    """Generated operations for ``customer_return_reasons``."""

    def create(
        self,
        company_id: str,
        body: _models.CustomerReturnReasonCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerReturnReason:
        """Create customerReturnReasons

        Creates a customer return reason object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerreturnreason_create
        Operation id: dynamics_customerreturnreason_create
        Request model: CustomerReturnReasonCreate
        Response model: CustomerReturnReason

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/customerReturnReasons
        Content-type: application/json
        {
          "code": "VARIANT",
          "description": "Incorrect item variant"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "6ea22bf6-a449-ee11-ad0b-a1422c0f7f1f",
            "code": "VARIANT",
            "description": "Incorrect item variant"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/customerReturnReasons'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.CustomerReturnReason.model_validate(data)

    def delete(
        self,
        company_id: str,
        customer_return_reason_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete customerReturnReasons

        Deletes a customer return reason object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerreturnreason_delete
        Operation id: dynamics_customerreturnreason_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/customerReturnReasons...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerReturnReasons('
            + _path_value(customer_return_reason_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        customer_return_reason_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerReturnReason:
        """Get customerReturnReasons

        Gets a customer return reason object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerreturnreason_get
        Operation id: dynamics_customerreturnreason_get
        Response model: CustomerReturnReason

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/customerReturnReasons({id})

        Example response:
        {
            "id": "6ea22bf6-a449-ee11-ad0b-a1422c0f7f1f",
            "code": "VARIANT",
            "description": "Wrong item variant"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerReturnReasons('
            + _path_value(customer_return_reason_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.CustomerReturnReason.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.CustomerReturnReason]:
        """List customerReturnReasons

        List customerReturnReasons objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerreturnreason_get
        Operation id: dynamics_customerreturnreason_list
        Response model: list[CustomerReturnReason]
        """

        path = '/companies(' + _path_value(company_id) + ')/customerReturnReasons'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.CustomerReturnReason.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        customer_return_reason_id: str,
        body: _models.CustomerReturnReasonUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.CustomerReturnReason:
        """Update customerReturnReasons

        Updates a  customer return reason object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customerreturnreason_update
        Operation id: dynamics_customerreturnreason_update
        Request model: CustomerReturnReasonUpdate
        Response model: CustomerReturnReason

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/customerReturnReasons(...
        Content-type: application/json
        {
          "description": "Wrong item variant"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "6ea22bf6-a449-ee11-ad0b-a1422c0f7f1f",
            "code": "VARIANT",
            "description": "Wrong item variant"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customerReturnReasons('
            + _path_value(customer_return_reason_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.CustomerReturnReason.model_validate(data)

class CustomerSalesClient(_EntityClient):
    """Generated operations for ``customer_sales``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.CustomerSale:
        """Get customerSales

        Gets a customerSale object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customersale_get
        Operation id: dynamics_customersale_get
        Response model: CustomerSale

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/customerSales

        Example response:
        {
          "customerId": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
          "customerNumber": "50000",
          "name": "Relecloud",
          "totalSalesAmount": 83956.45,
          "dateFilter_FilterOnly": null
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/customerSales'
        data = self._client.get(path, query=query, params=params)
        return _models.CustomerSale.model_validate(data)

class DefaultDimensionsClient(_EntityClient):
    """Generated operations for ``default_dimensions``."""

    def create(
        self,
        company_id: str,
        default_dimension_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Create defaultDimensions for entities

        Creates a default dimension of the item object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_defaultdimension_create
        Operation id: dynamics_defaultdimension_create
        Response model: DefaultDimension

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId})/...
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/vendors({vendorI...
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/employees({emplo...
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/customers({custo...

        Example response:
        {
            "parentId":"b3fbe87a-61b8-4a6c-85de-0555f1627a67",
            "dimensionId":"d5fc81ea-8687-4e9d-9c49-7fde28ccdb1a",
            "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
            "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/defaultDimensions('
            + _path_value(default_dimension_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions(
        self,
        company_id: str,
        customer_id: str,
        dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete customer defaultDimensions

        Deletes the default dimensions of the customer in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_delete_defaultdimensions
        Operation id: dynamics_customer_delete_defaultdimensions

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({companyId})/customers({cus...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')/defaultDimensions('
            + _path_value(customer_id)
            + ','
            + _path_value(dimension_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def default_dimensions_employee_delete_defaultdimensions(
        self,
        company_id: str,
        employee_id: str,
        dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete employee defaultDimensions

        Deletes the default dimensions of the employee in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_delete_defaultdimensions
        Operation id: dynamics_employee_delete_defaultdimensions

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({companyId})/employees({emp...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')/defaultDimensions('
            + _path_value(employee_id)
            + ','
            + _path_value(dimension_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def default_dimensions_vendor_delete_defaultdimensions(
        self,
        company_id: str,
        vendor_id: str,
        dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete vendor defaultDimensions

        Deletes the default dimensions of the vendor in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_delete_defaultdimensions
        Operation id: dynamics_vendor_delete_defaultdimensions

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({companyId})/vendors({vendo...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')/defaultDimensions('
            + _path_value(vendor_id)
            + ','
            + _path_value(dimension_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def default_dimensions_customer_get_defaultdimensions(
        self,
        company_id: str,
        customer_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Get customer defaultDimensions

        Gets a customer default dimensions in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_get_defaultdimensions
        Operation id: dynamics_customer_get_defaultdimensions
        Response model: DefaultDimension

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({companyId})/customers({custom...

        Example response:
        {
            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0OzNPaHFuS0ZQdk5oc3ZkSW9KdzVkdXk2LytjcmNqeHJJOU05Sj...
                    "parentId":"b3fbe87a-61b8-4a6c-85de-0555f1627a67","dimensionId":"d5fc81ea...
                    "dimensionCode":"DEPARTMENT",
                    "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
                    "dimensionValueCode":"PROD",
                    "postingValidation":"Same Code"
                }
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')/defaultDimensions'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_employee_get_defaultdimensions(
        self,
        company_id: str,
        employee_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Get employee defaultDimensions

        Gets an employee default dimensions in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_get_defaultdimensions
        Operation id: dynamics_employee_get_defaultdimensions
        Response model: DefaultDimension

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({companyId})/employees({employ...

        Example response:
        {
            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0OzNPaHFuS0ZQdk5oc3ZkSW9KdzVkdXk2LytjcmNqeHJJOU05Sj...
                    "parentId":"aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb","dimensionId":"bbbbbbbb...
                    "dimensionCode":"DEPARTMENT",
                    "dimensionValueId":"cccccccc-2222-3333-4444-dddddddddddd",
                    "dimensionValueCode":"PROD",
                    "postingValidation":"Same Code"
                }
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')/defaultDimensions'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_vendor_get_defaultdimensions(
        self,
        company_id: str,
        vendor_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Get vendor defaultDimensions

        Gets a vendor default dimensions in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_get_defaultdimensions
        Operation id: dynamics_vendor_get_defaultdimensions
        Response model: DefaultDimension

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({companyId})/vendors({vendorId...

        Example response:
        {
            "@odata.context":"https://api.businesscentral.dynamics.com/v2.0/api/v2.0/$metadat...
            "value":
            [
                {
                    "@odata.etag":"W/\\"JzQ0OzNPaHFuS0ZQdk5oc3ZkSW9KdzVkdXk2LytjcmNqeHJJOU05Sj...
                    "parentId":"b3fbe87a-61b8-4a6c-85de-0555f1627a67","dimensionId":"d5fc81ea...
                    "dimensionCode":"DEPARTMENT",
                    "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
                    "dimensionValueCode":"PROD",
                    "postingValidation":"Same Code"
                }
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')/defaultDimensions'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_customer_update_defaultdimensions(
        self,
        company_id: str,
        customer_id: str,
        dimension_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DefaultDimension:
        """Update customer defaultDimensions

        Updates the customer default dimensions in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_update_defaultdimensions
        Operation id: dynamics_customer_update_defaultdimensions
        Response model: DefaultDimension

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({companyId})/customers({cust...

        Example response:
        {
          "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
          "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')/defaultDimensions('
            + _path_value(customer_id)
            + ','
            + _path_value(dimension_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_employee_update_defaultdimensions(
        self,
        company_id: str,
        employee_id: str,
        dimension_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DefaultDimension:
        """Update employee defaultDimensions

        Updates an employee default dimensions in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_update_defaultdimensions
        Operation id: dynamics_employee_update_defaultdimensions
        Response model: DefaultDimension

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({companyId})/employees({empl...

        Example response:
        {
          "dimensionValueId":"cccccccc-2222-3333-4444-dddddddddddd",
          "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')/defaultDimensions('
            + _path_value(employee_id)
            + ','
            + _path_value(dimension_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_vendor_update_defaultdimensions(
        self,
        company_id: str,
        vendor_id: str,
        dimension_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DefaultDimension:
        """Update vendor defaultDimensions

        Updates the vendor default dimensions in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_update_defaultdimensions
        Operation id: dynamics_vendor_update_defaultdimensions
        Response model: DefaultDimension

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({companyId})/vendors({vendor...

        Example response:
        {
          "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
          "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')/defaultDimensions('
            + _path_value(vendor_id)
            + ','
            + _path_value(dimension_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_customer_create_defaultdimensions(
        self,
        company_id: str,
        customer_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Create customer defaultDimensions

        Creates a default dimensions of the customer object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_customer_create_defaultdimensions
        Operation id: dynamics_customer_create_defaultdimensions
        Response model: DefaultDimension

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/customers({custo...

        Example response:
        {
            "parentId":"b3fbe87a-61b8-4a6c-85de-0555f1627a67",
            "dimensionId":"d5fc81ea-8687-4e9d-9c49-7fde28ccdb1a",
            "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
            "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/customers('
            + _path_value(customer_id)
            + ')/defaultDimensions'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_employee_create_defaultdimensions(
        self,
        company_id: str,
        employee_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Create employee defaultDimensions

        Creates a default dimensions of the employee object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_create_defaultdimensions
        Operation id: dynamics_employee_create_defaultdimensions
        Response model: DefaultDimension

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/employees({emplo...

        Example response:
        {
            "parentId":"b3fbe87a-61b8-4a6c-85de-0555f1627a67",
            "dimensionId":"d5fc81ea-8687-4e9d-9c49-7fde28ccdb1a",
            "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
            "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')/defaultDimensions'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DefaultDimension.model_validate(data)

    def default_dimensions_vendor_create_defaultdimensions(
        self,
        company_id: str,
        vendor_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Create vendor defaultDimensions

        Creates a default dimensions of the vendor object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_create_defaultdimensions
        Operation id: dynamics_vendor_create_defaultdimensions
        Response model: DefaultDimension

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/vendors({vendorI...

        Example response:
        {
            "parentId":"b3fbe87a-61b8-4a6c-85de-0555f1627a67",
            "dimensionId":"d5fc81ea-8687-4e9d-9c49-7fde28ccdb1a",
            "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
            "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')/defaultDimensions'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DefaultDimension.model_validate(data)

    def delete(
        self,
        company_id: str,
        default_dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete defaultDimensions from entities

        Deletes the default dimension of the item in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_defaultdimension_delete
        Operation id: dynamics_defaultdimension_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId}...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/defaultDimensions('
            + _path_value(default_dimension_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        default_dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DefaultDimension:
        """Get entity defaultDimensions

        Gets an item default dimension in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_defaultdimension_get
        Operation id: dynamics_defaultdimension_get
        Response model: DefaultDimension

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId})/d...

        Example response:
        {
            "id": "5b049aad-bde4-ea11-bbf2-00155df3a615",
            "parentId": "53049aad-bde4-ea11-bbf2-00155df3a615",
            "dimensionId": "47c99ea7-bde4-ea11-bbf2-00155df3a615",
            "dimensionCode": "DEPARTMENT",
            "dimensionValueId": "49c99ea7-bde4-ea11-bbf2-00155df3a615",
            "dimensionValueCode": "SALES",
            "postingValidation": " "
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/defaultDimensions('
            + _path_value(default_dimension_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DefaultDimension.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.DefaultDimension]:
        """List defaultDimensions

        List defaultDimensions objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_defaultdimension_get
        Operation id: dynamics_defaultdimension_list
        Response model: list[DefaultDimension]
        """

        path = '/companies(' + _path_value(company_id) + ')/defaultDimensions'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.DefaultDimension.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        default_dimension_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DefaultDimension:
        """Update defaultDimensions for entities

        Updates the item default dimensions in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_defaultdimension_update
        Operation id: dynamics_defaultdimension_update
        Response model: DefaultDimension

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId})...

        Example response:
        {
          "dimensionValueId":"1045a902-070a-4d31-b2b1-b9431e9e5b26",
          "postingValidation":"Same Code"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/defaultDimensions('
            + _path_value(default_dimension_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DefaultDimension.model_validate(data)

class DimensionsClient(_EntityClient):
    """Generated operations for ``dimensions``."""

    def get(
        self,
        company_id: str,
        dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Dimension:
        """Get dimensions

        Gets a dimension object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimension_get
        Operation id: dynamics_dimension_get
        Response model: Dimension

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/dimensions({id})

        Example response:
        {
            "id": "a8196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "CUSTOMERGROUP",
            "displayName": "Customer Group",
            "lastModifiedDateTime": "2020-08-21T00:24:26.09Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/dimensions('
            + _path_value(dimension_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Dimension.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Dimension]:
        """List dimensions

        List dimensions objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimension_get
        Operation id: dynamics_dimension_list
        Response model: list[Dimension]
        """

        path = '/companies(' + _path_value(company_id) + ')/dimensions'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Dimension.model_validate(item) for item in items]

class DimensionSetLinesClient(_EntityClient):
    """Generated operations for ``dimension_set_lines``."""

    def create(
        self,
        company_id: str,
        sales_order_id: str,
        dimension_set_line_id: str,
        body: _models.DimensionSetLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DimensionSetLine:
        """Create dimensionSetLines

        Creates a dimensionSetLine object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionsetline_create
        Operation id: dynamics_dimensionsetline_create
        Request model: DimensionSetLineCreate
        Response model: DimensionSetLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/dimen...
        Content-type: application/json

        {
            "id": "55c99ea7-bde4-ea11-bbf2-00155df3a615",
            "code": "BUSINESSGROUP",
            "parentId": "85d8a1c5-bde4-ea11-bbf2-00155df3a615",
            "parentType": "Sales Order",
            "displayName": "Business Group",
            "valueId": "56c99ea7-bde4-ea11-bbf2-00155df3a615",
            "valueCode": "HOME",
            "valueDisplayName": "Home"
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "55c99ea7-bde4-ea11-bbf2-00155df3a615",
            "code": "BUSINESSGROUP",
            "parentId": "85d8a1c5-bde4-ea11-bbf2-00155df3a615",
            "parentType": "Sales Order",
            "displayName": "Business Group",
            "valueId": "56c99ea7-bde4-ea11-bbf2-00155df3a615",
            "valueCode": "HOME",
            "valueDisplayName": "Home"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/dimensionSetLines('
            + _path_value(dimension_set_line_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DimensionSetLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_order_id: str,
        dimension_set_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete dimensionSetLines

        Deletes dimensionSetLine  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionsetline_delete
        Operation id: dynamics_dimensionsetline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/dim...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/dimensionSetLines('
            + _path_value(dimension_set_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_order_id: str,
        dimension_set_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DimensionSetLine:
        """Get dimensionSetLines

        Gets a dimensionSetLine object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionsetline_get
        Operation id: dynamics_dimensionsetline_get
        Response model: DimensionSetLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/dimens...

        Example response:
        {
            "id": "55c99ea7-bde4-ea11-bbf2-00155df3a615",
            "code": "BUSINESSGROUP",
            "parentId": "85d8a1c5-bde4-ea11-bbf2-00155df3a615",
            "parentType": "Sales Order",
            "displayName": "Business Group",
            "valueId": "56c99ea7-bde4-ea11-bbf2-00155df3a615",
            "valueCode": "HOME",
            "valueDisplayName": "Home"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/dimensionSetLines('
            + _path_value(dimension_set_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DimensionSetLine.model_validate(data)

    def list(
        self,
        company_id: str,
        sales_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.DimensionSetLine]:
        """List dimensionSetLines

        List dimensionSetLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionsetline_get
        Operation id: dynamics_dimensionsetline_list
        Response model: list[DimensionSetLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/dimensionSetLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.DimensionSetLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_order_id: str,
        dimension_set_line_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DimensionSetLine:
        """Update dimensionSetLines

        Updates a dimensionSetLine object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionsetline_update
        Operation id: dynamics_dimensionsetline_update
        Response model: DimensionSetLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/dime...
        Content-type: application/json

        {
            "code": "SALESGROUP",
            "displayName": "Sales Group",
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "55c99ea7-bde4-ea11-bbf2-00155df3a615",
            "code": "SALESGROUP",
            "parentId": "85d8a1c5-bde4-ea11-bbf2-00155df3a615",
            "parentType": "Sales Order",
            "displayName": "Sales Group",
            "valueId": "56c99ea7-bde4-ea11-bbf2-00155df3a615",
            "valueCode": "HOME",
            "valueDisplayName": "Home"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/dimensionSetLines('
            + _path_value(dimension_set_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DimensionSetLine.model_validate(data)

class DimensionValuesClient(_EntityClient):
    """Generated operations for ``dimension_values``."""

    def get(
        self,
        company_id: str,
        dimension_id: str,
        dimension_value_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DimensionValue:
        """Get dimensionValues

        Gets a dimension value object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionvalue_get
        Operation id: dynamics_dimensionvalue_get
        Response model: DimensionValue

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/dimensions({id})/dimensi...

        Example response:
        {
            "id": "50c99ea7-bde4-ea11-bbf2-00155df3a615",
            "code": "PRIVATE",
            "dimensionId": "4fc99ea7-bde4-ea11-bbf2-00155df3a615",
            "displayName": "Private",
            "lastModifiedDateTime": "2020-08-22T21:23:11.437Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/dimensions('
            + _path_value(dimension_id)
            + ')/dimensionValues('
            + _path_value(dimension_value_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DimensionValue.model_validate(data)

    def list(
        self,
        company_id: str,
        dimension_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.DimensionValue]:
        """List dimensionValues

        List dimensionValues objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_dimensionvalue_get
        Operation id: dynamics_dimensionvalue_list
        Response model: list[DimensionValue]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/dimensions('
            + _path_value(dimension_id)
            + ')/dimensionValues'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.DimensionValue.model_validate(item) for item in items]

class DisputeStatusClient(_EntityClient):
    """Generated operations for ``dispute_status``."""

    def create(
        self,
        company_id: str,
        dispute_status_id: str,
        body: _models.DisputeStatusCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DisputeStatus:
        """Create disputeStatus

        Creates a dispute status object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_disputestatus_create
        Operation id: dynamics_disputestatus_create
        Request model: DisputeStatusCreate
        Response model: DisputeStatus

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/disputeStatus({id})
        Content-type: application/json
        {
            "code": "INVEST",
            "displayName": "Under Investigation"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "INVEST",
            "code": "INVEST",
            "displayName": "Under Investigation",
            "lastModifiedDateTime": "2025-04-29T14:32:09Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/disputeStatus('
            + _path_value(dispute_status_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DisputeStatus.model_validate(data)

    def delete(
        self,
        company_id: str,
        dispute_status_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete disputeStatus

        Deletes a dispute status object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_disputestatus_delete
        Operation id: dynamics_disputestatus_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/disputeStatus({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/disputeStatus('
            + _path_value(dispute_status_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        dispute_status_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DisputeStatus:
        """Get disputeStatus

        Gets a dispute status object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_disputestatus_get
        Operation id: dynamics_disputestatus_get
        Response model: DisputeStatus

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/disputeStatus({id})

        Example response:
        {
            "id": "REVIEW",
            "code": "REVIEW",
            "displayName": "Under Review",
            "lastModifiedDateTime": "2025-04-12T09:45:23Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/disputeStatus('
            + _path_value(dispute_status_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DisputeStatus.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.DisputeStatus]:
        """List disputeStatus

        List disputeStatus objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_disputestatus_get
        Operation id: dynamics_disputestatus_list
        Response model: list[DisputeStatus]
        """

        path = '/companies(' + _path_value(company_id) + ')/disputeStatus'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.DisputeStatus.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        dispute_status_id: str,
        body: _models.DisputeStatusUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DisputeStatus:
        """Update disputeStatus

        Updates a  dispute status object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_disputestatus_update
        Operation id: dynamics_disputestatus_update
        Request model: DisputeStatusUpdate
        Response model: DisputeStatus

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/disputeStatus({id})
        Content-type: application/json
        {
            "displayName": "Pending Resolution"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "PEND",
            "code": "PEND",
            "displayName": "Pending Resolution",
            "lastModifiedDateTime": "2025-04-29T16:42:18Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/disputeStatus('
            + _path_value(dispute_status_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DisputeStatus.model_validate(data)

class DocumentAttachmentsClient(_EntityClient):
    """Generated operations for ``document_attachments``."""

    def create(
        self,
        company_id: str,
        document_attachment_id: str,
        body: _models.DocumentAttachmentCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DocumentAttachment:
        """Create documentAttachments

        Creates a document attachment object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_documentattachment_create
        Operation id: dynamics_documentattachment_create
        Request model: DocumentAttachmentCreate
        Response model: DocumentAttachment

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/documentAttachments({id})
        Content-type: application/json
        {
            "fileName": "Invoice_10542.pdf",
            "byteSize": 245823,
            "attachmentContent": "JVBERi0xLjUKJeTl5OTlCjEgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1B...
            "parentType": "Purchase Invoice",
            "parentId": "INV-10542",
            "documentFlowPurchase": true
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "ATT00089",
            "fileName": "Invoice_10542.pdf",
            "byteSize": 245823,
            "attachmentContent": "JVBERi0xLjUKJeTl5OTlCjEgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1B...
            "parentType": "Purchase Invoice",
            "parentId": "INV-10542",
            "lineNumber": 0,
            "documentFlowSales": false,
            "documentFlowPurchase": true,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/documentAttachments('
            + _path_value(document_attachment_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.DocumentAttachment.model_validate(data)

    def delete(
        self,
        company_id: str,
        document_attachment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete documentAttachments

        Deletes a document attachment object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_documentattachment_delete
        Operation id: dynamics_documentattachment_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/documentAttachments({...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/documentAttachments('
            + _path_value(document_attachment_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        document_attachment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.DocumentAttachment:
        """Get documentAttachments

        Gets a document attachment object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_documentattachment_get
        Operation id: dynamics_documentattachment_get
        Response model: DocumentAttachment

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/documentAttachments({id})

        Example response:
        {
            "id": "ATT00089",
            "fileName": "Invoice_10542.pdf",
            "byteSize": 245823,
            "attachmentContent": "JVBERi0xLjUKJeTl5OTlCjEgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1B...
            "parentType": "Purchase Invoice",
            "parentId": "INV-10542",
            "lineNumber": 0,
            "documentFlowSales": false,
            "documentFlowPurchase": true,
            "lastModifiedDateTime": "2025-04-28T09:15:42Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/documentAttachments('
            + _path_value(document_attachment_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.DocumentAttachment.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.DocumentAttachment]:
        """List documentAttachments

        List documentAttachments objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_documentattachment_get
        Operation id: dynamics_documentattachment_list
        Response model: list[DocumentAttachment]
        """

        path = '/companies(' + _path_value(company_id) + ')/documentAttachments'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.DocumentAttachment.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        document_attachment_id: str,
        body: _models.DocumentAttachmentUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.DocumentAttachment:
        """Update documentAttachments

        Updates a  document attachment object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_documentattachment_update
        Operation id: dynamics_documentattachment_update
        Request model: DocumentAttachmentUpdate
        Response model: DocumentAttachment

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/documentAttachments({id})
        Content-type: application/json
        {
            "fileName": "Updated_Invoice_10542.pdf",
            "documentFlowSales": true
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "ATT00089",
            "fileName": "Updated_Invoice_10542.pdf",
            "byteSize": 245823,
            "attachmentContent": "JVBERi0xLjUKJeTl5OTlCjEgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1B...
            "parentType": "Purchase Invoice",
            "parentId": "INV-10542",
            "lineNumber": 0,
            "documentFlowSales": true,
            "documentFlowPurchase": true,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/documentAttachments('
            + _path_value(document_attachment_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.DocumentAttachment.model_validate(data)

class EmployeesClient(_EntityClient):
    """Generated operations for ``employees``."""

    def create(
        self,
        company_id: str,
        body: _models.EmployeeCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Employee:
        """Create employees

        Creates an employee object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_create
        Operation id: dynamics_employee_create
        Request model: EmployeeCreate
        Response model: Employee

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/employees
        Content-type: application/json

        {
          "id": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
          "number": "AH",
          "givenName": "Annette",
          "middleName": "",
          "surname": "Hill",
          "jobTitle": "Secretary",
          "addressLine1": "677 Fifth Avenue",
          "addressLine2": "",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
          "id": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
          "number": "AH",
          "displayName": "Annette Hill",
          "givenName": "Annette",
          "middleName": "",
          "surname": "Hill",
          "jobTitle": "Secretary",
          "addressLine1": "677 Fifth Avenue",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/employees'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Employee.model_validate(data)

    def delete(
        self,
        company_id: str,
        employee_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete employees

        Deletes an employee object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_delete
        Operation id: dynamics_employee_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/employees({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        employee_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Employee:
        """Get employees

        Gets an employee object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_get
        Operation id: dynamics_employee_get
        Response model: Employee
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Employee.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Employee]:
        """List employees

        List employees objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_get
        Operation id: dynamics_employee_list
        Response model: list[Employee]
        """

        path = '/companies(' + _path_value(company_id) + ')/employees'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Employee.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        employee_id: str,
        body: _models.EmployeeUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Employee:
        """Update employees

        Updates an employee object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_employee_update
        Operation id: dynamics_employee_update
        Request model: EmployeeUpdate
        Response model: Employee

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/employees({id})
        Content-type: application/json

        {
          "givenName": "Anthony",
          "phoneNumber": "0678-8712-3455"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
            "number": "AH",
            "displayName": "Anthony Hill",
            "givenName": "Anthony",
            "middleName": "",
            "surname": "Hill",
            "jobTitle": "Secretary",
            "addressLine1": "677 Fifth Avenue",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/employees('
            + _path_value(employee_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Employee.model_validate(data)

class FixedAssetsClient(_EntityClient):
    """Generated operations for ``fixed_assets``."""

    def create(
        self,
        company_id: str,
        fixed_asset_id: str,
        body: _models.FixedAssetCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.FixedAsset:
        """Create fixedAssets

        Creates a fixed asset object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedasset_create
        Operation id: dynamics_fixedasset_create
        Request model: FixedAssetCreate
        Response model: FixedAsset

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssets({id})
        Content-type: application/json
        {
            "number": "FA-1005",
            "displayName": "Company Vehicle - Ford Escape",
            "fixedAssetLocationCode": "MAIN",
            "fixedAssetLocationId": "LOC0001",
            "classCode": "VEHICLE",
            "subclassCode": "COMPANY",
            "blocked": false,
            "serialNumber": "1FMCU0F74MUA12345",
            "employeeNumber": "EM1042",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "FA000012",
            "number": "FA-1005",
            "displayName": "Company Vehicle - Ford Escape",
            "fixedAssetLocationCode": "MAIN",
            "fixedAssetLocationId": "LOC0001",
            "classCode": "VEHICLE",
            "subclassCode": "COMPANY",
            "blocked": false,
            "serialNumber": "1FMCU0F74MUA12345",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssets('
            + _path_value(fixed_asset_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.FixedAsset.model_validate(data)

    def delete(
        self,
        company_id: str,
        fixed_asset_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete fixedAssets

        Deletes a fixed asset object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedasset_delete
        Operation id: dynamics_fixedasset_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssets({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssets('
            + _path_value(fixed_asset_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        fixed_asset_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.FixedAsset:
        """Get fixedAssets

        Gets a fixed asset object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedasset_get
        Operation id: dynamics_fixedasset_get
        Response model: FixedAsset

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssets({id})

        Example response:
        {
            "id": "FA000012",
            "number": "FA-1005",
            "displayName": "Company Vehicle - Ford Escape",
            "fixedAssetLocationCode": "MAIN",
            "fixedAssetLocationId": "LOC0001",
            "classCode": "VEHICLE",
            "subclassCode": "COMPANY",
            "blocked": false,
            "serialNumber": "1FMCU0F74MUA12345",
            "employeeNumber": "EM1042",
            "employeeId": "e2a5738a-44e3-ea11-bb43-000d3a2feca1",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssets('
            + _path_value(fixed_asset_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.FixedAsset.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.FixedAsset]:
        """List fixedAssets

        List fixedAssets objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedasset_get
        Operation id: dynamics_fixedasset_list
        Response model: list[FixedAsset]
        """

        path = '/companies(' + _path_value(company_id) + ')/fixedAssets'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.FixedAsset.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        fixed_asset_id: str,
        body: _models.FixedAssetUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.FixedAsset:
        """Update fixedAssets

        Updates a fixed asset object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedasset_update
        Operation id: dynamics_fixedasset_update
        Request model: FixedAssetUpdate
        Response model: FixedAsset

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssets({id})
        Content-type: application/json
        {
            "id": "FA000012",
            "employeeNumber": "EM2068",
            "employeeId": "f3b6742a-44e3-ea11-bb43-000d3a2feca1",
            "underMaintenance": true,
            "fixedAssetLocationCode": "BRANCH",
            "fixedAssetLocationId": "LOC0002"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "FA000012",
            "number": "FA-1005",
            "displayName": "Company Vehicle - Ford Escape",
            "fixedAssetLocationCode": "BRANCH",
            "fixedAssetLocationId": "LOC0002",
            "classCode": "VEHICLE",
            "subclassCode": "COMPANY",
            "blocked": false,
            "serialNumber": "1FMCU0F74MUA12345",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssets('
            + _path_value(fixed_asset_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.FixedAsset.model_validate(data)

class FixedAssetLocationsClient(_EntityClient):
    """Generated operations for ``fixed_asset_locations``."""

    def create(
        self,
        company_id: str,
        fixed_asset_location_id: str,
        body: _models.FixedAssetLocationCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.FixedAssetLocation:
        """Create fixedAssetLocations

        Creates a fixed asset location object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedassetlocation_create
        Operation id: dynamics_fixedassetlocation_create
        Request model: FixedAssetLocationCreate
        Response model: FixedAssetLocation

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssetLocations({id})
        Content-type: application/json
        {
            "code": "WAREHOUSE",
            "displayName": "Main Warehouse Facility"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "LOC0003",
            "code": "WAREHOUSE",
            "displayName": "Main Warehouse Facility",
            "lastModifiedDateTime": "2025-04-29T16:25:42Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssetLocations('
            + _path_value(fixed_asset_location_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.FixedAssetLocation.model_validate(data)

    def delete(
        self,
        company_id: str,
        fixed_asset_location_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete fixedAssetLocations

        Deletes a fixed asset location object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedassetlocation_delete
        Operation id: dynamics_fixedassetlocation_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssetLocations({...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssetLocations('
            + _path_value(fixed_asset_location_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        fixed_asset_location_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.FixedAssetLocation:
        """Get fixedAssetLocations

        Gets a fixed asset location object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedassetlocation_get
        Operation id: dynamics_fixedassetlocation_get
        Response model: FixedAssetLocation

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssetLocations({id})

        Example response:
        {
            "id": "LOC0003",
            "code": "WAREHOUSE",
            "displayName": "Main Warehouse Facility",
            "lastModifiedDateTime": "2025-04-15T16:25:42Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssetLocations('
            + _path_value(fixed_asset_location_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.FixedAssetLocation.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.FixedAssetLocation]:
        """List fixedAssetLocations

        List fixedAssetLocations objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedassetlocation_get
        Operation id: dynamics_fixedassetlocation_list
        Response model: list[FixedAssetLocation]
        """

        path = '/companies(' + _path_value(company_id) + ')/fixedAssetLocations'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.FixedAssetLocation.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        fixed_asset_location_id: str,
        body: _models.FixedAssetLocationUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.FixedAssetLocation:
        """Update fixedAssetLocations

        Updates a  fixed asset location object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_fixedassetlocation_update
        Operation id: dynamics_fixedassetlocation_update
        Request model: FixedAssetLocationUpdate
        Response model: FixedAssetLocation

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/fixedAssetLocations({id})
        Content-type: application/json
        {
            "id": "LOC0003",
            "displayName": "Main Warehouse Facility - East Wing"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "LOC0003",
            "code": "WAREHOUSE",
            "displayName": "Main Warehouse Facility - East Wing",
            "lastModifiedDateTime": "2025-04-29T16:48:37Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/fixedAssetLocations('
            + _path_value(fixed_asset_location_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.FixedAssetLocation.model_validate(data)

class GeneralLedgerEntriesClient(_EntityClient):
    """Generated operations for ``general_ledger_entries``."""

    def get(
        self,
        company_id: str,
        general_ledger_entry_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.GeneralLedgerEntry:
        """Get generalLedgerEntries

        Gets a generalLedgerEntry object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_generalledgerentry_get
        Operation id: dynamics_generalledgerentry_get
        Response model: GeneralLedgerEntry

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/generalLedgerEntries({id})

        Example response:
        {
            "id": "9dd7b4dc-44e3-ea11-bb43-000d3a2feca1",
            "entryNumber": 1,
            "postingDate": "2019-01-15",
            "documentNumber": "PS-INV103001",
            "documentType": " ",
            "accountId": "aaa5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountNumber": "10700",
            "description": "Direct Cost 20000 on 01/15/19",
            "debitAmount": 0,
            "creditAmount": 128.4,
            "lastModifiedDateTime": "2020-08-21T00:25:56.383Z"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/generalLedgerEntries('
            + _path_value(general_ledger_entry_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.GeneralLedgerEntry.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.GeneralLedgerEntry]:
        """List generalLedgerEntries

        List generalLedgerEntries objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_generalledgerentry_get
        Operation id: dynamics_generalledgerentry_list
        Response model: list[GeneralLedgerEntry]
        """

        path = '/companies(' + _path_value(company_id) + ')/generalLedgerEntries'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.GeneralLedgerEntry.model_validate(item) for item in items]

class GeneralLedgerSetupsClient(_EntityClient):
    """Generated operations for ``general_ledger_setups``."""

    def get(
        self,
        company_id: str,
        general_ledger_setup_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.GeneralLedgerSetup:
        """Get generalLedgerSetup

        Gets a general ledger setup object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_generalledgersetup_get
        Operation id: dynamics_generalledgersetup_get
        Response model: GeneralLedgerSetup

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/generalLedgerSetup({id})

        Example response:
        {
            "id": "00000000-0000-0000-0000-000000000001",
            "allowPostingFrom": "2025-01-01",
            "allowPostingTo": "2025-12-31",
            "additionalReportingCurrency": "EUR",
            "localCurrencyCode": "USD",
            "localCurrencySymbol": "$",
            "lastModifiedDateTime": "2025-03-15T09:45:12Z",
            "allowQueryFromConsolidation": true
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/generalLedgerSetup('
            + _path_value(general_ledger_setup_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.GeneralLedgerSetup.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.GeneralLedgerSetup]:
        """List generalLedgerSetup

        List generalLedgerSetup objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_generalledgersetup_get
        Operation id: dynamics_generalledgersetup_list
        Response model: list[GeneralLedgerSetup]
        """

        path = '/companies(' + _path_value(company_id) + ')/generalLedgerSetup'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.GeneralLedgerSetup.model_validate(item) for item in items]

class GeneralProductPostingGroupsClient(_EntityClient):
    """Generated operations for ``general_product_posting_groups``."""

    def get(
        self,
        company_id: str,
        general_product_posting_group_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.GeneralProductPostingGroup:
        """Get generalProductPostingGroups

        Gets a general product posting group object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_generalproductpostinggroup_get
        Operation id: dynamics_generalproductpostinggroup_get
        Response model: GeneralProductPostingGroup

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/generalProductPostingGro...

        Example response:
        {
        "@odata.etag": "W/\\"JzQ0O1RkZjFGSzJKcXR3VU5QTmNyMUNuUjltT2Z5b1FtWjV5eGdndHNKcXN5bFE9M...
        "id": "50bd9bdb-51ff-eb11-bb76-000d3a220646",
        "code": "MISC",
        "description": "Miscellaneous with VAT",
        "defaultVATProductPostingGroup": "VAT25",
        "autoInsertDefault": true
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/generalProductPostingGroups('
            + _path_value(general_product_posting_group_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.GeneralProductPostingGroup.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.GeneralProductPostingGroup]:
        """List generalProductPostingGroups

        List generalProductPostingGroups objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_generalproductpostinggroup_get
        Operation id: dynamics_generalproductpostinggroup_list
        Response model: list[GeneralProductPostingGroup]
        """

        path = '/companies(' + _path_value(company_id) + ')/generalProductPostingGroups'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.GeneralProductPostingGroup.model_validate(item) for item in items]

class IncomeStatementsClient(_EntityClient):
    """Generated operations for ``income_statements``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.IncomeStatement:
        """Get incomeStatement

        Gets an income statement object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_incomestatement_get
        Operation id: dynamics_incomestatement_get
        Response model: IncomeStatement

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/incomeStatements?$orderb...

        Example response:
        {
            "id": "bafbf171-44e3-ea11-bb43-000d3a2feca1",
            "lineNumber": 10000,
            "display": "Income",
            "netChange": 0,
            "lineType": "header",
            "indentation": 0,
            "dateFilter": "2020-08-21"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/incomeStatements'
        data = self._client.get(path, query=query, params=params)
        return _models.IncomeStatement.model_validate(data)

class InventoryPostingGroupsClient(_EntityClient):
    """Generated operations for ``inventory_posting_groups``."""

    def get(
        self,
        company_id: str,
        inventory_posting_group_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.InventoryPostingGroup:
        """Get inventoryPostingGroups

        Gets an inventory posting group object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_inventorypostinggroup_get
        Operation id: dynamics_inventorypostinggroup_get
        Response model: InventoryPostingGroup

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/inventoryPostingGroups({...

        Example response:
        {
        "@odata.etag": "W/\\"JzQ0O2Zpb3ZGaXJybzIvSXRpWHNsZWJRNFV1ZUcycUdvTkFOV2paQVNiQVlaNkU9M...
        "id": "dd318ff3-51ff-eb11-bb76-000d3a220646",
        "code": "RESALE",
        "description": "Resale items"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/inventoryPostingGroups('
            + _path_value(inventory_posting_group_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.InventoryPostingGroup.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.InventoryPostingGroup]:
        """List inventoryPostingGroups

        List inventoryPostingGroups objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_inventorypostinggroup_get
        Operation id: dynamics_inventorypostinggroup_list
        Response model: list[InventoryPostingGroup]
        """

        path = '/companies(' + _path_value(company_id) + ')/inventoryPostingGroups'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.InventoryPostingGroup.model_validate(item) for item in items]

class ItemsClient(_EntityClient):
    """Generated operations for ``items``."""

    def create(
        self,
        company_id: str,
        body: _models.ItemCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Item:
        """Create items

        Creates an item object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_create
        Operation id: dynamics_item_create
        Request model: ItemCreate
        Response model: Item

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/items
        Content-type: application/json

        {
            "number": "1896-S",
            "displayName": "ATHENS Desk",
            "type": "Inventory",
            "itemCategoryId": "e21a6a90-44e3-ea11-bb43-000d3a2feca1",
            "itemCategoryCode": "TABLE",
            "blocked": false,
            "gtin": "",
            "unitPrice": 1000.8,
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "1896-S",
            "displayName": "ATHENS Desk",
            "displayName2": "",
            "type": "Inventory",
            "itemCategoryId": "e21a6a90-44e3-ea11-bb43-000d3a2feca1",
            "itemCategoryCode": "TABLE",
            "blocked": false,
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/items'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Item.model_validate(data)

    def delete(
        self,
        company_id: str,
        item_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete items

        Deletes an item object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_delete
        Operation id: dynamics_item_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/items({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        item_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Item:
        """Get items

        Gets an item object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_get
        Operation id: dynamics_item_get
        Response model: Item

        Example request:
        GET https://graph.microsoft.com/v2.0businesscentralPrefix/companies({id})/items({id})

        Example response:
        {
            "id": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "1896-S",
            "displayName": "ATHENS Desk",
            "type": "Inventory",
            "itemCategoryId": "e21a6a90-44e3-ea11-bb43-000d3a2feca1",
            "itemCategoryCode": "TABLE",
            "blocked": false,
            "gtin": "",
            "inventory": 4,
            "unitPrice": 1000.8,
            "priceIncludesTax": false,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Item.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Item]:
        """List items

        List items objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_get
        Operation id: dynamics_item_list
        Response model: list[Item]
        """

        path = '/companies(' + _path_value(company_id) + ')/items'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Item.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        item_id: str,
        body: _models.ItemUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Item:
        """Update items

        Updates an item object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_update
        Operation id: dynamics_item_update
        Request model: ItemUpdate
        Response model: Item

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/items({id})
        Content-type: application/json

        {
          "displayName": "ATHENS Desk - blocked",
          "blocked": true
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "1896-S",
            "displayName": "ATHENS Desk - blocked",
            "type": "Inventory",
            "itemCategoryId": "e21a6a90-44e3-ea11-bb43-000d3a2feca1",
            "itemCategoryCode": "TABLE",
            "blocked": true,
            "gtin": "",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Item.model_validate(data)

class ItemCategoriesClient(_EntityClient):
    """Generated operations for ``item_categories``."""

    def create(
        self,
        company_id: str,
        body: _models.ItemCategoryCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ItemCategory:
        """Create itemCategories

        Creates a itemCategory object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemcategory_create
        Operation id: dynamics_itemcategory_create
        Request model: ItemCategoryCreate
        Response model: ItemCategory

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/itemCategories
        Content-type: application/json

        {
          "code": "CHAIR",
          "displayName": "Office Chair"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "dd1a6a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "CHAIR",
            "displayName": "Office Chair",
            "lastModifiedDateTime": "2020-08-21T00:24:31.777Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/itemCategories'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.ItemCategory.model_validate(data)

    def delete(
        self,
        company_id: str,
        item_category_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete itemCategories

        Deletes itemCategory  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemcategory_delete
        Operation id: dynamics_itemcategory_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/itemCategories({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemCategories('
            + _path_value(item_category_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        item_category_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ItemCategory:
        """Get itemCategories

        Gets a itemCategory object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemcategory_get
        Operation id: dynamics_itemcategory_get
        Response model: ItemCategory

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/itemCategories({id})

        Example response:
        {
            "id": "dd1a6a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "CHAIR",
            "displayName": "Office Chair",
            "lastModifiedDateTime": "2020-08-21T00:24:31.777Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemCategories('
            + _path_value(item_category_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.ItemCategory.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.ItemCategory]:
        """List itemCategories

        List itemCategories objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemcategory_get
        Operation id: dynamics_itemcategory_list
        Response model: list[ItemCategory]
        """

        path = '/companies(' + _path_value(company_id) + ')/itemCategories'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.ItemCategory.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        item_category_id: str,
        body: _models.ItemCategoryUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.ItemCategory:
        """Update itemCategories

        Updates a itemCategory object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemcategory_update
        Operation id: dynamics_itemcategory_update
        Request model: ItemCategoryUpdate
        Response model: ItemCategory

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/itemCategories({id})
        Content-type: application/json

        {
          "displayName": "Office Chair - swivel"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "dd1a6a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "CHAIR",
            "displayName": "Office Chair - swivel",
            "lastModifiedDateTime": "2020-08-21T00:24:31.777Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemCategories('
            + _path_value(item_category_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.ItemCategory.model_validate(data)

class ItemLedgerEntriesClient(_EntityClient):
    """Generated operations for ``item_ledger_entries``."""

    def get(
        self,
        company_id: str,
        item_ledger_entry_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ItemLedgerEntry:
        """Get itemLedgerEntries

        Gets an item ledger entry object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemledgerentry_get
        Operation id: dynamics_itemledgerentry_get
        Response model: ItemLedgerEntry

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/itemLedgerEntries({id})

        Example response:
        {
        "@odata.etag": "W/\\"JzQ0O2ZyaTlPVmR6WUxDOEJyMExqOER1WXgxR0IvanErd0t4WXM0ckpzY20xSkU9M...
        "id": "44a76d24-52ff-eb11-bb76-000d3a220646",
        "entryNumber": 1,
        "itemNumber": "1100",
        "postingDate": "2022-06-01",
        "entryType": "Positive_x0020_Adjmt_x002E_",
        "sourceNumber": "",
        "sourceType": "_x0020_",
        "documentNumber": "START-MANF",
        "documentType": "_x0020_",
        "description": "",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemLedgerEntries('
            + _path_value(item_ledger_entry_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.ItemLedgerEntry.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.ItemLedgerEntry]:
        """List itemLedgerEntries

        List itemLedgerEntries objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemledgerentry_get
        Operation id: dynamics_itemledgerentry_list
        Response model: list[ItemLedgerEntry]
        """

        path = '/companies(' + _path_value(company_id) + ')/itemLedgerEntries'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.ItemLedgerEntry.model_validate(item) for item in items]

class ItemVariantsClient(_EntityClient):
    """Generated operations for ``item_variants``."""

    def create(
        self,
        company_id: str,
        item_variant_id: str,
        body: _models.ItemVariantCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ItemVariant:
        """Create itemVariants

        Creates a itemVariant object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemvariant_create
        Operation id: dynamics_itemvariant_create
        Request model: ItemVariantCreate
        Response model: ItemVariant

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/itemVariants
        Content-type: application/json

        {
            "id": "c12af665-c1e3-ea11-aa60-000d3ad7cacb",
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "itemNumber": "1896-S",
            "code": "TESTCRUD",
            "description": "test crud"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "c12af665-c1e3-ea11-aa60-000d3ad7cacb",
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "itemNumber": "1896-S",
            "code": "TESTCRUD",
            "description": "test crud"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemVariants('
            + _path_value(item_variant_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.ItemVariant.model_validate(data)

    def delete(
        self,
        company_id: str,
        item_variant_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete itemVariants

        Deletes itemVariant  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemvariant_delete
        Operation id: dynamics_itemvariant_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/itemVariants({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemVariants('
            + _path_value(item_variant_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        item_variant_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ItemVariant:
        """Get itemVariants

        Gets a itemVariant object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemvariant_get
        Operation id: dynamics_itemvariant_get
        Response model: ItemVariant

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/itemVariants({id})

        Example response:
        {
            "id": "c12af665-c1e3-ea11-aa60-000d3ad7cacb",
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "itemNumber": "1896-S",
            "code": "TESTCRUD",
            "description": "test crud"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemVariants('
            + _path_value(item_variant_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.ItemVariant.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.ItemVariant]:
        """List itemVariants

        List itemVariants objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemvariant_get
        Operation id: dynamics_itemvariant_list
        Response model: list[ItemVariant]
        """

        path = '/companies(' + _path_value(company_id) + ')/itemVariants'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.ItemVariant.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        item_variant_id: str,
        body: _models.ItemVariantUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.ItemVariant:
        """Update itemVariants

        Updates a itemVariant object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_itemvariant_update
        Operation id: dynamics_itemvariant_update
        Request model: ItemVariantUpdate
        Response model: ItemVariant

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/itemVariants({id})
        Content-type: application/json

        {
            "itemNumber": "3876-J"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "c12af665-c1e3-ea11-aa60-000d3ad7cacb",
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "itemNumber": "3876-J",
            "code": "TESTCRUD",
            "description": "test crud"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/itemVariants('
            + _path_value(item_variant_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.ItemVariant.model_validate(data)

class JobQueueEntriesClient(_EntityClient):
    """Generated operations for ``job_queue_entries``."""

    def get(
        self,
        company_id: str,
        job_queue_entry_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.JobQueueEntry:
        """Get jobQueueEntries

        Gets a job queue entry object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_jobqueueentry_get
        Operation id: dynamics_jobqueueentry_get
        Response model: JobQueueEntry

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/jobQueueEntries({id})

        Example response:
        {
            "id": "e7c93b42-89a1-ed11-94cc-000d3a2feca1",
            "jobQueueEntryId": "JQE00042",
            "userId": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
            "lastReadyState": "Ready",
            "expirationDateTime": "2025-05-29T23:59:59Z",
            "earliestStartDateTime": "2025-04-29T20:00:00Z",
            "objectTypeToRun": "Codeunit",
            "objectIdToRun": 12345,
            "objectCaptionToRun": "Customer Data Sync",
            "reportOutputType": "None",
            "maxNumberAttemptsToRun": 5,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/jobQueueEntries('
            + _path_value(job_queue_entry_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.JobQueueEntry.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.JobQueueEntry]:
        """List jobQueueEntries

        List jobQueueEntries objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_jobqueueentry_get
        Operation id: dynamics_jobqueueentry_list
        Response model: list[JobQueueEntry]
        """

        path = '/companies(' + _path_value(company_id) + ')/jobQueueEntries'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.JobQueueEntry.model_validate(item) for item in items]

class JobQueueLogEntriesClient(_EntityClient):
    """Generated operations for ``job_queue_log_entries``."""

    def get(
        self,
        company_id: str,
        job_queue_log_entry_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.JobQueueLogEntry:
        """Get jobQueueLogEntries

        Gets a job queue log entry object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_jobqueuelogentry_get
        Operation id: dynamics_jobqueuelogentry_get
        Response model: JobQueueLogEntry

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/jobQueueLogEntries({id})

        Example response:
        {
            "id": "f8d93b42-89a1-ed11-94cc-000d3a2feca1",
            "jobQueueEntryId": "JQE00042",
            "userId": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
            "startDateTime": "2025-04-28T20:00:03Z",
            "endDateTime": "2025-04-28T20:01:45Z",
            "objectIdToRun": 12345,
            "objectTypeToRun": "Codeunit",
            "status": "Success",
            "description": "Daily customer data synchronization job",
            "errorMessage": "",
            "jobQueueCategoryCode": "SYNC",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/jobQueueLogEntries('
            + _path_value(job_queue_log_entry_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.JobQueueLogEntry.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.JobQueueLogEntry]:
        """List jobQueueLogEntries

        List jobQueueLogEntries objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_jobqueuelogentry_get
        Operation id: dynamics_jobqueuelogentry_list
        Response model: list[JobQueueLogEntry]
        """

        path = '/companies(' + _path_value(company_id) + ')/jobQueueLogEntries'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.JobQueueLogEntry.model_validate(item) for item in items]

class JournalsClient(_EntityClient):
    """Generated operations for ``journals``."""

    def create(
        self,
        company_id: str,
        journal_id: str,
        body: _models.JournalCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Journal:
        """Create journals

        Creates a journal object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journal_create
        Operation id: dynamics_journal_create
        Request model: JournalCreate
        Response model: Journal

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/journals
        Content-type: application/json

        {
          "code": "DEFAULT",
          "displayName": "Default Journal Batch"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
          "id": "id-value",
          "code": "DEFAULT",
          "displayName": "Default Journal Batch",
          "lastModifiedDateTime": "2017-05-17T11:30:01.313Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Journal.model_validate(data)

    def delete(
        self,
        company_id: str,
        journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete journals

        Deletes a journal object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journal_delete
        Operation id: dynamics_journal_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Journal:
        """Get journals

        Gets a journal object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journal_get
        Operation id: dynamics_journal_get
        Response model: Journal

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})

        Example response:
        {
          "id": "id-value",
          "code": "DEFAULT",
          "displayName": "Default Journal Batch",
          "lastModifiedDateTime": "2017-05-17T11:30:01.313Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Journal.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Journal]:
        """List journals

        List journals objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journal_get
        Operation id: dynamics_journal_list
        Response model: list[Journal]
        """

        path = '/companies(' + _path_value(company_id) + ')/journals'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Journal.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        journal_id: str,
        body: _models.JournalUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Journal:
        """Update journals

        Updates a journal object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journal_update
        Operation id: dynamics_journal_update
        Request model: JournalUpdate
        Response model: Journal

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})
        Content-type: application/json

        {
          "code": "EXPENSE",
          "displayName": "Expense Batch"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
          "id": "id-value",
          "code": "EXPENSE",
          "displayName": "Expense Batch",
          "lastModifiedDateTime": "2017-05-17T11:30:01.313Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Journal.model_validate(data)

class JournalLinesClient(_EntityClient):
    """Generated operations for ``journal_lines``."""

    def create(
        self,
        company_id: str,
        journal_id: str,
        body: _models.JournalLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.JournalLine:
        """Create journalLines

        Creates a journal line in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journalLine_create
        Operation id: dynamics_journalLine_create
        Request model: JournalLineCreate
        Response model: JournalLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})/journalL...
        Content-type: application/json

        {
            "id": "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "journalId": "dd1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "lineNumber": 10000,
            "accountType": "G/L Account",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "accountNumber": "",
            "postingDate": "2018-12-31",
            "documentNumber": "",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "journalId": "dd1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "journalDisplayName": "DEFAULT",
            "lineNumber": 10000,
            "accountType": "G/L Account",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "accountNumber": "",
            "postingDate": "2018-12-31",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')/journalLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.JournalLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        journal_id: str,
        journal_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete journalLines

        Deletes a journal line in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journalline_delete
        Operation id: dynamics_journalline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})/journa...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')/journalLines('
            + _path_value(journal_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        journal_id: str,
        journal_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.JournalLine:
        """Get journalLines

        Gets a journal line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journalline_get
        Operation id: dynamics_journalline_get
        Response model: JournalLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})/journalLi...

        Example response:
        {
            "id": "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "journalId": "dd1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "journalDisplayName": "DEFAULT",
            "lineNumber": 10000,
            "accountType": "G/L Account",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "accountNumber": "",
            "postingDate": "2018-12-31",
            "documentNumber": "",
            "externalDocumentNumber": "",
            "amount": 0,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')/journalLines('
            + _path_value(journal_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.JournalLine.model_validate(data)

    def list(
        self,
        company_id: str,
        journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.JournalLine]:
        """List journalLines

        List journalLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journalline_get
        Operation id: dynamics_journalline_list
        Response model: list[JournalLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')/journalLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.JournalLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        journal_id: str,
        journal_line_id: str,
        body: _models.JournalLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.JournalLine:
        """Update journalLines

        Updates a journal line in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_journalline_update
        Operation id: dynamics_journalline_update
        Request model: JournalLineUpdate
        Response model: JournalLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/journals({id})/journal...
        Content-type: application/json

        {
          "amount": 0
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "0a077d18-45e3-ea11-bb43-000d3a2feca1",
            "journalId": "dd1b6a90-44e3-ea11-bb43-000d3a2feca1",
            "journalDisplayName": "DEFAULT",
            "lineNumber": 10000,
            "accountType": "G/L Account",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "accountNumber": "",
            "postingDate": "2018-12-31",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/journals('
            + _path_value(journal_id)
            + ')/journalLines('
            + _path_value(journal_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.JournalLine.model_validate(data)

class LocationsClient(_EntityClient):
    """Generated operations for ``locations``."""

    def create(
        self,
        company_id: str,
        body: _models.LocationCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Location:
        """Create locations

        Creates a location object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_location_create
        Operation id: dynamics_location_create
        Request model: LocationCreate
        Response model: Location

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/locations
        Content-type: application/json
        {
          "id": "59f029b1-508c-ed11-aada-000d3a298ab3",
          "code": "MAIN",
          "displayName": "Main Warehouse",
          "contact": "Eleanor Faulkner",
          "addressLine1": "UK Campus Bldg 5",
          "addressLine2": "Thames Valley Park",
          "city": "Reading",
          "state": "",
          "country": "GB",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
          "id": "59f029b1-508c-ed11-aada-000d3a298ab3",
          "code": "MAIN",
          "displayName": "Main Warehouse",
          "contact": "Eleanor Faulkner",
          "addressLine1": "UK Campus Bldg 5",
          "addressLine2": "Thames Valley Park",
          "city": "Reading",
          "state": "",
          "country": "GB",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/locations'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Location.model_validate(data)

    def delete(
        self,
        company_id: str,
        location_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete locations

        Deletes a location object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_location_delete
        Operation id: dynamics_location_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/locations({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/locations('
            + _path_value(location_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        location_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Location:
        """Get locations

        Gets a location object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_location_get
        Operation id: dynamics_location_get
        Response model: Location

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/locations({id})

        Example response:
        {
            "id": "59f029b1-508c-ed11-aada-000d3a298ab3",
            "code": "MAIN",
            "displayName": "Main Warehouse",
            "contact": "Eleanor Faulkner",
            "addressLine1": "UK Campus Bldg 5",
            "addressLine2": "Thames Valley Park",
            "city": "Reading",
            "state": "",
            "country": "GB",
            "postalCode": "RG6 1WG",
            "phoneNumber": "+44-(0)10 5214 4987",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/locations('
            + _path_value(location_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Location.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Location]:
        """List locations

        List locations objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_location_get
        Operation id: dynamics_location_list
        Response model: list[Location]
        """

        path = '/companies(' + _path_value(company_id) + ')/locations'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Location.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        location_id: str,
        body: _models.LocationUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Location:
        """Update locations

        Updates a  location object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_location_update
        Operation id: dynamics_location_update
        Request model: LocationUpdate
        Response model: Location

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/locations({id})
        Content-type: application/json
        {
          "displayName": "Main Whse."
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
          "id": "59f029b1-508c-ed11-aada-000d3a298ab3",
          "code": "MAIN",
          "displayName": "Main Whse.",
          "contact": "Eleanor Faulkner",
          "addressLine1": "UK Campus Bldg 5",
          "addressLine2": "Thames Valley Park",
          "city": "Reading",
          "state": "",
          "country": "GB",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/locations('
            + _path_value(location_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Location.model_validate(data)

class OpportunitiesClient(_EntityClient):
    """Generated operations for ``opportunities``."""

    def create(
        self,
        company_id: str,
        opportunity_id: str,
        body: _models.OpportunityCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Opportunity:
        """Create opportunities

        Creates an opportunity object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_opportunity_create
        Operation id: dynamics_opportunity_create
        Request model: OpportunityCreate
        Response model: Opportunity

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/opportunities({id})
        Content-type: application/json
        {
        "number": "OP100101",
        "contactNumber": "CT200116",
        "salespersonCode": "BC",
        "description": "Description"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
        "@odata.etag": "W/\\"JzQ0O05OZnZiNXpLT1BhTmkvQmduNDBxL1pMR09tdE1aZjVJUVYrYVBWb0VzeDA9M...
        "id": "563c6d96-cd04-ec11-9310-000d3abb70f9",
        "number": "OP100101",
        "contactNumber": "CT200116",
        "contactName": "David Oliver Lawrence",
        "contactCompanyName": "A. Gibson\\"s Law Firm",
        "salespersonCode": "BC",
        "description": "Description",
        "status": "Not_x0020_Started",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/opportunities('
            + _path_value(opportunity_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Opportunity.model_validate(data)

    def delete(
        self,
        company_id: str,
        opportunity_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete opportunities

        Deletes an opportunity object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_opportunity_delete
        Operation id: dynamics_opportunity_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/opportunities({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/opportunities('
            + _path_value(opportunity_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        opportunity_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Opportunity:
        """Get opportunities

        Gets an opportunity object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_opportunity_get
        Operation id: dynamics_opportunity_get
        Response model: Opportunity

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/opportunities({id})

        Example response:
        200 OK
        {
        "@odata.etag": "W/\\"JzQ0OzZXc0ZDVjlUYjBOTDNOYmMvbjdTSTNpRWlhVjVXbmRBUzltakJOYmFlTU09M...
        "id": "2438bf05-52ff-eb11-bb76-000d3a220646",
        "number": "OP100001",
        "contactNumber": "CT200116",
        "contactName": "David Oliver Lawrence",
        "contactCompanyName": "A. Gibson\\"s Law Firm",
        "salespersonCode": "BC",
        "description": "New tables",
        "status": "In_x0020_Progress",
        "closed": false,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/opportunities('
            + _path_value(opportunity_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Opportunity.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Opportunity]:
        """List opportunities

        List opportunities objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_opportunity_get
        Operation id: dynamics_opportunity_list
        Response model: list[Opportunity]
        """

        path = '/companies(' + _path_value(company_id) + ')/opportunities'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Opportunity.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        opportunity_id: str,
        body: _models.OpportunityUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Opportunity:
        """Update opportunities

        Updates an  opportunity object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_opportunity_update
        Operation id: dynamics_opportunity_update
        Request model: OpportunityUpdate
        Response model: Opportunity

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/opportunities({id})

        {
        "salespersonCode": "HR",
        "description": "New Description"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
        "@odata.etag": "W/\\"JzQ0Oy84R1BFRmhreUhtZi9iNlJpYVUxYjRmUzFOWFlwYWJTZ3ZHVkVEZGROQ3c9M...
        "id": "563c6d96-cd04-ec11-9310-000d3abb70f9",
        "number": "OP100101",
        "contactNumber": "CT200116",
        "contactName": "David Oliver Lawrence",
        "contactCompanyName": "A. Gibson\\"s Law Firm",
        "salespersonCode": "HR",
        "description": "New Description",
        "status": "Not_x0020_Started",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/opportunities('
            + _path_value(opportunity_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Opportunity.model_validate(data)

class PaymentMethodsClient(_EntityClient):
    """Generated operations for ``payment_methods``."""

    def create(
        self,
        company_id: str,
        body: _models.PaymentMethodCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PaymentMethod:
        """Create paymentMethods

        Creates a paymentMethod object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentmethod_create
        Operation id: dynamics_paymentmethod_create
        Request model: PaymentMethodCreate
        Response model: PaymentMethod

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentMethods
        Content-type: application/json

        {
            "id": "3a196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "ACCOUNT",
            "displayName": "Payment on account"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "3a196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "ACCOUNT",
            "displayName": "Payment on account",
            "lastModifiedDateTime": "2020-08-21T00:48:51.487Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/paymentMethods'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PaymentMethod.model_validate(data)

    def delete(
        self,
        company_id: str,
        payment_method_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete paymentMethods

        Deletes paymentMethod  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentmethod_delete
        Operation id: dynamics_paymentmethod_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentMethods({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/paymentMethods('
            + _path_value(payment_method_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        payment_method_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PaymentMethod:
        """Get paymentMethods

        Gets a paymentMethod object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentmethod_get
        Operation id: dynamics_paymentmethod_get
        Response model: PaymentMethod

        Example request:
        GET https://{businesscentralPrefix}/api/v1.0/companies({id})/paymentMethods({id})

        Example response:
        {

            "id": "3a196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "ACCOUNT",
            "displayName": "Payment on account",
            "lastModifiedDateTime": "2020-08-21T00:48:51.487Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/paymentMethods('
            + _path_value(payment_method_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PaymentMethod.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PaymentMethod]:
        """List paymentMethods

        List paymentMethods objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentmethod_get
        Operation id: dynamics_paymentmethod_list
        Response model: list[PaymentMethod]
        """

        path = '/companies(' + _path_value(company_id) + ')/paymentMethods'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PaymentMethod.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        payment_method_id: str,
        body: _models.PaymentMethodUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PaymentMethod:
        """Update paymentMethods

        Updates a paymentMethod object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentmethod_update
        Operation id: dynamics_paymentmethod_update
        Request model: PaymentMethodUpdate
        Response model: PaymentMethod

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentMethods({id})
        Content-type: application/json

        {
          "displayName": "Personal Check Payment"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "3a196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "ACCOUNT",
            "displayName": "Payment on account",
            "lastModifiedDateTime": "2020-08-21T00:48:51.487Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/paymentMethods('
            + _path_value(payment_method_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PaymentMethod.model_validate(data)

class PaymentTermsClient(_EntityClient):
    """Generated operations for ``payment_terms``."""

    def create(
        self,
        company_id: str,
        body: _models.PaymentTermCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PaymentTerm:
        """Create paymentTerms

        Creates a paymentTerm object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentterm_create
        Operation id: dynamics_paymentterm_create
        Request model: PaymentTermCreate
        Response model: PaymentTerm

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentTerms
        Content-type: application/json

        {
            "code": "10 DAYS",
            "displayName": "Net 10 days",
            "dueDateCalculation": "10D",
            "discountDateCalculation": "",
            "discountPercent": 0,
            "calculateDiscountOnCreditMemos": false
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "01a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "10 DAYS",
            "displayName": "Net 10 days",
            "dueDateCalculation": "10D",
            "discountDateCalculation": "",
            "discountPercent": 0,
            "calculateDiscountOnCreditMemos": false,
            "lastModifiedDateTime": "2020-08-21T00:24:12.633Z"
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/paymentTerms'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PaymentTerm.model_validate(data)

    def delete(
        self,
        company_id: str,
        payment_term_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete paymentTerms

        Deletes paymentTerm  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentterm_delete
        Operation id: dynamics_paymentterm_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentTerms({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/paymentTerms('
            + _path_value(payment_term_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        payment_term_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PaymentTerm:
        """Get paymentTerms

        Gets a paymentTerm object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentterm_get
        Operation id: dynamics_paymentterm_get
        Response model: PaymentTerm

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentTerms({id})

        Example response:
        {
            "id": "01a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "10 DAYS",
            "displayName": "Net 10 days",
            "dueDateCalculation": "10D",
            "discountDateCalculation": "",
            "discountPercent": 0,
            "calculateDiscountOnCreditMemos": false,
            "lastModifiedDateTime": "2020-08-21T00:24:12.633Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/paymentTerms('
            + _path_value(payment_term_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PaymentTerm.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PaymentTerm]:
        """List paymentTerms

        List paymentTerms objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentterm_get
        Operation id: dynamics_paymentterm_list
        Response model: list[PaymentTerm]
        """

        path = '/companies(' + _path_value(company_id) + ')/paymentTerms'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PaymentTerm.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        payment_term_id: str,
        body: _models.PaymentTermUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PaymentTerm:
        """Update paymentTerms

        Updates a paymentTerm object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_paymentterm_update
        Operation id: dynamics_paymentterm_update
        Request model: PaymentTermUpdate
        Response model: PaymentTerm

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/paymentTerms({id})
        Content-type: application/json

        {
          "displayName": "Net 7 days with Discount",
          "discountPercent": 10
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "01a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "10 DAYS",
            "displayName": "Net 7 days with Discount",
            "dueDateCalculation": "10D",
            "discountDateCalculation": "",
            "discountPercent": 10,
            "calculateDiscountOnCreditMemos": false,
            "lastModifiedDateTime": "2020-08-21T00:24:12.633Z"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/paymentTerms('
            + _path_value(payment_term_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PaymentTerm.model_validate(data)

class PdfDocumentsClient(_EntityClient):
    """Generated operations for ``pdf_documents``."""

    def get(
        self,
        company_id: str,
        sales_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PdfDocument:
        """Get pdfDocuments

        Gets a pdfDocument object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_pdfdocument_get
        Operation id: dynamics_pdfdocument_get
        Response model: PdfDocument

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})/pdfD...

        Example response:
        {
            "id": "5fd8a1c5-bde4-ea11-bbf2-00155df3a615",
            "parentId": "5fd8a1c5-bde4-ea11-bbf2-00155df3a615",
            "parentType": "Sales Invoice",
            "pdfDocumentContent@odata.mediaReadLink": "http://onbuyuka-azvm1.europe.corp.micr...
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')/pdfDocument'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PdfDocument.model_validate(data)

class PicturesClient(_EntityClient):
    """Generated operations for ``pictures``."""

    def delete(
        self,
        company_id: str,
        item_id: str,
        picture_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete picture

        Deletes a picture object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_picture_delete
        Operation id: dynamics_picture_delete

        Example request:
        DELETE https://api.businesscentral.dynamics-tie.com/v2.0/api/v2.0/companies(companyId...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture('
            + _path_value(picture_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        item_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Picture:
        """Get picture

        Gets a picture object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_picture_get
        Operation id: dynamics_picture_get
        Response model: Picture

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies(companyId)/items(itemId)/picture

        Example response:
        {
            "id": "53049aad-bde4-ea11-bbf2-00155df3a615",
            "parentType": "Item",
            "width": 400,
            "height": 400,
            "contentType": "image/jpeg",
            "pictureContent@odata.mediaEditLink": "http://bcserver:7048/BC/api/v2.0/companies...
            "pictureContent@odata.mediaReadLink": "http://bcserver:7048/BC/api/v2.0/companies...
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Picture.model_validate(data)

    def picture(
        self,
        company_id: str,
        item_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete item picture

        Deletes the picture of the item in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_delete_picture
        Operation id: dynamics_item_delete_picture

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId}...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def picture_item_get_picture(
        self,
        company_id: str,
        item_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Picture:
        """Get item picture

        Gets an item picture in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_get_picture
        Operation id: dynamics_item_get_picture
        Response model: Picture

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId})/p...

        Example response:
        {
          "id": "d0e5d5da-795a-4924-b376-13665f794cdd",
          "width": 500,
          "height": 496,
          "contentType": "image\\jpeg",
          "content@odata.mediaEditLink": "https:\\\\api.businesscentral.dynamics-tie.com\\v2.0\\a...
          "content@odata.mediaReadLink": "https:\\\\api.businesscentral.dynamics-tie.com\\v2.0\\a...
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Picture.model_validate(data)

    def picture_item_update_picture(
        self,
        company_id: str,
        item_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Picture:
        """Update item picture

        Updates the item picture in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_update_picture
        Operation id: dynamics_item_update_picture
        Response model: Picture

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId})...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Picture.model_validate(data)

    def picture_item_create_picture(
        self,
        company_id: str,
        item_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Picture:
        """Create item picture

        Creates a picture of the item object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_item_create_picture
        Operation id: dynamics_item_create_picture
        Response model: Picture

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({companyId})/items({itemId})/...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Picture.model_validate(data)

class PictureContentsClient(_EntityClient):
    """Generated operations for ``picture_contents``."""

    def create(
        self,
        company_id: str,
        item_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> dict[str, Any]:
        """Create picture

        Creates a picture object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_picture_create
        Operation id: dynamics_picture_create

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies(companyId)/items(itemId)/pic...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture/pictureContent'
        )
        return self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )

    def update(
        self,
        company_id: str,
        item_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> dict[str, Any]:
        """Update picture

        Updates a picture object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_picture_update
        Operation id: dynamics_picture_update

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies(companyId)/items(itemId)/pic...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/items('
            + _path_value(item_id)
            + ')/picture/pictureContent'
        )
        return self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )

class ProjectsClient(_EntityClient):
    """Generated operations for ``projects``."""

    def create(
        self,
        company_id: str,
        body: _models.ProjectCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Project:
        """Create projects

        Creates a project object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_project_create
        Operation id: dynamics_project_create
        Request model: ProjectCreate
        Response model: Project

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/projects
        Content-type: application/json

        {
            "number": "DEERFIELD, 8 WP",
            "displayName": "Setting up Eight Work Areas"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "22d7a1c5-bde4-ea11-bbf2-00155df3a615",
            "number": "DEERFIELD, 8 WP",
            "displayName": "Setting up Eight Work Areas"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/projects'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Project.model_validate(data)

    def delete(
        self,
        company_id: str,
        project_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete projects

        Deletes project  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_project_delete
        Operation id: dynamics_project_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/projects({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/projects('
            + _path_value(project_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        project_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Project:
        """Get projects

        Gets a project object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_project_get
        Operation id: dynamics_project_get
        Response model: Project

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/projects({id})

        Example response:
        {
            "id": "22d7a1c5-bde4-ea11-bbf2-00155df3a615",
            "number": "DEERFIELD, 8 WP",
            "displayName": "Setting up Eight Work Areas"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/projects('
            + _path_value(project_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Project.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Project]:
        """List projects

        List projects objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_project_get
        Operation id: dynamics_project_list
        Response model: list[Project]
        """

        path = '/companies(' + _path_value(company_id) + ')/projects'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Project.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        project_id: str,
        body: _models.ProjectUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Project:
        """Update projects

        Updates a project object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_project_update
        Operation id: dynamics_project_update
        Request model: ProjectUpdate
        Response model: Project

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/projects({id})
        Content-type: application/json

        {
            "number": "DEERFIELD, 8 WP"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "22d7a1c5-bde4-ea11-bbf2-00155df3a615",
            "number": "DEERFIELD, 8 WP",
            "displayName": "Setting up Eight Work Areas"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/projects('
            + _path_value(project_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Project.model_validate(data)

class PurchaseCreditMemosClient(_EntityClient):
    """Generated operations for ``purchase_credit_memos``."""

    def create(
        self,
        company_id: str,
        purchase_credit_memo_id: str,
        body: _models.PurchaseCreditMemoCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseCreditMemo:
        """Create purchaseCreditMemos

        Creates a purchase credit memo object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemo_create
        Operation id: dynamics_purchasecreditmemo_create
        Request model: PurchaseCreditMemoCreate
        Response model: PurchaseCreditMemo

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemos
        Content-type: application/json
        {
            "number" : "PC1001",
            "creditMemoDate" : "2025-04-01",
            "postingDate" : "2025-04-01",
            "dueDate" : "2025-04-15",
            "vendorId" : "12345",
            "vendorNumber" : "V001",
            "vendorName" : "Contoso Supplies",
            "payToVendorId" : "67890",
            "payToVendorNumber" : "V002",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id" : "PC1001-ID",
            "number" : "PC1001",
            "creditMemoDate" : "2025-04-01",
            "postingDate" : "2025-04-01",
            "dueDate" : "2025-04-15",
            "vendorId" : "12345",
            "vendorNumber" : "V001",
            "vendorName" : "Contoso Supplies",
            "payToVendorId" : "67890",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemos('
            + _path_value(purchase_credit_memo_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PurchaseCreditMemo.model_validate(data)

    def delete(
        self,
        company_id: str,
        purchase_credit_memo_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete purchaseCreditMemos

        Deletes a purchase credit memo object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemo_delete
        Operation id: dynamics_purchasecreditmemo_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemos({...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemos('
            + _path_value(purchase_credit_memo_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        purchase_credit_memo_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseCreditMemo:
        """Get purchaseCreditMemos

        Gets a purchase credit memo object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemo_get
        Operation id: dynamics_purchasecreditmemo_get
        Response model: PurchaseCreditMemo

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemos({id})

        Example response:
        {
            "id": "a6c93b42-89a1-ed11-94cc-000d3a2feca1",
            "number": "PCM-00428",
            "creditMemoDate": "2025-04-15",
            "postingDate": "2025-04-15",
            "dueDate": "2025-05-15",
            "vendorId": "e8d93b42-89a1-ed11-94cc-000d3a2feca1",
            "vendorNumber": "V-0452",
            "vendorName": "Woodgrove Distribution",
            "payToVendorId": "e8d93b42-89a1-ed11-94cc-000d3a2feca1",
            "payToVendorNumber": "V-0452",
            "payToName": "Woodgrove Distribution",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemos('
            + _path_value(purchase_credit_memo_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseCreditMemo.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseCreditMemo]:
        """List purchaseCreditMemos

        List purchaseCreditMemos objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemo_get
        Operation id: dynamics_purchasecreditmemo_list
        Response model: list[PurchaseCreditMemo]
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseCreditMemos'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseCreditMemo.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        purchase_credit_memo_id: str,
        body: _models.PurchaseCreditMemoUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PurchaseCreditMemo:
        """Update purchaseCreditMemos

        Updates a  purchase credit memo object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemo_update
        Operation id: dynamics_purchasecreditmemo_update
        Request model: PurchaseCreditMemoUpdate
        Response model: PurchaseCreditMemo

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemos({id})
        Content-type: application/json
        {
            "id": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "number": "PCM-00103"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "number": "PCM-00103",
            "creditMemoDate": "2023-08-15",
            "postingDate": "2023-08-15",
            "dueDate": "2023-09-14",
            "vendorId": "eeeeeeee-4444-5555-6666-ffffffffffff",
            "vendorNumber": "V00010",
            "vendorName": "Contoso Office Supplies",
            "payToVendorId": "eeeeeeee-4444-5555-6666-ffffffffffff",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemos('
            + _path_value(purchase_credit_memo_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PurchaseCreditMemo.model_validate(data)

class PurchaseCreditMemoLinesClient(_EntityClient):
    """Generated operations for ``purchase_credit_memo_lines``."""

    def create(
        self,
        company_id: str,
        purchase_credit_memo_line_id: str,
        body: _models.PurchaseCreditMemoLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseCreditMemoLine:
        """Create purchaseCreditMemoLines

        Creates a purchase credit memo line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemoline_create
        Operation id: dynamics_purchasecreditmemoline_create
        Request model: PurchaseCreditMemoLineCreate
        Response model: PurchaseCreditMemoLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemoLines...
        Content-type: application/json
        {
            "documentId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "Athens Desk",
            "unitOfMeasureCode": "PCS",
            "unitCost": 250.00,
            "quantity": 2,
            "discountPercent": 5,
            "discountAppliedBeforeTax": true
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "sequence": 10000,
            "itemId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "accountId": "",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "Athens Desk",
            "unitOfMeasureId": "cccccccc-2222-3333-4444-dddddddddddd",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemoLines('
            + _path_value(purchase_credit_memo_line_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PurchaseCreditMemoLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        purchase_credit_memo_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete purchaseCreditMemoLines

        Deletes a purchase credit memo line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemoline_delete
        Operation id: dynamics_purchasecreditmemoline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemoLin...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemoLines('
            + _path_value(purchase_credit_memo_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        purchase_credit_memo_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseCreditMemoLine:
        """Get purchaseCreditMemoLines

        Gets a purchase credit memo line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemoline_get
        Operation id: dynamics_purchasecreditmemoline_get
        Response model: PurchaseCreditMemoLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemoLines(...

        Example response:
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "sequence": 10000,
            "itemId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "accountId": "",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "Athens Desk",
            "unitOfMeasureId": "cccccccc-2222-3333-4444-dddddddddddd",
            "unitOfMeasureCode": "PCS",
            "unitCost": 250.00,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemoLines('
            + _path_value(purchase_credit_memo_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseCreditMemoLine.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseCreditMemoLine]:
        """List purchaseCreditMemoLines

        List purchaseCreditMemoLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemoline_get
        Operation id: dynamics_purchasecreditmemoline_list
        Response model: list[PurchaseCreditMemoLine]
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseCreditMemoLines'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseCreditMemoLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        purchase_credit_memo_line_id: str,
        body: _models.PurchaseCreditMemoLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PurchaseCreditMemoLine:
        """Update purchaseCreditMemoLines

        Updates a  purchase credit memo line object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasecreditmemoline_update
        Operation id: dynamics_purchasecreditmemoline_update
        Request model: PurchaseCreditMemoLineUpdate
        Response model: PurchaseCreditMemoLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseCreditMemoLine...
        Content-type: application/json
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "quantity": 3
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "sequence": 10000,
            "itemId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "accountId": "",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "Athens Desk",
            "unitOfMeasureId": "cccccccc-2222-3333-4444-dddddddddddd",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseCreditMemoLines('
            + _path_value(purchase_credit_memo_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PurchaseCreditMemoLine.model_validate(data)

class PurchaseInvoicesClient(_EntityClient):
    """Generated operations for ``purchase_invoices``."""

    def create(
        self,
        company_id: str,
        body: _models.PurchaseInvoiceCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseInvoice:
        """Create purchaseInvoices

        Creates a purchase invoice object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseInvoice_create
        Operation id: dynamics_purchaseInvoice_create
        Request model: PurchaseInvoiceCreate
        Response model: PurchaseInvoice

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices
        Content-type: application/json
        {
            "invoiceDate": "2019-01-01",
            "postingDate": "2019-01-01",
            "dueDate": "2019-01-01",
            "vendorInvoiceNumber": "107001",
            "vendorId": "f8a5738a-44e3-ea11-bb43-000d3a2feca1",
            "vendorNumber": "20000",
            "payToVendorId": "f8a5738a-44e3-ea11-bb43-000d3a2feca1",
            "payToVendorNumber": "20000",
            "shipToName": "",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number": "108001",
            "invoiceDate": "2019-01-01",
            "postingDate": "2019-01-01",
            "dueDate": "2019-01-01",
            "vendorInvoiceNumber": "107001",
            "vendorId": "f8a5738a-44e3-ea11-bb43-000d3a2feca1",
            "vendorNumber": "20000",
            "vendorName": "First Up Consultants",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseInvoices'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PurchaseInvoice.model_validate(data)

    def delete(
        self,
        company_id: str,
        purchase_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete purchaseInvoices

        Deletes a purchase invoice object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoice_delete
        Operation id: dynamics_purchaseinvoice_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        purchase_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseInvoice:
        """Get purchaseInvoices

        Gets a purchase invoice object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoice_get
        Operation id: dynamics_purchaseinvoice_get
        Response model: PurchaseInvoice

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id})

        Example response:
        {
            "id": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number": "108001",
            "invoiceDate": "2019-01-01",
            "postingDate": "2019-01-01",
            "dueDate": "2019-01-01",
            "vendorInvoiceNumber": "107001",
            "vendorId": "f8a5738a-44e3-ea11-bb43-000d3a2feca1",
            "vendorNumber": "20000",
            "vendorName": "First Up Consultants",
            "payToName": "First Up Consultants",
            "payToContact": "Evan McIntosh",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseInvoice.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseInvoice]:
        """List purchaseInvoices

        List purchaseInvoices objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoice_get
        Operation id: dynamics_purchaseinvoice_list
        Response model: list[PurchaseInvoice]
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseInvoices'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseInvoice.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        purchase_invoice_id: str,
        body: _models.PurchaseInvoiceUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PurchaseInvoice:
        """Update purchaseInvoices

        Updates a purchase invoice object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoice_update
        Operation id: dynamics_purchaseinvoice_update
        Request model: PurchaseInvoiceUpdate
        Response model: PurchaseInvoice

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id})
        Content-type: application/json

        {
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "number": "108001",
            "invoiceDate": "2019-01-01",
            "postingDate": "2019-01-01",
            "dueDate": "2019-01-01",
            "vendorInvoiceNumber": "107001",
            "vendorId": "f8a5738a-44e3-ea11-bb43-000d3a2feca1",
            "vendorNumber": "20000",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PurchaseInvoice.model_validate(data)

class PurchaseInvoiceLinesClient(_EntityClient):
    """Generated operations for ``purchase_invoice_lines``."""

    def create(
        self,
        company_id: str,
        purchase_invoice_id: str,
        body: _models.PurchaseInvoiceLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseInvoiceLine:
        """Create purchaseInvoiceLines

        Creates a purchase invoice line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseInvoiceLine_create
        Operation id: dynamics_purchaseInvoiceLine_create
        Request model: PurchaseInvoiceLineCreate
        Response model: PurchaseInvoiceLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id})/...
        Content-type: application/json

        {
            "id": "dd8db9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "dd8db9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')/purchaseInvoiceLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PurchaseInvoiceLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        purchase_invoice_id: str,
        purchase_invoice_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete purchaseInvoiceLines

        Deletes a purchase invoice line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoiceline_delete
        Operation id: dynamics_purchaseinvoiceline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id}...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')/purchaseInvoiceLines('
            + _path_value(purchase_invoice_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        purchase_invoice_id: str,
        purchase_invoice_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseInvoiceLine:
        """Get purchaseInvoiceLines

        Gets a purchase invoice line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoiceline_get
        Operation id: dynamics_purchaseinvoiceline_get
        Response model: PurchaseInvoiceLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id})/p...

        Example response:
        {
            "id": "dd8db9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "unitCost": 780.7,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')/purchaseInvoiceLines('
            + _path_value(purchase_invoice_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseInvoiceLine.model_validate(data)

    def list(
        self,
        company_id: str,
        purchase_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseInvoiceLine]:
        """List purchaseInvoiceLines

        List purchaseInvoiceLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoiceline_get
        Operation id: dynamics_purchaseinvoiceline_list
        Response model: list[PurchaseInvoiceLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')/purchaseInvoiceLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseInvoiceLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        purchase_invoice_id: str,
        purchase_invoice_line_id: str,
        body: _models.PurchaseInvoiceLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PurchaseInvoiceLine:
        """Update purchaseInvoiceLines

        Updates a purchase invoice line object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseinvoiceline_update
        Operation id: dynamics_purchaseinvoiceline_update
        Request model: PurchaseInvoiceLineUpdate
        Response model: PurchaseInvoiceLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseInvoices({id})...
        Content-type: application/json

        {
          "quantity": 4
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "dd8db9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseInvoices('
            + _path_value(purchase_invoice_id)
            + ')/purchaseInvoiceLines('
            + _path_value(purchase_invoice_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PurchaseInvoiceLine.model_validate(data)

class PurchaseOrdersClient(_EntityClient):
    """Generated operations for ``purchase_orders``."""

    def create(
        self,
        company_id: str,
        body: _models.PurchaseOrderCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseOrder:
        """Create purchaseOrders

        Creates a purchase order object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorder_create
        Operation id: dynamics_purchaseorder_create
        Request model: PurchaseOrderCreate
        Response model: PurchaseOrder

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrders
        Content-type: application/json
        {
           "orderDate": "2021-01-01",
           "postingDate": "2021-01-01",
           "dueDate": "2021-01-01",
           "vendorId": "",
           "vendorNumber": "20000",
           "payToVendorId": "Evan McIntosh",
           "payToVendorNumber": "20000",
           "shipToName": "First Up Consultants",
           "shipToContact": "Evan McIntosh",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
           "id": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
           "number": "108001",
           "orderDate": "2021-01-01",
           "postingDate": "2021-01-01",
           "dueDate": "2021-01-01",
           "vendorId": "",
           "vendorNumber": "20000",
           "vendorName": "First Up Consultants",
           "payToName": "First Up Consultants",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseOrders'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PurchaseOrder.model_validate(data)

    def delete(
        self,
        company_id: str,
        purchase_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete purchaseOrders

        Deletes a purchase order object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorder_delete
        Operation id: dynamics_purchaseorder_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrders({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        purchase_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseOrder:
        """Get purchaseOrders

        Gets a purchase order object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorder_get
        Operation id: dynamics_purchaseorder_get
        Response model: PurchaseOrder

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrders({id})

        Example response:
        {
           "id": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
           "number": "108001",
           "orderDate": "2021-01-01",
           "postingDate": "2021-01-01",
           "dueDate": "2021-01-01",
           "vendorId": "eeeeeeee-4444-5555-6666-ffffffffffff",
           "vendorNumber": "20000",
           "vendorName": "First Up Consultants",
           "payToName": "First Up Consultants",
           "payToVendorId": "eeeeeeee-4444-5555-6666-ffffffffffff",
           "payToVendorNumber": "20000",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseOrder.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseOrder]:
        """List purchaseOrders

        List purchaseOrders objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorder_get
        Operation id: dynamics_purchaseorder_list
        Response model: list[PurchaseOrder]
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseOrders'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseOrder.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        purchase_order_id: str,
        body: _models.PurchaseOrderUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PurchaseOrder:
        """Update purchaseOrders

        Updates a purchase order object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorder_update
        Operation id: dynamics_purchaseorder_update
        Request model: PurchaseOrderUpdate
        Response model: PurchaseOrder

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrders({id})
        Content-type: application/json
        {
            "id" : "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
            "number" : "108001"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
           "id": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
           "number": "108001",
           "orderDate": "2021-01-01",
           "postingDate": "2021-01-01",
           "dueDate": "2021-01-01",
           "vendorId" : "",
           "vendorNumber": "20000",
           "vendorName": "First Up Consultants",
           "payToName": "First Up Consultants",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PurchaseOrder.model_validate(data)

class PurchaseOrderLinesClient(_EntityClient):
    """Generated operations for ``purchase_order_lines``."""

    def create(
        self,
        company_id: str,
        purchase_order_id: str,
        body: _models.PurchaseOrderLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseOrderLine:
        """Create purchaseOrderLine

        Creates a purchase order line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorderline_create
        Operation id: dynamics_purchaseorderline_create
        Request model: PurchaseOrderLineCreate
        Response model: PurchaseOrderLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrderLines
        Content-type: application/json
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "sequence": 10000,
            "itemId": "cccccccc-2222-3333-4444-dddddddddddd",
            "accountId": "93f5638a-55e3-jk22-aa32-211d3a2fdce5",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "sequence": 10000,
            "itemId": "cccccccc-2222-3333-4444-dddddddddddd",
            "accountId": "93f5638a-55e3-jk22-aa32-211d3a2fdce5",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')/purchaseOrderLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.PurchaseOrderLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        purchase_order_id: str,
        purchase_order_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete purchaseOrderLine

        Deletes a purchase order line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorderline_delete
        Operation id: dynamics_purchaseorderline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrderLines({p...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')/purchaseOrderLines('
            + _path_value(purchase_order_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        purchase_order_id: str,
        purchase_order_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseOrderLine:
        """Get purchaseOrderLines

        Gets a purchase order line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorderline_get
        Operation id: dynamics_purchaseorderline_get
        Response model: PurchaseOrderLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrderLines({purc...

        Example response:
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "sequence": 10000,
            "itemId": "cccccccc-2222-3333-4444-dddddddddddd",
            "accountId": "93f5638a-55e3-jk22-aa32-211d3a2fdce5",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
            "unitOfMeasureCode": "PCS",
            "quantity": 12,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')/purchaseOrderLines('
            + _path_value(purchase_order_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseOrderLine.model_validate(data)

    def list(
        self,
        company_id: str,
        purchase_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseOrderLine]:
        """List purchaseOrderLines

        List purchaseOrderLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorderline_get
        Operation id: dynamics_purchaseorderline_list
        Response model: list[PurchaseOrderLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')/purchaseOrderLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseOrderLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        purchase_order_id: str,
        purchase_order_line_id: str,
        body: _models.PurchaseOrderLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.PurchaseOrderLine:
        """Update purchaseOrderLine

        Updates a  purchase order line object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchaseorderline_update
        Operation id: dynamics_purchaseorderline_update
        Request model: PurchaseOrderLineUpdate
        Response model: PurchaseOrderLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseOrderLines({pu...
        Content-type: application/json
        {
            "id" : "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId" : "bbbbbbbb-1111-2222-3333-cccccccccccc"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "documentId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
            "sequence": 10000,
            "itemId": "cccccccc-2222-3333-4444-dddddddddddd",
            "accountId": "93f5638a-55e3-jk22-aa32-211d3a2fdce5",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseOrders('
            + _path_value(purchase_order_id)
            + ')/purchaseOrderLines('
            + _path_value(purchase_order_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.PurchaseOrderLine.model_validate(data)

class PurchaseReceiptsClient(_EntityClient):
    """Generated operations for ``purchase_receipts``."""

    def get(
        self,
        company_id: str,
        purchase_receipt_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseReceipt:
        """Get purchaseReceipts

        Gets a purchaseReceipt object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasereceipt_get
        Operation id: dynamics_purchasereceipt_get
        Response model: PurchaseReceipt

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseReceipts({id})

        Example response:
        {
           "id": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
           "number": "108001",
           "invoiceDate": "2019-01-01",
           "postingDate": "2019-01-01",
           "dueDate": "2019-01-01",
           "vendorNumber": "20000",
           "vendorName": "First Up Consultants",
           "payToName": "First Up Consultants",
           "payToContact": "Evan McIntosh",
           "payToVendorNumber": "20000",
           "shipToName": "First Up Consultants",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseReceipts('
            + _path_value(purchase_receipt_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseReceipt.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseReceipt]:
        """List purchaseReceipts

        List purchaseReceipts objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasereceipt_get
        Operation id: dynamics_purchasereceipt_list
        Response model: list[PurchaseReceipt]
        """

        path = '/companies(' + _path_value(company_id) + ')/purchaseReceipts'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseReceipt.model_validate(item) for item in items]

class PurchaseReceiptLinesClient(_EntityClient):
    """Generated operations for ``purchase_receipt_lines``."""

    def get(
        self,
        company_id: str,
        purchase_receipt_id: str,
        purchase_receipt_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.PurchaseReceiptLine:
        """Get purchaseReceiptLines

        Gets a purchaseReceiptLine object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasereceiptline_get
        Operation id: dynamics_purchasereceiptline_get
        Response model: PurchaseReceiptLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/purchaseReceipts({id})/p...

        Example response:
        {
           "id": "dd8db9c0-44e3-ea11-bb43-000d3a2feca1",
           "documentId": "5d115c9c-44e3-ea11-bb43-000d3a2feca1",
           "sequence": "10000",
           "lineType": "Item",
           "lineObjectNumber": "1896-S",
           "description": "ATHENS Desk",
           "unitOfMeasureCode": "PCS",
           "unitCost": 780.7,
           "quantity": 4,
           "discountPercent": 5,
           "taxPercent": 10,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseReceipts('
            + _path_value(purchase_receipt_id)
            + ')/purchaseReceiptLines('
            + _path_value(purchase_receipt_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.PurchaseReceiptLine.model_validate(data)

    def list(
        self,
        company_id: str,
        purchase_receipt_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.PurchaseReceiptLine]:
        """List purchaseReceiptLines

        List purchaseReceiptLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_purchasereceiptline_get
        Operation id: dynamics_purchasereceiptline_list
        Response model: list[PurchaseReceiptLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/purchaseReceipts('
            + _path_value(purchase_receipt_id)
            + ')/purchaseReceiptLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.PurchaseReceiptLine.model_validate(item) for item in items]

class RetainedEarningsStatementsClient(_EntityClient):
    """Generated operations for ``retained_earnings_statements``."""

    def get(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.RetainedEarningsStatement:
        """Get retainedEarningsStatement

        Gets a retained earnings statement object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_retainedearningsstatement_get
        Operation id: dynamics_retainedearningsstatement_get
        Response model: RetainedEarningsStatement

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/retainedEarningsStatemen...

        Example response:
        {
            "id": "f7fbf171-44e3-ea11-bb43-000d3a2feca1",
            "lineNumber": 10000,
            "display": "Retained Earnings, Period Start",
            "netChange": 69723.14,
            "lineType": "detail",
            "indentation": 0,
            "dateFilter": "2020-08-21"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/retainedEarningsStatements'
        data = self._client.get(path, query=query, params=params)
        return _models.RetainedEarningsStatement.model_validate(data)

class SalesCreditMemosClient(_EntityClient):
    """Generated operations for ``sales_credit_memos``."""

    def create(
        self,
        company_id: str,
        body: _models.SalesCreditMemoCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesCreditMemo:
        """Create salesCreditMemos

        Creates a sales credit memo object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesCreditMemo_create
        Operation id: dynamics_salesCreditMemo_create
        Request model: SalesCreditMemoCreate
        Response model: SalesCreditMemo

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos
        Content-type: application/json

        {
          "creditMemoDate": "2022-12-27",
          "customerNumber": "10000",
          "currencyCode": "GBP",
          "paymentTermsId": "a0a51911-e48a-ed11-af3b-cf75db0ab305"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
          "id": "1e8cb9c0-44e3-ea11-bb43-000d3a2feca1",
          "number": "1009",
          "creditMemoDate": "2022-12-27",
          "dueDate": "2023-01-27",
          "customerId": "customerId-value",
          "contactId": "",
          "customerNumber": "10000",
          "customerName": "Adatum Corporation",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/salesCreditMemos'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesCreditMemo.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesCreditMemos

        Deletes a sales credit memo object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemo_delete
        Operation id: dynamics_salescreditmemo_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesCreditMemo:
        """Get salesCreditMemos

        Gets a sales credit memo object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemo_get
        Operation id: dynamics_salescreditmemo_get
        Response model: SalesCreditMemo

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id})

        Example response:
        {
          "id": "id-value",
          "number": "1009",
          "creditMemoDate": "2015-12-31",
          "dueDate": "2016-01-31",
          "customerId": "customerId-value",
          "contactId": "",
          "customerNumber": "GL00000008",
          "customerName": "GL00000008",
          "billingPostalAddress": {
            "street": "",
            "city": "",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesCreditMemo.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesCreditMemo]:
        """List salesCreditMemos

        List salesCreditMemos objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemo_get
        Operation id: dynamics_salescreditmemo_list
        Response model: list[SalesCreditMemo]
        """

        path = '/companies(' + _path_value(company_id) + ')/salesCreditMemos'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesCreditMemo.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        body: _models.SalesCreditMemoUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesCreditMemo:
        """Update salesCreditMemos

        Updates a sales credit memo object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemo_update
        Operation id: dynamics_salescreditmemo_update
        Request model: SalesCreditMemoUpdate
        Response model: SalesCreditMemo

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id})
        Content-type: application/json

        {
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
          "id": "id-value",
          "number": "1009",
          "creditMemoDate": "2015-12-31",
          "dueDate": "2016-01-31",
          "customerId": "customerId-value",
          "contactId": "",
          "customerNumber": "GL00000008",
          "customerName": "GL00000008",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesCreditMemo.model_validate(data)

class SalesCreditMemoLinesClient(_EntityClient):
    """Generated operations for ``sales_credit_memo_lines``."""

    def create(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        body: _models.SalesCreditMemoLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesCreditMemoLine:
        """Create salesCreditMemoLines

        Creates a sales credit memo line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesCreditMemoLine_create
        Operation id: dynamics_salesCreditMemoLine_create
        Request model: SalesCreditMemoLineCreate
        Response model: SalesCreditMemoLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id})/...
        Content-type: application/json

        {
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "unitPrice": 1000.8,
            "quantity": 1,
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "cd7b3ba0-bde3-ea11-aa60-000d3ad7cacb",
            "documentId": "cb7b3ba0-bde3-ea11-aa60-000d3ad7cacb",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')/salesCreditMemoLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesCreditMemoLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesCreditMemoLines

        Deletes a sales credit memo line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemoline_delete
        Operation id: dynamics_salescreditmemoline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id}...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')/salesCreditMemoLines('
            + _path_value(sales_credit_memo_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesCreditMemoLine:
        """Get salesCreditMemoLines

        Gets a sales credit memo line in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemoline_get
        Operation id: dynamics_salescreditmemoline_get
        Response model: SalesCreditMemoLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id})/s...

        Example response:
        {
            "id": "cd7b3ba0-bde3-ea11-aa60-000d3ad7cacb",
            "documentId": "cb7b3ba0-bde3-ea11-aa60-000d3ad7cacb",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "unitPrice": 1000.8,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')/salesCreditMemoLines('
            + _path_value(sales_credit_memo_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesCreditMemoLine.model_validate(data)

    def list(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesCreditMemoLine]:
        """List salesCreditMemoLines

        List salesCreditMemoLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemoline_get
        Operation id: dynamics_salescreditmemoline_list
        Response model: list[SalesCreditMemoLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')/salesCreditMemoLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesCreditMemoLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        body: _models.SalesCreditMemoLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesCreditMemoLine:
        """Update salesCreditMemoLines

        Updates a sales credit memo line object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salescreditmemoline_update
        Operation id: dynamics_salescreditmemoline_update
        Request model: SalesCreditMemoLineUpdate
        Response model: SalesCreditMemoLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesCreditMemos({id})...
        Content-type: application/json

        {
          "unitPrice": 1000.8
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "cd7b3ba0-bde3-ea11-aa60-000d3ad7cacb",
            "documentId": "cb7b3ba0-bde3-ea11-aa60-000d3ad7cacb",
            "sequence": 10000,
            "itemId": "fca5738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1896-S",
            "description": "ATHENS Desk",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesCreditMemos('
            + _path_value(sales_credit_memo_id)
            + ')/salesCreditMemoLines('
            + _path_value(sales_credit_memo_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesCreditMemoLine.model_validate(data)

class SalesInvoicesClient(_EntityClient):
    """Generated operations for ``sales_invoices``."""

    def create(
        self,
        company_id: str,
        body: _models.SalesInvoiceCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesInvoice:
        """Create salesInvoices

        Create a sales invoice object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesInvoice_create
        Operation id: dynamics_salesInvoice_create
        Request model: SalesInvoiceCreate
        Response model: SalesInvoice

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices
        Content-type: application/json

        {
            "number": "PS-INV103001",
            "externalDocumentNumber": "",
            "invoiceDate": "2019-01-15",
            "postingDate": "2019-01-15",
            "dueDate": "2019-01-15",
            "customerPurchaseOrderReference": "",
            "customerId": "f3a5738a-44e3-ea11-bb43-000d3a2feca1",
            "customerNumber": "20000",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "number": "PS-INV103001",
            "externalDocumentNumber": "",
            "invoiceDate": "2019-01-15",
            "postingDate": "2019-01-15",
            "dueDate": "2019-01-15",
            "customerPurchaseOrderReference": "",
            "customerId": "f3a5738a-44e3-ea11-bb43-000d3a2feca1",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/salesInvoices'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesInvoice.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesInvoices

        Deletes a sales invoice object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_delete
        Operation id: dynamics_salesinvoice_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesInvoice:
        """Get salesInvoices

        Gets a sales invoice object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_get
        Operation id: dynamics_salesinvoice_get
        Response model: SalesInvoice

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})

        Example response:
        {
            "id": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "number": "PS-INV103001",
            "externalDocumentNumber": "",
            "invoiceDate": "2019-01-15",
            "postingDate": "2019-01-15",
            "dueDate": "2019-01-15",
            "customerPurchaseOrderReference": "",
            "customerId": "f3a5738a-44e3-ea11-bb43-000d3a2feca1",
            "customerNumber": "20000",
            "customerName": "Trey Research",
            "billToName": "Trey Research",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesInvoice.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesInvoice]:
        """List salesInvoices

        List salesInvoices objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_get
        Operation id: dynamics_salesinvoice_list
        Response model: list[SalesInvoice]
        """

        path = '/companies(' + _path_value(company_id) + ')/salesInvoices'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesInvoice.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_invoice_id: str,
        body: _models.SalesInvoiceUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesInvoice:
        """Update salesInvoices

        Updates a sales invoice object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update
        Operation id: dynamics_salesinvoice_update
        Request model: SalesInvoiceUpdate
        Response model: SalesInvoice

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})
        Content-type: application/json

        {
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "number": "PS-INV103001",
            "externalDocumentNumber": "",
            "invoiceDate": "2019-01-15",
            "postingDate": "2019-01-15",
            "dueDate": "2019-01-15",
            "customerPurchaseOrderReference": "",
            "customerId": "f3a5738a-44e3-ea11-bb43-000d3a2feca1",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesInvoice.model_validate(data)

class SalesInvoiceLinesClient(_EntityClient):
    """Generated operations for ``sales_invoice_lines``."""

    def create(
        self,
        company_id: str,
        sales_invoice_id: str,
        body: _models.SalesInvoiceLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesInvoiceLine:
        """Create salesInvoiceLines

        Creates a sales invoice line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesInvoiceLine_create
        Operation id: dynamics_salesInvoiceLine_create
        Request model: SalesInvoiceLineCreate
        Response model: SalesInvoiceLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})/sal...
        Content-type: application/json

        {
          "itemId": "02a6738a-44e3-ea11-bb43-000d3a2feca1",
          "lineType": "Item",
          "lineObjectNumber": "1928-S",
          "description": "AMSTERDAM Lamp",
          "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
          "unitOfMeasureCode": "PCS",
          "unitPrice": 54.9,
          "quantity": 3,
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "238cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "02a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1928-S",
            "description": "AMSTERDAM Lamp",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')/salesInvoiceLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesInvoiceLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_invoice_id: str,
        sales_invoice_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesInvoiceLines

        Deletes a sales invoice line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoiceline_delete
        Operation id: dynamics_salesinvoiceline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})/s...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')/salesInvoiceLines('
            + _path_value(sales_invoice_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_invoice_id: str,
        sales_invoice_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesInvoiceLine:
        """Get salesInvoiceLines

        Gets a sales invoice line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoiceline_get
        Operation id: dynamics_salesinvoiceline_get
        Response model: SalesInvoiceLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})/sale...

        Example response:
        {
            "id": "238cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "02a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1928-S",
            "description": "AMSTERDAM Lamp",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "unitPrice": 54.9,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')/salesInvoiceLines('
            + _path_value(sales_invoice_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesInvoiceLine.model_validate(data)

    def list(
        self,
        company_id: str,
        sales_invoice_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesInvoiceLine]:
        """List salesInvoiceLines

        List salesInvoiceLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoiceline_get
        Operation id: dynamics_salesinvoiceline_list
        Response model: list[SalesInvoiceLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')/salesInvoiceLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesInvoiceLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_invoice_id: str,
        sales_invoice_line_id: str,
        body: _models.SalesInvoiceLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesInvoiceLine:
        """Update salesInvoiceLines

        Updates a sales invoice line object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoiceline_update
        Operation id: dynamics_salesinvoiceline_update
        Request model: SalesInvoiceLineUpdate
        Response model: SalesInvoiceLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices{id}/sale...
        Content-type: application/json

        {
          "discountAmount": 0
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "238cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "02a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1928-S",
            "description": "AMSTERDAM Lamp",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesInvoices('
            + _path_value(sales_invoice_id)
            + ')/salesInvoiceLines('
            + _path_value(sales_invoice_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesInvoiceLine.model_validate(data)

class SalesOrdersClient(_EntityClient):
    """Generated operations for ``sales_orders``."""

    def create(
        self,
        company_id: str,
        body: _models.SalesOrderCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesOrder:
        """Create salesOrders

        Creates a sales order object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesOrder_create
        Operation id: dynamics_salesOrder_create
        Request model: SalesOrderCreate
        Response model: SalesOrder

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders
        Content-type: application/json

        {
          "orderDate": "2023-09-01",
          "customerNumber": "GL00000008",
          "currencyCode": "GBP",
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "b6f4017a-b749-ee11-ad0b-a1422c0f7f1f",
            "number": "101005",
            "externalDocumentNumber": "",
            "orderDate": "2023-09-01",
            "postingDate": "2023-09-02",
            "customerId": "c04c550b-593f-ee11-be74-6045bdc8c285",
            "customerNumber": "10000",
            "customerName": "Adatum Corporation",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/salesOrders'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesOrder.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesOrders

        Deletes a sales order object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorder_delete
        Operation id: dynamics_salesorder_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesOrder:
        """Get salesOrders

        Gets a sales order object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorder_get
        Operation id: dynamics_salesorder_get
        Response model: SalesOrder

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})

        Example response:
        {
          "id": "b6f4017a-b749-ee11-ad0b-a1422c0f7f1f",
          "number": "101005",
          "externalDocumentNumber": "",
          "orderDate": "2015-12-31",
          "postingDate": "2023-09-02",
          "customerId": "c04c550b-593f-ee11-be74-6045bdc8c285",
          "customerNumber": "10000",
          "customerName": "Adatum Corporation",
          "billToName": "Adatum Corporation",
          "billToCustomerId": "c04c550b-593f-ee11-be74-6045bdc8c285",
          "billToCustomerNumber": "10000",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesOrder.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesOrder]:
        """List salesOrders

        List salesOrders objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorder_get
        Operation id: dynamics_salesorder_list
        Response model: list[SalesOrder]
        """

        path = '/companies(' + _path_value(company_id) + ')/salesOrders'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesOrder.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_order_id: str,
        body: _models.SalesOrderUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesOrder:
        """Update salesOrders

        Updates a sales order object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorder_update
        Operation id: dynamics_salesorder_update
        Request model: SalesOrderUpdate
        Response model: SalesOrder

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})
        Content-type: application/json

        {
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "b6f4017a-b749-ee11-ad0b-a1422c0f7f1f",
            "number": "101005",
            "externalDocumentNumber": "",
            "orderDate": "2015-12-31",
            "postingDate": "2023-09-02",
            "customerId": "c04c550b-593f-ee11-be74-6045bdc8c285",
            "customerNumber": "10000",
            "customerName": "Adatum Corporation",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesOrder.model_validate(data)

class SalesOrderLinesClient(_EntityClient):
    """Generated operations for ``sales_order_lines``."""

    def create(
        self,
        company_id: str,
        sales_order_id: str,
        body: _models.SalesOrderLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesOrderLine:
        """Create salesOrderLines

        Creates a sales order line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesOrderLine_create
        Operation id: dynamics_salesOrderLine_create
        Request model: SalesOrderLineCreate
        Response model: SalesOrderLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/sales...
        Content-type: application/json

        {
            "itemId": "0ea6738a-44e3-ea11-bb43-000d3a2feca1",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "quantity": 12,
            "unitPrice": 1397.3,
        ...

        Example response:
        HTTP/2 201 Created
        Content-type: application/json

        {
            "id": "1e8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "960f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "itemId": "0ea6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/salesOrderLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesOrderLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_order_id: str,
        sales_credit_memo_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesOrderLines

        Deletes a sales order line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorderline_delete
        Operation id: dynamics_salesorderline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/sal...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/salesOrderLines('
            + _path_value(sales_credit_memo_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesOrderLine:
        """Get salesOrderLines

        Gets a sales order line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorderline_get
        Operation id: dynamics_salesorderline_get
        Response model: SalesOrderLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/salesO...

        Example response:
        {
            "id": "1e8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "960f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "0ea6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "quantity": 12,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/salesOrderLines('
            + _path_value(sales_order_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesOrderLine.model_validate(data)

    def list(
        self,
        company_id: str,
        sales_order_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesOrderLine]:
        """List salesOrderLines

        List salesOrderLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorderline_get
        Operation id: dynamics_salesorderline_list
        Response model: list[SalesOrderLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/salesOrderLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesOrderLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        body: _models.SalesOrderLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesOrderLine:
        """Update salesOrderLines

        Update a sales order line object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesorderline_update
        Operation id: dynamics_salesorderline_update
        Request model: SalesOrderLineUpdate
        Response model: SalesOrderLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesOrders({id})/sale...
        Content-type: application/json

        {
          "unitPrice": 1397.3
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "1e8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "960f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "0ea6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1996-S",
            "description": "ATLANTA Whiteboard, base",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesOrders('
            + _path_value(sales_order_id)
            + ')/salesOrderLines('
            + _path_value(sales_order_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesOrderLine.model_validate(data)

class SalesQuotesClient(_EntityClient):
    """Generated operations for ``sales_quotes``."""

    def create(
        self,
        company_id: str,
        body: _models.SalesQuoteCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesQuote:
        """Create salesQuotes

        Creates a sales quote object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesQuote_create
        Operation id: dynamics_salesQuote_create
        Request model: SalesQuoteCreate
        Response model: SalesQuote

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes
        Content-type: application/json

        {
          "id": "id-value",
          "number": "1006",
          "documentDate": "2016-12-31",
          "customerNumber": "10000",
          "currencyCode": "GBP",
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/salesQuotes'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesQuote.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_quote_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesQuotes

        Deletes a sales quote object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_delete
        Operation id: dynamics_salesquote_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_quote_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesQuote:
        """Get salesQuotes

        Gets a sales quote object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_get
        Operation id: dynamics_salesquote_get
        Response model: SalesQuote

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})

        Example response:
        {
          "id": "id-value",
          "number": "1006",
          "externalDocumentNumber": "",
          "documentDate": "2019-01-24",
          "dueDate": "2019-01-24",
          "customerId": "customerId-value",
          "contactId": "",
          "customerNumber": "10000",
          "customerName": "Coho Winery",
          "billingPostalAddress": {
            "street": "",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesQuote.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesQuote]:
        """List salesQuotes

        List salesQuotes objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_get
        Operation id: dynamics_salesquote_list
        Response model: list[SalesQuote]
        """

        path = '/companies(' + _path_value(company_id) + ')/salesQuotes'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesQuote.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_quote_id: str,
        body: _models.SalesQuoteUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesQuote:
        """Update salesQuotes

        Updates a sales quote object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquote_update
        Operation id: dynamics_salesquote_update
        Request model: SalesQuoteUpdate
        Response model: SalesQuote

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})
        Content-type: application/json

        {
          "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
          "id": "id-value",
          "number": "1006",
          "externalDocumentNumber": "",
          "documentDate": "2019-01-24",
          "dueDate": "2019-01-24",
          "customerId": "customerId-value",
          "contactId": "",
          "customerNumber": "10000",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesQuote.model_validate(data)

class SalesQuoteLinesClient(_EntityClient):
    """Generated operations for ``sales_quote_lines``."""

    def create(
        self,
        company_id: str,
        sales_quote_id: str,
        body: _models.SalesQuoteLineCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesQuoteLine:
        """Create salesQuoteLines

        Creates a sales quote line object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesQuoteLine_create
        Operation id: dynamics_salesQuoteLine_create
        Request model: SalesQuoteLineCreate
        Response model: SalesQuoteLine

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})/sales...
        Content-type: application/json

        {
            "id": "1c8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "920f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "04a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1936-S",
            "description": "BERLIN Guest Chair, yellow",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "1c8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "920f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "04a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1936-S",
            "description": "BERLIN Guest Chair, yellow",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')/salesQuoteLines'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalesQuoteLine.model_validate(data)

    def delete(
        self,
        company_id: str,
        sales_quote_id: str,
        sales_quote_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salesQuoteLines

        Deletes a sales quote line object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquoteline_delete
        Operation id: dynamics_salesquoteline_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})/sal...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')/salesQuoteLines('
            + _path_value(sales_quote_line_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        sales_quote_id: str,
        sales_quote_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesQuoteLine:
        """Get salesQuoteLines

        Gets a sales quote line object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquoteline_get
        Operation id: dynamics_salesquoteline_get
        Response model: SalesQuoteLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})/salesQ...

        Example response:
        {
            "id": "1c8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "920f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "04a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1936-S",
            "description": "BERLIN Guest Chair, yellow",
            "unitOfMeasureId": "5ca6738a-44e3-ea11-bb43-000d3a2feca1",
            "unitOfMeasureCode": "PCS",
            "unitPrice": 192.8,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')/salesQuoteLines('
            + _path_value(sales_quote_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesQuoteLine.model_validate(data)

    def list(
        self,
        company_id: str,
        sales_quote_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesQuoteLine]:
        """List salesQuoteLines

        List salesQuoteLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquoteline_get
        Operation id: dynamics_salesquoteline_list
        Response model: list[SalesQuoteLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')/salesQuoteLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesQuoteLine.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        sales_quote_id: str,
        sales_quote_line_id: str,
        body: _models.SalesQuoteLineUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalesQuoteLine:
        """Update salesQuoteLines

        Updates a sales quote line in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesquoteline_update
        Operation id: dynamics_salesquoteline_update
        Request model: SalesQuoteLineUpdate
        Response model: SalesQuoteLine

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesQuotes({id})/sale...
        Content-type: application/json

        {
          "lineType": "Item"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "1c8cb9c0-44e3-ea11-bb43-000d3a2feca1",
            "documentId": "920f5c9c-44e3-ea11-bb43-000d3a2feca1",
            "sequence": 10000,
            "itemId": "04a6738a-44e3-ea11-bb43-000d3a2feca1",
            "accountId": "00000000-0000-0000-0000-000000000000",
            "lineType": "Item",
            "lineObjectNumber": "1936-S",
            "description": "BERLIN Guest Chair, yellow",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesQuotes('
            + _path_value(sales_quote_id)
            + ')/salesQuoteLines('
            + _path_value(sales_quote_line_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalesQuoteLine.model_validate(data)

class SalesShipmentsClient(_EntityClient):
    """Generated operations for ``sales_shipments``."""

    def get(
        self,
        company_id: str,
        sales_shipment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesShipment:
        """Get salesShipments

        Gets a salesShipment object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesshipment_get
        Operation id: dynamics_salesshipment_get
        Response model: SalesShipment

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesShipments({id})

        Example response:
        {
           "id": "55c99ea7-bde4-ea11-bbf2-00155df3a61",
           "number": "108001",
           "externalDocumentNumber": "",
           "invoiceDate": "2019-01-01",
           "postingDate": "2019-01-01",
           "dueDate": "2019-10-05",
           "customerPurchaseOrderReference": "",
           "customerNumber": "20000",
           "customerName": "First Up Consultants",
           "billToName": "First Up Consultants",
           "billToCustomerNumber": "20000",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesShipments('
            + _path_value(sales_shipment_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesShipment.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesShipment]:
        """List salesShipments

        List salesShipments objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesshipment_get
        Operation id: dynamics_salesshipment_list
        Response model: list[SalesShipment]
        """

        path = '/companies(' + _path_value(company_id) + ')/salesShipments'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesShipment.model_validate(item) for item in items]

class SalesShipmentLinesClient(_EntityClient):
    """Generated operations for ``sales_shipment_lines``."""

    def get(
        self,
        company_id: str,
        sales_shipment_id: str,
        sales_shipment_line_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalesShipmentLine:
        """Get salesShipmentLines

        Gets a salesShipmentLine object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesshipmentline_get
        Operation id: dynamics_salesshipmentline_get
        Response model: SalesShipmentLine

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salesShipments({id})/sal...

        Example response:
        {
           "id": "238cb9c0-44e3-ea11-bb43-000d3a2feca1",
           "documentId": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
           "documentNo": "829482",
           "sequence": 10000,
           "lineType": "NAV.salesLineType",
           "lineObjectNumber": "1928-S",
           "description": "AMSTERDAM Lamp",
           "unitOfMeasureCode": "PCS",
           "unitPrice":  54.9,
           "quantity": 3,
           "discountPercent": 0,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesShipments('
            + _path_value(sales_shipment_id)
            + ')/salesShipmentLines('
            + _path_value(sales_shipment_line_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalesShipmentLine.model_validate(data)

    def list(
        self,
        company_id: str,
        sales_shipment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalesShipmentLine]:
        """List salesShipmentLines

        List salesShipmentLines objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesshipmentline_get
        Operation id: dynamics_salesshipmentline_list
        Response model: list[SalesShipmentLine]
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salesShipments('
            + _path_value(sales_shipment_id)
            + ')/salesShipmentLines'
        )
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalesShipmentLine.model_validate(item) for item in items]

class SalespeoplePurchasersClient(_EntityClient):
    """Generated operations for ``salespeople_purchasers``."""

    def create(
        self,
        company_id: str,
        salespeople_purchaser_id: str,
        body: _models.SalespeoplePurchaserCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalespeoplePurchaser:
        """Create salespersonPurchasers

        Creates a salesperson purchaser object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salespersonpurchaser_create
        Operation id: dynamics_salespersonpurchaser_create
        Request model: SalespeoplePurchaserCreate
        Response model: SalespeoplePurchaser

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/salespeoplePurchasers({...
        Content-type: application/json
        {
            "code": "JS",
            "displayName": "Jennifer Smith",
            "email": "jennifer.smith@contoso.com",
            "email2": "js@contoso.onmicrosoft.com",
            "phoneNo": "+1 425-555-0187",
            "jobTitle": "Senior Sales Representative",
            "commisionPercent": 7.5,
            "privacyBlocked": false,
            "blocked": false
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json
        {
            "id": "f57a8943-92b5-ed11-94cc-000d3a2feca1",
            "code": "JS",
            "displayName": "Jennifer Smith",
            "email": "jennifer.smith@contoso.com",
            "email2": "js@contoso.onmicrosoft.com",
            "phoneNo": "+1 425-555-0187",
            "jobTitle": "Senior Sales Representative",
            "commisionPercent": 7.5,
            "privacyBlocked": false,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salespeoplePurchasers('
            + _path_value(salespeople_purchaser_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.SalespeoplePurchaser.model_validate(data)

    def delete(
        self,
        company_id: str,
        salespeople_purchaser_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete salespersonPurchasers

        Deletes a salesperson purchaser object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salespersonpurchaser_delete
        Operation id: dynamics_salespersonpurchaser_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/salespeoplePurchasers...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salespeoplePurchasers('
            + _path_value(salespeople_purchaser_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        salespeople_purchaser_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.SalespeoplePurchaser:
        """Get salespersonPurchasers

        Gets a salesperson purchaser object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salespersonpurchaser_get
        Operation id: dynamics_salespersonpurchaser_get
        Response model: SalespeoplePurchaser

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/salespeoplePurchasers({id})

        Example response:
        {
            "id": "f57a8943-92b5-ed11-94cc-000d3a2feca1",
            "code": "JS",
            "displayName": "Jennifer Smith",
            "email": "jennifer.smith@contoso.com",
            "email2": "js@contoso.onmicrosoft.com",
            "phoneNo": "+1 425-555-0187",
            "jobTitle": "Senior Sales Representative",
            "commisionPercent": 7.5,
            "privacyBlocked": false,
            "blocked": false,
            "lastModifiedDateTime": "2025-04-28T15:42:26Z"
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salespeoplePurchasers('
            + _path_value(salespeople_purchaser_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.SalespeoplePurchaser.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.SalespeoplePurchaser]:
        """List salespeoplePurchasers

        List salespeoplePurchasers objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salespersonpurchaser_get
        Operation id: dynamics_salespersonpurchaser_list
        Response model: list[SalespeoplePurchaser]
        """

        path = '/companies(' + _path_value(company_id) + ')/salespeoplePurchasers'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.SalespeoplePurchaser.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        salespeople_purchaser_id: str,
        body: _models.SalespeoplePurchaserUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.SalespeoplePurchaser:
        """Update salespersonPurchasers

        Updates a  salesperson purchaser object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salespersonpurchaser_update
        Operation id: dynamics_salespersonpurchaser_update
        Request model: SalespeoplePurchaserUpdate
        Response model: SalespeoplePurchaser

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salespeoplePurchasers(...
        Content-type: application/json
        {
            "id": "f57a8943-92b5-ed11-94cc-000d3a2feca1",
            "jobTitle": "Sales Manager",
            "commisionPercent": 8.5,
            "phoneNo": "+1 425-555-0198"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json
        {
            "id": "f57a8943-92b5-ed11-94cc-000d3a2feca1",
            "code": "JS",
            "displayName": "Jennifer Smith",
            "email": "jennifer.smith@contoso.com",
            "email2": "js@contoso.onmicrosoft.com",
            "phoneNo": "+1 425-555-0198",
            "jobTitle": "Sales Manager",
            "commisionPercent": 8.5,
            "privacyBlocked": false,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/salespeoplePurchasers('
            + _path_value(salespeople_purchaser_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.SalespeoplePurchaser.model_validate(data)

class ShipmentMethodsClient(_EntityClient):
    """Generated operations for ``shipment_methods``."""

    def create(
        self,
        company_id: str,
        body: _models.ShipmentMethodCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ShipmentMethod:
        """Create shipmentMethods

        Creates a shipmentMethod object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_shipmentmethod_create
        Operation id: dynamics_shipmentmethod_create
        Request model: ShipmentMethodCreate
        Response model: ShipmentMethod

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/shipmentMethods
        Content-type: application/json

        {
            "id": "87a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CFR",
            "displayName": "Cost and Freight",
            "lastModifiedDateTime": "2020-08-21T00:24:14.287Z"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "87a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CFR",
            "displayName": "Cost and Freight",
            "lastModifiedDateTime": "2020-08-21T00:24:14.287Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/shipmentMethods'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.ShipmentMethod.model_validate(data)

    def delete(
        self,
        company_id: str,
        shipment_method_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete shipmentMethods

        Deletes shipmentMethod  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_shipmentmethod_delete
        Operation id: dynamics_shipmentmethod_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/shipmentMethods({id})
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/shipmentMethods('
            + _path_value(shipment_method_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        shipment_method_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.ShipmentMethod:
        """Get shipmentMethods

        Gets a shipmentMethod object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_shipmentmethod_get
        Operation id: dynamics_shipmentmethod_get
        Response model: ShipmentMethod

        Example request:
        GET https://{businesscentralPrefix}/api/v1.0/companies({id})/shipmentMethods({id})

        Example response:
        {
            "id": "87a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "CFR",
            "displayName": "Cost and Freight",
            "lastModifiedDateTime": "2020-08-21T00:24:14.287Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/shipmentMethods('
            + _path_value(shipment_method_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.ShipmentMethod.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.ShipmentMethod]:
        """List shipmentMethods

        List shipmentMethods objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_shipmentmethod_get
        Operation id: dynamics_shipmentmethod_list
        Response model: list[ShipmentMethod]
        """

        path = '/companies(' + _path_value(company_id) + ')/shipmentMethods'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.ShipmentMethod.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        shipment_method_id: str,
        body: _models.ShipmentMethodUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.ShipmentMethod:
        """Update shipmentMethod

        Updates shipmentMethod object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_shipmentmethod_update
        Operation id: dynamics_shipmentmethod_update
        Request model: ShipmentMethodUpdate
        Response model: ShipmentMethod

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/shipmentMethods({id})
        Content-type: application/json

        {
          "code": "PICKUP",
          "displayName": "Pickup at Location"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "87a5738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "PICKUP",
            "displayName": "Pickup at Location",
            "lastModifiedDateTime": "2020-08-21T00:24:14.287Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/shipmentMethods('
            + _path_value(shipment_method_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.ShipmentMethod.model_validate(data)

    def update_shipmentmethods_update(
        self,
        company_id: str,
        shipment_method_id: str,
        body: _models.ShipmentMethodUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.ShipmentMethod:
        """Update shipmentMethods

        Updates a shipment method object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_shipmentmethods_update
        Operation id: dynamics_shipmentmethods_update
        Request model: ShipmentMethodUpdate
        Response model: ShipmentMethod

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/shipmentMethods({id})
        Content-type: application/json

        {
          "displayName": "Pickup at Store Location"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
          "id": "id-value",
          "code": "PICKUP",
          "displayName": "Pickup at Store Location",
          "lastModifiedDateTime": "2017-03-15T02:20:57.09Z"
          }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/shipmentMethods('
            + _path_value(shipment_method_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.ShipmentMethod.model_validate(data)

class SubscriptionsClient(_EntityClient):
    """Generated operations for ``subscriptions``."""

    def create(
        self,
        body: _models.SubscriptionCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Subscription:
        """Create subscription

        Creates a subscriptions object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_subscriptions_create
        Operation id: dynamics_subscriptions_create
        Request model: SubscriptionCreate
        Response model: Subscription

        Example request:
        POST https://{businesscentralPrefix}/api/v1.0/subscriptions
        Content-type: application/json

        {
          "subscriptionId": "c670ea73cacb459bb51dc1740da2f1db",
          "notificationUrl": "https://contoso.com/myCallbacks",
          "resource": "/api/v1.0/companies(f64eba74-dacd-4854-a584-1834f68cfc3a)/customers",
          "userId": "00000000-0000-0000-0000-000000000001",
          "lastModifiedDateTime": "2018-10-12T12:32:35Z",
          "clientState": "optionalvalueof2048",
          "expirationDateTime": "2021-10-15T12:32:35Z",
          "systemCreatedAt": "2017-01-23T00:24:31.766Z",
        ...

        Example response:
        {
          "subscriptionId": "c670ea73cacb459bb51dc1740da2f1db",
          "notificationUrl": "https://contoso.com/myCallbacks",
          "resource": "/api/v1.0/companies(f64eba74-dacd-4854-a584-1834f68cfc3a)/customers",
          "userId": "00000000-0000-0000-0000-000000000001",
          "lastModifiedDateTime": "2018-10-12T12:32:35Z",
          "clientState": "optionalvalueof2048",
          "expirationDateTime": "2021-10-15T12:32:35Z",
          "systemCreatedAt": "2017-01-23T00:24:31.766Z",
          "systemCreatedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
          "systemModifiedAt": "2020-08-21T00:24:31.777Z",
          "systemModifiedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1"
        ...
        """

        path = '/subscriptions'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Subscription.model_validate(data)

    def delete(
        self,
        id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete subscriptions

        Deletes subscriptions  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_subscriptions_delete
        Operation id: dynamics_subscriptions_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v1.0/subscriptions('c670ea73-b37b-4a7e-8dc...
        """

        path = "/subscriptions('" + _path_value(id) + "')"
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Subscription:
        """Get subscriptions

        Gets a subscriptions object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_subscriptions_get
        Operation id: dynamics_subscriptions_get
        Response model: Subscription

        Example request:
        https://{businesscentralPrefix}/api/v1.0/subscriptions

        Example response:
        {
          "subscriptionId": "c670ea73cacb459bb51dc1740da2f1db",
          "notificationUrl": "https://contoso.com/myCallbacks",
          "resource": "/api/v1.0/companies(f64eba74-dacd-4854-a584-1834f68cfc3a)/customers",
          "userId": "00000000-0000-0000-0000-000000000001",
          "lastModifiedDateTime": "2018-10-12T12:32:35Z",
          "clientState": "optionalvalueof2048",
          "expirationDateTime": "2021-10-15T12:32:35Z",
          "systemCreatedAt": "2017-01-23T00:24:31.766Z",
          "systemCreatedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
          "systemModifiedAt": "2020-08-21T00:24:31.777Z",
          "systemModifiedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1"
        ...
        """

        path = '/subscriptions'
        data = self._client.get(path, query=query, params=params)
        return _models.Subscription.model_validate(data)

    def update(
        self,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Subscription:
        """Update subscriptions

        Updates a subscriptions object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_subscriptions_update
        Operation id: dynamics_subscriptions_update
        Response model: Subscription

        Example request:
        https://{businesscentralPrefix}/api/v1.0/subscriptions({'id'})

        Example response:
        {
          "subscriptionId": "c670ea73cacb459bb51dc1740da2f1db",
          "notificationUrl": "https://{notificationUrl}",
          "resource": "/api/v1.0/companies(f64eba74-dacd-4854-a584-1834f68cfc3a)/customers",
          "userId": "00000000-0000-0000-0000-000000000001",
          "lastModifiedDateTime": "2018-10-12T12:32:35Z",
          "clientState": "optionalvalueof2048",
          "expirationDateTime": "2021-10-15T12:32:35Z",
          "systemCreatedAt": "2017-01-23T00:24:31.766Z",
          "systemCreatedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1",
          "systemModifiedAt": "2020-08-21T00:24:31.777Z",
          "systemModifiedBy": "f2a5738a-44e3-ea11-bb43-000d3a2feca1"
        ...
        """

        path = "/subscriptions({'id'})"
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Subscription.model_validate(data)

class TaxAreasClient(_EntityClient):
    """Generated operations for ``tax_areas``."""

    def create(
        self,
        company_id: str,
        tax_area_id: str,
        body: _models.TaxAreaCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TaxArea:
        """Create taxAreas

        Creates a tax area object in Dynamics for Financials.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxArea_create
        Operation id: dynamics_taxArea_create
        Request model: TaxAreaCreate
        Response model: TaxArea

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/taxAreas
        Content-type: application/json
        ```json
        {
            "code": "ATLANTA, GA",
            "displayName": "ATLANTA, GA"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "code": "ATLANTA, GA",
            "displayName": "ATLANTA, GA"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxAreas('
            + _path_value(tax_area_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.TaxArea.model_validate(data)

    def delete(
        self,
        company_id: str,
        tax_area_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete taxAreas

        Deletes a tax area object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxarea_delete
        Operation id: dynamics_taxarea_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/taxAreas({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxAreas('
            + _path_value(tax_area_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        tax_area_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TaxArea:
        """Get taxAreas

        Gets a tax area object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxarea_get
        Operation id: dynamics_taxarea_get
        Response model: TaxArea

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/taxAreas({id})

        Example response:
        {
            "id": "90196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "ATLANTA, GA",
            "displayName": "ATLANTA, GA",
            "taxType": "Sales Tax",
            "lastModifiedDateTime": "2020-08-21T00:24:25.847Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxAreas('
            + _path_value(tax_area_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.TaxArea.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.TaxArea]:
        """List taxAreas

        List taxAreas objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxarea_get
        Operation id: dynamics_taxarea_list
        Response model: list[TaxArea]
        """

        path = '/companies(' + _path_value(company_id) + ')/taxAreas'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.TaxArea.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        tax_area_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.TaxArea:
        """Update taxAreas

        Updates a tax areas object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxarea_update
        Operation id: dynamics_taxarea_update
        Response model: TaxArea

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/taxAreas({id})
        Content-type: application/json

        {
          "code": "ATLANTA, GA",
          "displayName": "tax area",
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "90196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "ATLANTA, GA",
            "displayName": "ATLANTA, GA",
            "taxType": "tax area",
            "lastModifiedDateTime": "2020-08-21T00:24:25.847Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxAreas('
            + _path_value(tax_area_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.TaxArea.model_validate(data)

class TaxGroupsClient(_EntityClient):
    """Generated operations for ``tax_groups``."""

    def create(
        self,
        company_id: str,
        body: _models.TaxGroupCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TaxGroup:
        """Create taxGroups

        Creates a taxGroup object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxgroup_create
        Operation id: dynamics_taxgroup_create
        Request model: TaxGroupCreate
        Response model: TaxGroup

        Example request:
        POST https://{businesscentralPrefix}/api/v1.0/companies({id})/taxGroups
        Content-type: application/json

        {
          "code": "FURNITURE",
          "displayName": "Taxable Olympic Furniture"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "9f196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "FURNITURE",
            "displayName": "Taxable Olympic Furniture",
            "taxType": "Sales Tax",
            "lastModifiedDateTime": "2020-08-21T00:24:26Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/taxGroups'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.TaxGroup.model_validate(data)

    def delete(
        self,
        company_id: str,
        tax_group_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete taxGroups

        Deletes taxGroup  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxgroup_delete
        Operation id: dynamics_taxgroup_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v1.0/companies({id})/taxGroups({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxGroups('
            + _path_value(tax_group_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        tax_group_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TaxGroup:
        """Get taxGroups

        Gets a taxGroup object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxgroup_get
        Operation id: dynamics_taxgroup_get
        Response model: TaxGroup

        Example request:
        GET https://{businesscentralPrefix}/api/v1.0/companies({id})/taxGroups({id})

        Example response:
        {
            "id": "9f196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "FURNITURE",
            "displayName": "Taxable Olympic Furniture",
            "taxType": "Sales Tax",
            "lastModifiedDateTime": "2020-08-21T00:24:26Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxGroups('
            + _path_value(tax_group_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.TaxGroup.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.TaxGroup]:
        """List taxGroups

        List taxGroups objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxgroup_get
        Operation id: dynamics_taxgroup_list
        Response model: list[TaxGroup]
        """

        path = '/companies(' + _path_value(company_id) + ')/taxGroups'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.TaxGroup.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        tax_group_id: str,
        body: _models.TaxGroupUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.TaxGroup:
        """Update taxGroups

        Updates a taxGroup object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_taxgroup_update
        Operation id: dynamics_taxgroup_update
        Request model: TaxGroupUpdate
        Response model: TaxGroup

        Example request:
        PATCH https://{businesscentralPrefix}/api/v1.0/companies({id})/taxGroups({id})
        Content-type: application/json

        {
          "displayName": "Taxable Furniture"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "9f196a90-44e3-ea11-bb43-000d3a2feca1",
            "code": "FURNITURE",
            "displayName": "Taxable Furniture",
            "taxType": "Sales Tax",
            "lastModifiedDateTime": "2020-08-21T00:24:26Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/taxGroups('
            + _path_value(tax_group_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.TaxGroup.model_validate(data)

class TimeRegistrationEntriesClient(_EntityClient):
    """Generated operations for ``time_registration_entries``."""

    def create(
        self,
        company_id: str,
        timeregistration_id: str,
        body: _models.TimeRegistrationEntryCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TimeRegistrationEntry:
        """Create timeRegistrationEntry

        Creates a attachment object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_timeRegistrationEntry_create
        Operation id: dynamics_timeRegistrationEntry_create
        Request model: TimeRegistrationEntryCreate
        Response model: TimeRegistrationEntry

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/timeRegistrationEntries
        Content-type: application/json

        {
            "employeeId": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
            "employeeNumber": "AH",
            "jobId": "00000000-0000-0000-0000-000000000000",
            "jobNumber": "",
            "jobTaskNumber": "",
            "date": "2019-02-02",
            "quantity": 5
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "1a8b1fec-c0e3-ea11-aa60-000d3ad7cacb",
            "employeeId": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
            "employeeNumber": "AH",
            "jobId": "00000000-0000-0000-0000-000000000000",
            "jobNumber": "",
            "jobTaskNumber": "",
            "absence": "",
            "lineNumber": 10000,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/timeRegistrationEntries('
            + _path_value(timeregistration_id)
            + ')'
        )
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.TimeRegistrationEntry.model_validate(data)

    def delete(
        self,
        company_id: str,
        timeregistration_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete timeRegistrationEntries

        Deletes a timeRegistrationEntry object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_timeRegistrationEntry_delete
        Operation id: dynamics_timeRegistrationEntry_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/timeRegistrationEntri...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/timeRegistrationEntries('
            + _path_value(timeregistration_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        timeregistration_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TimeRegistrationEntry:
        """Get timeRegistrationEntries

        Gets timeRegistrationEntries object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_timeRegistrationEntry_get
        Operation id: dynamics_timeRegistrationEntry_get
        Response model: TimeRegistrationEntry

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})timeRegistrationEntries?$...

        Example response:
        {
            "id": "1a8b1fec-c0e3-ea11-aa60-000d3ad7cacb",
            "employeeId": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
            "employeeNumber": "AH",
            "jobId": "00000000-0000-0000-0000-000000000000",
            "jobNumber": "",
            "jobTaskNumber": "",
            "absence": "",
            "lineNumber": 10000,
            "date": "2019-02-02",
            "quantity": 5,
            "status": "Open",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/timeRegistrationEntries('
            + _path_value(timeregistration_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.TimeRegistrationEntry.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.TimeRegistrationEntry]:
        """List timeRegistrationEntries

        List timeRegistrationEntries objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_timeRegistrationEntry_get
        Operation id: dynamics_timeRegistrationEntry_list
        Response model: list[TimeRegistrationEntry]
        """

        path = '/companies(' + _path_value(company_id) + ')/timeRegistrationEntries'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.TimeRegistrationEntry.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        timeregistration_id: str,
        body: _models.TimeRegistrationEntryUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.TimeRegistrationEntry:
        """Update timeRegistrationEntries

        Patch a timeRegistrationEntries in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_timeRegistrationEntry_update
        Operation id: dynamics_timeRegistrationEntry_update
        Request model: TimeRegistrationEntryUpdate
        Response model: TimeRegistrationEntry

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/timeRegistrationEntrie...
        Content-type: application/json

        {
            "quantity": 8
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "1a8b1fec-c0e3-ea11-aa60-000d3ad7cacb",
            "employeeId": "258bb9c0-44e3-ea11-bb43-000d3a2feca1",
            "employeeNumber": "AH",
            "jobId": "00000000-0000-0000-0000-000000000000",
            "jobNumber": "",
            "jobTaskNumber": "",
            "absence": "",
            "lineNumber": 10000,
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/timeRegistrationEntries('
            + _path_value(timeregistration_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.TimeRegistrationEntry.model_validate(data)

class TrialBalancesClient(_EntityClient):
    """Generated operations for ``trial_balances``."""

    def get(
        self,
        company_id: str,
        trial_balance_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.TrialBalance:
        """Get trialBalance

        Gets a trial balance object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_trialbalance_get
        Operation id: dynamics_trialbalance_get
        Response model: TrialBalance

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/trialBalances?$orderby n...

        Example response:
        {
          "number": "1110",
          "display": "Accounts Receivable",
          "totalDebit": "0.00",
          "totalCredit": "0.00",
          "balanceAtDateDebit": "72,893.84",
          "balanceAtDateCredit": "0.00",
          "dateFilter": "2019-12-31"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/trialBalances('
            + _path_value(trial_balance_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.TrialBalance.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.TrialBalance]:
        """List trialBalances

        List trialBalances objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_trialbalance_get
        Operation id: dynamics_trialbalance_list
        Response model: list[TrialBalance]
        """

        path = '/companies(' + _path_value(company_id) + ')/trialBalances'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.TrialBalance.model_validate(item) for item in items]

class UnitsOfMeasuresClient(_EntityClient):
    """Generated operations for ``units_of_measures``."""

    def create(
        self,
        company_id: str,
        body: _models.UnitsOfMeasureCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.UnitsOfMeasure:
        """Create unitsOfMeasure

        Creates a unitOfMeasure object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_unitofmeasure_create
        Operation id: dynamics_unitofmeasure_create
        Request model: UnitsOfMeasureCreate
        Response model: UnitsOfMeasure

        Example request:
        POST https://{businesscentralPrefix}/api/v1.0/companies({id})/unitsOfMeasure
        Content-type: application/json

        {
            "code": "BOX",
            "displayName": "Box",
            "internationalStandardCode": "BX",
            "symbol": ""
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
            "id": "53a6738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "BOX",
            "displayName": "Box",
            "internationalStandardCode": "BX",
            "symbol": "",
            "lastModifiedDateTime": "2020-08-20T22:24:22.193Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/unitsOfMeasure'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.UnitsOfMeasure.model_validate(data)

    def delete(
        self,
        company_id: str,
        units_of_measure_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete unitsOfMeasure

        Deletes unitOfMeasure  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_unitofmeasure_delete
        Operation id: dynamics_unitofmeasure_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/unitsOfMeasure({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/unitsOfMeasure('
            + _path_value(units_of_measure_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        units_of_measure_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.UnitsOfMeasure:
        """Get unitsOfMeasure

        Gets a unitOfMeasure object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_unitofmeasure_get
        Operation id: dynamics_unitofmeasure_get
        Response model: UnitsOfMeasure

        Example request:
        GET https://{businesscentralPrefix}/api/v1.0/companies({id})/unitsOfMeasure({id})

        Example response:
        {
            "id": "53a6738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "BOX",
            "displayName": "Box",
            "internationalStandardCode": "BX",
            "symbol": "",
            "lastModifiedDateTime": "2020-08-20T22:24:22.193Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/unitsOfMeasure('
            + _path_value(units_of_measure_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.UnitsOfMeasure.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.UnitsOfMeasure]:
        """List unitsOfMeasure

        List unitsOfMeasure objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_unitofmeasure_get
        Operation id: dynamics_unitofmeasure_list
        Response model: list[UnitsOfMeasure]
        """

        path = '/companies(' + _path_value(company_id) + ')/unitsOfMeasure'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.UnitsOfMeasure.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        units_of_measure_id: str,
        body: _models.UnitsOfMeasureUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.UnitsOfMeasure:
        """Update unitsOfMeasure

        Updates a unitOfMeasure object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_unitofmeasure_update
        Operation id: dynamics_unitofmeasure_update
        Request model: UnitsOfMeasureUpdate
        Response model: UnitsOfMeasure

        Example request:
        PATCH https://{businesscentralPrefix}/api/v1.0/companies({id})/unitsOfMeasure({id})
        Content-type: application/json

        {
          "displayName": "Box"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "53a6738a-44e3-ea11-bb43-000d3a2feca1",
            "code": "BOX",
            "displayName": "Box",
            "internationalStandardCode": "BX",
            "symbol": "",
            "lastModifiedDateTime": "2020-08-20T22:24:22.193Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/unitsOfMeasure('
            + _path_value(units_of_measure_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.UnitsOfMeasure.model_validate(data)

class VendorsClient(_EntityClient):
    """Generated operations for ``vendors``."""

    def create(
        self,
        company_id: str,
        body: _models.VendorCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Vendor:
        """Create vendors

        Creates a vendor object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_create
        Operation id: dynamics_vendor_create
        Request model: VendorCreate
        Response model: Vendor

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/vendors
        Content-type: application/json

        {
            "id": "f7a5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "10000",
            "displayName": "Fabrikam, Inc.",
            "addressLine1": "10 North Lake Avenue",
            "addressLine2": "",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
        ...

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
          "id": "f7a5738a-44e3-ea11-bb43-000d3a2feca1",
          "number": "10000",
          "displayName": "Fabrikam, Inc.",
          "addressLine1": "10 North Lake Avenue",
          "addressLine2": "",
          "city": "Atlanta",
          "state": "GA",
          "country": "US",
        ...
        """

        path = '/companies(' + _path_value(company_id) + ')/vendors'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.Vendor.model_validate(data)

    def delete(
        self,
        company_id: str,
        vendor_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete vendors

        Deletes a vendor object in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_delete
        Operation id: dynamics_vendor_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/vendors({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        vendor_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.Vendor:
        """Get vendors

        Gets a vendor object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_get
        Operation id: dynamics_vendor_get
        Response model: Vendor

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/vendors({id})

        Example response:
        {
            "id": "f7a5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "10000",
            "displayName": "Fabrikam, Inc.",
            "addressLine1": "10 North Lake Avenue",
            "addressLine2": "",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
            "postalCode": "31772",
            "phoneNumber": "4255550101",
            "email": "krystal.york@contoso.com",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.Vendor.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.Vendor]:
        """List vendors

        List vendors objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_get
        Operation id: dynamics_vendor_list
        Response model: list[Vendor]
        """

        path = '/companies(' + _path_value(company_id) + ')/vendors'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.Vendor.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        vendor_id: str,
        body: _models.VendorUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.Vendor:
        """Update vendors

        Updates a vendor object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendor_update
        Operation id: dynamics_vendor_update
        Request model: VendorUpdate
        Response model: Vendor

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/vendors({id})
        Content-type: application/json

        {
          "displayName": "Wide World Importers Inc.",
          "blocked": "Payment"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
            "id": "f7a5738a-44e3-ea11-bb43-000d3a2feca1",
            "number": "10000",
            "displayName": "Wide World Importers Inc.",
            "addressLine1": "10 North Lake Avenue",
            "addressLine2": "",
            "city": "Atlanta",
            "state": "GA",
            "country": "US",
        ...
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendors('
            + _path_value(vendor_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.Vendor.model_validate(data)

class VendorPaymentsClient(_EntityClient):
    """Generated operations for ``vendor_payments``."""

    def create(
        self,
        company_id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.VendorPayment:
        """Create vendorPayments

        Creates a vendorPayment object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpayment_create
        Operation id: dynamics_vendorpayment_create
        Response model: VendorPayment

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPayments
        Content-type: application/json

        {
        PLACE CODE HERE.
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
        PLACE CODE HERE.
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/vendorPayments'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.VendorPayment.model_validate(data)

    def delete(
        self,
        company_id: str,
        vendor_payment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete vendorPayments

        Deletes vendorPayment  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpayment_delete
        Operation id: dynamics_vendorpayment_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPayments({id})

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPayments('
            + _path_value(vendor_payment_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        vendor_payment_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.VendorPayment:
        """Get vendorPayments

        Gets a vendorPayment object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpayment_get
        Operation id: dynamics_vendorpayment_get
        Response model: VendorPayment

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPayments({id})

        Example response:
        {

        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPayments('
            + _path_value(vendor_payment_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.VendorPayment.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.VendorPayment]:
        """List vendorPayments

        List vendorPayments objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpayment_get
        Operation id: dynamics_vendorpayment_list
        Response model: list[VendorPayment]
        """

        path = '/companies(' + _path_value(company_id) + ')/vendorPayments'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.VendorPayment.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        id: str,
        body: Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.VendorPayment:
        """Update vendorPayments

        Updates a vendorPayment object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpayment_update
        Operation id: dynamics_vendorpayment_update
        Response model: VendorPayment

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPayments({id})
        Content-type: application/json

        {
        PLACE CODE HERE.
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
        PLACE CODE HERE.
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPayments ('
            + _path_value(id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.VendorPayment.model_validate(data)

class VendorPaymentJournalsClient(_EntityClient):
    """Generated operations for ``vendor_payment_journals``."""

    def create(
        self,
        company_id: str,
        body: _models.VendorPaymentJournalCreate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.VendorPaymentJournal:
        """Create vendorPaymentJournals

        Creates a vendorPaymentJournal object in Dynamics 365 Business Central.

        HTTP method: POST
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpaymentjournal_create
        Operation id: dynamics_vendorpaymentjournal_create
        Request model: VendorPaymentJournalCreate
        Response model: VendorPaymentJournal

        Example request:
        POST https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPaymentJournals
        Content-type: application/json

        {
          "code": "OTTER",
          "displayName": "Otter cash receipts and payments",
          "balancingAccountId": "021c2ed0-021d-ed11-9db9-000d3aa935da"
        }

        Example response:
        HTTP/1.1 201 Created
        Content-type: application/json

        {
          "id": "1377cc08-eb23-ed11-88e7-f2834877f72d",
          "code": "OTTER",
          "displayName": "Otter cash receipts and payments",
          "balancingAccountId": "021c2ed0-021d-ed11-9db9-000d3aa935da",
          "balancingAccountNumber": "10700",
          "lastModifiedDateTime": "2022-08-24T20:26:30.03Z"
        }
        """

        path = '/companies(' + _path_value(company_id) + ')/vendorPaymentJournals'
        data = self._client.post(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
        )
        return _models.VendorPaymentJournal.model_validate(data)

    def delete(
        self,
        company_id: str,
        vendor_payment_journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> None:
        """Delete vendorPaymentJournals

        Deletes vendorPaymentJournal  in Dynamics 365 Business Central.

        HTTP method: DELETE
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpaymentjournal_delete
        Operation id: dynamics_vendorpaymentjournal_delete

        Example request:
        DELETE https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPaymentJournals...

        Example response:
        HTTP/1.1 204 No Content
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPaymentJournals('
            + _path_value(vendor_payment_journal_id)
            + ')'
        )
        return self._client.delete(path, query=query, params=params, etag=etag)

    def get(
        self,
        company_id: str,
        vendor_payment_journal_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.VendorPaymentJournal:
        """Get vendorPaymentJournals

        Gets a vendorPaymentJournal object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpaymentjournal_get
        Operation id: dynamics_vendorpaymentjournal_get
        Response model: VendorPaymentJournal

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPaymentJournals({id})

        Example response:
        {
          "id": "dbe826d6-021d-ed11-9db9-000d3aa935da",
          "code": "CASH",
          "displayName": "Cash receipts and payments",
          "balancingAccountId": "00000000-0000-0000-0000-000000000000",
          "balancingAccountNumber": "10100",
          "lastModifiedDateTime": "2022-08-16T01:29:56.15Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPaymentJournals('
            + _path_value(vendor_payment_journal_id)
            + ')'
        )
        data = self._client.get(path, query=query, params=params)
        return _models.VendorPaymentJournal.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.VendorPaymentJournal]:
        """List vendorPaymentJournals

        List vendorPaymentJournals objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpaymentjournal_get
        Operation id: dynamics_vendorpaymentjournal_list
        Response model: list[VendorPaymentJournal]
        """

        path = '/companies(' + _path_value(company_id) + ')/vendorPaymentJournals'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.VendorPaymentJournal.model_validate(item) for item in items]

    def update(
        self,
        company_id: str,
        vendor_payment_journal_id: str,
        body: _models.VendorPaymentJournalUpdate | Mapping[str, Any] | None = None,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        etag: str | None = None,
    ) -> _models.VendorPaymentJournal:
        """Update vendorPaymentJournals

        Updates a vendorPaymentJournal object in Dynamics 365 Business Central.

        HTTP method: PATCH
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpaymentjournal_update
        Operation id: dynamics_vendorpaymentjournal_update
        Request model: VendorPaymentJournalUpdate
        Response model: VendorPaymentJournal

        Example request:
        PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPaymentJournals(...
        Content-type: application/json

        {
          "code": "COMMON",
          "displayName": "COMMON"
        }

        Example response:
        HTTP/1.1 200 OK
        Content-type: application/json

        {
          "id": "1377cc08-eb23-ed11-88e7-f2834877f72d",
          "code": "COMMON",
          "displayName": "COMMON",
          "balancingAccountId": "021c2ed0-021d-ed11-9db9-000d3aa935da",
          "balancingAccountNumber": "10700",
          "lastModifiedDateTime": "2022-08-24T20:37:54.867Z"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPaymentJournals('
            + _path_value(vendor_payment_journal_id)
            + ')'
        )
        data = self._client.patch(
            path,
            json=_body_payload(body),
            query=query,
            params=params,
            etag=etag,
        )
        return _models.VendorPaymentJournal.model_validate(data)

class VendorPurchasesClient(_EntityClient):
    """Generated operations for ``vendor_purchases``."""

    def get(
        self,
        company_id: str,
        vendor_id: str,
        vendor_no: str,
        vendor_name: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> _models.VendorPurchase:
        """Get vendorPurchases

        Gets a vendorPurchase object in Dynamics 365 Business Central.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpurchase_get
        Operation id: dynamics_vendorpurchase_get
        Response model: VendorPurchase

        Example request:
        GET https://{businesscentralPrefix}/api/v2.0/companies({id})/vendorPurchases({vendorI...

        Example response:
        {
            "vendorId": "f7a5738a-44e3-ea11-bb43-000d3a2feca1",
            "vendorNumber": "10000",
            "name": "Fabrikam, Inc.",
            "totalPurchaseAmount": "32.0",
            "dateFilter_FilterOnly": "2020-08-21"
        }
        """

        path = (
            '/companies('
            + _path_value(company_id)
            + ')/vendorPurchases('
            + _path_value(vendor_id)
            + ", '"
            + _path_value(vendor_no)
            + "', '"
            + _path_value(vendor_name)
            + "')"
        )
        data = self._client.get(path, query=query, params=params)
        return _models.VendorPurchase.model_validate(data)

    def list(
        self,
        company_id: str,
        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> list[_models.VendorPurchase]:
        """List vendorPurchases

        List vendorPurchases objects.

        HTTP method: GET
        Docs: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_vendorpurchase_get
        Operation id: dynamics_vendorpurchase_list
        Response model: list[VendorPurchase]
        """

        path = '/companies(' + _path_value(company_id) + ')/vendorPurchases'
        items = self._client.get_value(path, query=query, params=params)
        return [_models.VendorPurchase.model_validate(item) for item in items]

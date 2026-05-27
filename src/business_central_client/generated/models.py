from __future__ import annotations

from datetime import date as Date
from datetime import datetime as DateTime
from decimal import Decimal
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class BusinessCentralModel(BaseModel):
    """Base model for generated Business Central schemas."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


class Account(BusinessCentralModel):
    """Generated schema for ``account`` (response)."""
    account_type: str | None = Field(None, alias="accountType")
    balance: Decimal | None = None
    blocked: bool | None = None
    category: str | None = None
    debit_credit_balance: str | None = Field(None, alias="debitCreditBalance")
    direct_posting: bool | None = Field(None, alias="directPosting")
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    income_balance: str | None = Field(None, alias="incomeBalance")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    net_change: Decimal | None = Field(None, alias="netChange")
    number: str | None = None
    sub_category: str | None = Field(None, alias="subCategory")
    total_balance: Decimal | None = Field(None, alias="totalBalance")

class AccountingPeriod(BusinessCentralModel):
    """Generated schema for ``accounting_period`` (response)."""
    closed: bool | None = None
    date_locked: Date | None = Field(None, alias="dateLocked")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    name: str | None = None
    new_fiscal_year: bool | None = Field(None, alias="newFiscalYear")
    starting_date: Date | None = Field(None, alias="startingDate")

class AgedAccountsPayable(BusinessCentralModel):
    """Generated schema for ``aged_accounts_payable`` (response)."""
    aged_as_of_date: Date | None = Field(None, alias="agedAsOfDate")
    balance_due: Decimal | None = Field(None, alias="balanceDue")
    currency_code: str | None = Field(None, alias="currencyCode")
    current_amount: int | None = Field(None, alias="currentAmount")
    name: str | None = None
    period1_amount: int | None = Field(None, alias="period1Amount")
    period2_amount: int | None = Field(None, alias="period2Amount")
    period3_amount: Decimal | None = Field(None, alias="period3Amount")
    period_length_filter: str | None = Field(None, alias="periodLengthFilter")
    vendor_id: UUID | None = Field(None, alias="vendorId")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class AgedAccountsReceivable(BusinessCentralModel):
    """Generated schema for ``aged_accounts_receivable`` (response)."""
    aged_as_of_date: Date | None = Field(None, alias="agedAsOfDate")
    balance_due: int | None = Field(None, alias="balanceDue")
    currency_code: str | None = Field(None, alias="currencyCode")
    current_amount: int | None = Field(None, alias="currentAmount")
    customer_id: UUID | None = Field(None, alias="customerId")
    customer_number: str | None = Field(None, alias="customerNumber")
    name: str | None = None
    period1_amount: int | None = Field(None, alias="period1Amount")
    period2_amount: int | None = Field(None, alias="period2Amount")
    period3_amount: int | None = Field(None, alias="period3Amount")
    period_length_filter: str | None = Field(None, alias="periodLengthFilter")

class ApplyVendorEntry(BusinessCentralModel):
    """Generated schema for ``apply_vendor_entry`` (response)."""
    applied: bool | None = None
    applies_to_id: UUID | None = Field(None, alias="appliesToId")
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    document_type: str | None = Field(None, alias="documentType")
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: UUID | None = None
    posting_date: Date | None = Field(None, alias="postingDate")
    remaining_amount: int | None = Field(None, alias="remainingAmount")
    vendor_name: str | None = Field(None, alias="vendorName")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class ApplyVendorEntryUpdate(BusinessCentralModel):
    """Generated schema for ``apply_vendor_entry`` (update)."""
    applied: bool | None = None
    id: UUID | None = None

class Attachment(BusinessCentralModel):
    """Generated schema for ``attachment`` (response)."""
    byte_size: int | None = Field(None, alias="byteSize")
    file_name: str | None = Field(None, alias="fileName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    parent_id: UUID | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")

class AttachmentContent(BusinessCentralModel):
    """Generated schema for ``attachment_content`` (response)."""
    attachment_content: str | None = Field(None, alias="attachmentContent")
    byte_size: int | None = Field(None, alias="byteSize")
    file_name: str | None = Field(None, alias="fileName")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    parent_id: str | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")

class AttachmentCreate(BusinessCentralModel):
    """Generated schema for ``attachment`` (create)."""
    file_name: str | None = Field(None, alias="fileName")
    parent_id: UUID | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")

class BalanceSheet(BusinessCentralModel):
    """Generated schema for ``balance_sheet`` (response)."""
    balance: int | None = None
    date_filter: Date | None = Field(None, alias="dateFilter")
    display: str | None = None
    id: UUID | None = None
    indentation: int | None = None
    line_number: int | None = Field(None, alias="lineNumber")
    line_type: str | None = Field(None, alias="lineType")

class BankAccount(BusinessCentralModel):
    """Generated schema for ``bank_account`` (response)."""
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    number: str | None = None

class BankAccountCreate(BusinessCentralModel):
    """Generated schema for ``bank_account`` (create)."""
    display_name: str | None = Field(None, alias="displayName")
    number: str | None = None

class BankAccountUpdate(BusinessCentralModel):
    """Generated schema for ``bank_account`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class CashFlowStatement(BusinessCentralModel):
    """Generated schema for ``cash_flow_statement`` (response)."""
    date_filter: Date | None = Field(None, alias="dateFilter")
    display: str | None = None
    id: UUID | None = None
    indentation: int | None = None
    line_number: int | None = Field(None, alias="lineNumber")
    line_type: str | None = Field(None, alias="lineType")
    net_change: int | None = Field(None, alias="netChange")

class Company(BusinessCentralModel):
    """Generated schema for ``company`` (response)."""
    business_profile_id: str | None = Field(None, alias="businessProfileId")
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    name: str | None = None
    system_created_at: DateTime | None = Field(None, alias="systemCreatedAt")
    system_created_by: UUID | None = Field(None, alias="systemCreatedBy")
    system_modified_at: DateTime | None = Field(None, alias="systemModifiedAt")
    system_modified_by: UUID | None = Field(None, alias="systemModifiedBy")
    system_version: str | None = Field(None, alias="systemVersion")
    timestamp: int | None = None

class CompanyInformation(BusinessCentralModel):
    """Generated schema for ``company_information`` (response)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    city: str | None = None
    country: str | None = None
    currency_code: str | None = Field(None, alias="currencyCode")
    current_fiscal_year_start_date: Date | None = Field(None, alias="currentFiscalYearStartDate")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    fax_number: str | None = Field(None, alias="faxNumber")
    id: UUID | None = None
    industry: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    phone_number: str | None = Field(None, alias="phoneNumber")
    picture_odata_media_read_link: str | None = Field(None, alias="picture@odata.mediaReadLink")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    tax_registration_number: str | None = Field(None, alias="taxRegistrationNumber")
    website: str | None = None

class CompanyInformationUpdate(BusinessCentralModel):
    """Generated schema for ``company_information`` (update)."""
    display_name: str | None = Field(None, alias="displayName")
    website: str | None = None

class Contact(BusinessCentralModel):
    """Generated schema for ``contact`` (response)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    city: str | None = None
    company_name: str | None = Field(None, alias="companyName")
    company_number: str | None = Field(None, alias="companyNumber")
    country: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    id: UUID | None = None
    last_interaction_date: Date | None = Field(None, alias="lastInteractionDate")
    last_modified_date_time: Date | None = Field(None, alias="lastModifiedDateTime")
    mobile_phone_number: str | None = Field(None, alias="mobilePhoneNumber")
    number: str | None = None
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    privacy_blocked: bool | None = Field(None, alias="privacyBlocked")
    search_name: str | None = Field(None, alias="searchName")
    state: str | None = None
    type: str | None = None
    website: str | None = None

class ContactCreate(BusinessCentralModel):
    """Generated schema for ``contact`` (create)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    city: str | None = None
    company_name: str | None = Field(None, alias="companyName")
    company_number: str | None = Field(None, alias="companyNumber")
    country: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    last_interaction_date: Date | None = Field(None, alias="lastInteractionDate")
    last_modified_date_time: Date | None = Field(None, alias="lastModifiedDateTime")
    mobile_phone_number: str | None = Field(None, alias="mobilePhoneNumber")
    number: str | None = None
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    privacy_blocked: bool | None = Field(None, alias="privacyBlocked")
    search_name: str | None = Field(None, alias="searchName")
    state: str | None = None
    type: str | None = None
    website: str | None = None

class ContactUpdate(BusinessCentralModel):
    """Generated schema for ``contact`` (update)."""
    id: UUID | None = None
    number: str | None = None

class ContactsInformation(BusinessCentralModel):
    """Generated schema for ``contacts_information`` (response)."""
    contact_id: UUID | None = Field(None, alias="contactId")
    contact_name: str | None = Field(None, alias="contactName")
    contact_number: str | None = Field(None, alias="contactNumber")
    contact_type: str | None = Field(None, alias="contactType")
    related_id: UUID | None = Field(None, alias="relatedId")
    related_type: str | None = Field(None, alias="relatedType")

class Content(BusinessCentralModel):
    """Generated schema for ``content`` (response)."""
    content_odata_media_read_link: str | None = Field(None, alias="content@odata.mediaReadLink")
    id: UUID | None = None
    odata_etag: str | None = Field(None, alias="@odata.etag")

class CountriesRegion(BusinessCentralModel):
    """Generated schema for ``countries_region`` (response)."""
    address_format: str | None = Field(None, alias="addressFormat")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class CountriesRegionCreate(BusinessCentralModel):
    """Generated schema for ``countries_region`` (create)."""
    address_format: str | None = Field(None, alias="addressFormat")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class CountriesRegionUpdate(BusinessCentralModel):
    """Generated schema for ``countries_region`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class Currency(BusinessCentralModel):
    """Generated schema for ``currency`` (response)."""
    amount_decimal_places: str | None = Field(None, alias="amountDecimalPlaces")
    amount_rounding_precision: Decimal | None = Field(None, alias="amountRoundingPrecision")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    symbol: str | None = None

class CurrencyCreate(BusinessCentralModel):
    """Generated schema for ``currency`` (create)."""
    amount_decimal_places: str | None = Field(None, alias="amountDecimalPlaces")
    amount_rounding_precision: Decimal | None = Field(None, alias="amountRoundingPrecision")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    symbol: str | None = None

class CurrencyExchangeRate(BusinessCentralModel):
    """Generated schema for ``currency_exchange_rate`` (response)."""
    currency_code: str | None = Field(None, alias="currencyCode")
    exchange_rate_amount: Decimal | None = Field(None, alias="exchangeRateAmount")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    relational_currency_code: str | None = Field(None, alias="relationalCurrencyCode")
    relational_exchange_rate_amount: Decimal | None = Field(
        None,
        alias="relationalExchangeRateAmount",
    )
    starting_date: Date | None = Field(None, alias="startingDate")

class CurrencyUpdate(BusinessCentralModel):
    """Generated schema for ``currency`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class Customer(BusinessCentralModel):
    """Generated schema for ``customer`` (response)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    blocked: str | None = None
    city: str | None = None
    country: str | None = None
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    shipment_method_id: UUID | None = Field(None, alias="shipmentMethodId")
    state: str | None = None
    tax_area_display_name: str | None = Field(None, alias="taxAreaDisplayName")
    tax_area_id: UUID | None = Field(None, alias="taxAreaId")
    tax_liable: bool | None = Field(None, alias="taxLiable")
    tax_registration_number: str | None = Field(None, alias="taxRegistrationNumber")
    type: str | None = None
    website: str | None = None

class CustomerContact(BusinessCentralModel):
    """Generated schema for ``customer_contact`` (response)."""
    customer_id: str | None = Field(None, alias="customerId")
    customer_name: str | None = Field(None, alias="customerName")
    email: str | None = None
    first_name: str | None = Field(None, alias="firstName")
    id: str | None = None
    last_name: str | None = Field(None, alias="lastName")
    primary_phone_number: str | None = Field(None, alias="primaryPhoneNumber")
    professional_title: str | None = Field(None, alias="professionalTitle")

class CustomerContactUpdate(BusinessCentralModel):
    """Generated schema for ``customer_contact`` (update)."""
    email: str | None = None
    id: str | None = None
    professional_title: str | None = Field(None, alias="professionalTitle")

class CustomerCreate(BusinessCentralModel):
    """Generated schema for ``customer`` (create)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    blocked: str | None = None
    city: str | None = None
    country: str | None = None
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    shipment_method_id: UUID | None = Field(None, alias="shipmentMethodId")
    state: str | None = None
    tax_area_id: UUID | None = Field(None, alias="taxAreaId")
    tax_liable: bool | None = Field(None, alias="taxLiable")
    tax_registration_number: str | None = Field(None, alias="taxRegistrationNumber")
    type: str | None = None
    website: str | None = None

class CustomerFinancialDetail(BusinessCentralModel):
    """Generated schema for ``customer_financial_detail`` (response)."""
    balance: int | None = None
    id: UUID | None = None
    number: str | None = None
    overdue_amount: int | None = Field(None, alias="overdueAmount")
    total_sales_excluding_tax: int | None = Field(None, alias="totalSalesExcludingTax")

class CustomerPayment(BusinessCentralModel):
    """Generated schema for ``customer_payment`` (response)."""
    amount: int | None = None
    applies_to_invoice_id: str | None = Field(None, alias="appliesToInvoiceId")
    applies_to_invoice_number: str | None = Field(None, alias="appliesToInvoiceNumber")
    comment: str | None = None
    contact_id: str | None = Field(None, alias="contactId")
    customer_id: str | None = Field(None, alias="customerId")
    customer_number: str | None = Field(None, alias="customerNumber")
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    line_number: int | None = Field(None, alias="lineNumber")
    posting_date: Date | None = Field(None, alias="postingDate")

class CustomerPaymentCreate(BusinessCentralModel):
    """Generated schema for ``customer_payment`` (create)."""
    amount: int | None = None
    applies_to_invoice_id: str | None = Field(None, alias="appliesToInvoiceId")
    applies_to_invoice_number: str | None = Field(None, alias="appliesToInvoiceNumber")
    comment: str | None = None
    contact_id: str | None = Field(None, alias="contactId")
    customer_id: str | None = Field(None, alias="customerId")
    customer_number: str | None = Field(None, alias="customerNumber")
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    line_number: int | None = Field(None, alias="lineNumber")
    posting_date: Date | None = Field(None, alias="postingDate")

class CustomerPaymentJournal(BusinessCentralModel):
    """Generated schema for ``customer_payment_journal`` (response)."""
    balancing_account_id: UUID | None = Field(None, alias="balancingAccountId")
    balancing_account_number: str | None = Field(None, alias="balancingAccountNumber")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class CustomerPaymentJournalCreate(BusinessCentralModel):
    """Generated schema for ``customer_payment_journal`` (create)."""
    balancing_account_id: UUID | None = Field(None, alias="balancingAccountId")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class CustomerPaymentJournalUpdate(BusinessCentralModel):
    """Generated schema for ``customer_payment_journal`` (update)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class CustomerPaymentUpdate(BusinessCentralModel):
    """Generated schema for ``customer_payment`` (update)."""
    amount: int | None = None

class CustomerReturnReason(BusinessCentralModel):
    """Generated schema for ``customer_return_reason`` (response)."""
    code: str | None = None
    description: str | None = None
    id: UUID | None = None

class CustomerReturnReasonCreate(BusinessCentralModel):
    """Generated schema for ``customer_return_reason`` (create)."""
    code: str | None = None
    description: str | None = None

class CustomerReturnReasonUpdate(BusinessCentralModel):
    """Generated schema for ``customer_return_reason`` (update)."""
    description: str | None = None

class CustomerSale(BusinessCentralModel):
    """Generated schema for ``customer_sale`` (response)."""
    customer_id: UUID | None = Field(None, alias="customerId")
    customer_number: str | None = Field(None, alias="customerNumber")
    date_filter_filter_only: Any | None = Field(None, alias="dateFilter_FilterOnly")
    name: str | None = None
    total_sales_amount: Decimal | None = Field(None, alias="totalSalesAmount")

class CustomerUpdate(BusinessCentralModel):
    """Generated schema for ``customer`` (update)."""
    display_name: str | None = Field(None, alias="displayName")
    phone_number: str | None = Field(None, alias="phoneNumber")

class DefaultDimension(BusinessCentralModel):
    """Generated schema for ``default_dimension`` (response)."""
    dimension_code: str | None = Field(None, alias="dimensionCode")
    dimension_id: UUID | None = Field(None, alias="dimensionId")
    dimension_value_code: str | None = Field(None, alias="dimensionValueCode")
    dimension_value_id: UUID | None = Field(None, alias="dimensionValueId")
    id: UUID | None = None
    odata_etag: str | None = Field(None, alias="@odata.etag")
    parent_id: UUID | None = Field(None, alias="parentId")
    posting_validation: str | None = Field(None, alias="postingValidation")

class Dimension(BusinessCentralModel):
    """Generated schema for ``dimension`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class DimensionSetLine(BusinessCentralModel):
    """Generated schema for ``dimension_set_line`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    parent_id: UUID | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")
    value_code: str | None = Field(None, alias="valueCode")
    value_display_name: str | None = Field(None, alias="valueDisplayName")
    value_id: UUID | None = Field(None, alias="valueId")

class DimensionSetLineCreate(BusinessCentralModel):
    """Generated schema for ``dimension_set_line`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    parent_id: UUID | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")
    value_code: str | None = Field(None, alias="valueCode")
    value_display_name: str | None = Field(None, alias="valueDisplayName")
    value_id: UUID | None = Field(None, alias="valueId")

class DimensionValue(BusinessCentralModel):
    """Generated schema for ``dimension_value`` (response)."""
    code: str | None = None
    dimension_id: UUID | None = Field(None, alias="dimensionId")
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class DisputeStatus(BusinessCentralModel):
    """Generated schema for ``dispute_status`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class DisputeStatusCreate(BusinessCentralModel):
    """Generated schema for ``dispute_status`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class DisputeStatusUpdate(BusinessCentralModel):
    """Generated schema for ``dispute_status`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class DocumentAttachment(BusinessCentralModel):
    """Generated schema for ``document_attachment`` (response)."""
    attachment_content: str | None = Field(None, alias="attachmentContent")
    byte_size: int | None = Field(None, alias="byteSize")
    document_flow_purchase: bool | None = Field(None, alias="documentFlowPurchase")
    document_flow_sales: bool | None = Field(None, alias="documentFlowSales")
    file_name: str | None = Field(None, alias="fileName")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    line_number: int | None = Field(None, alias="lineNumber")
    parent_id: str | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")

class DocumentAttachmentCreate(BusinessCentralModel):
    """Generated schema for ``document_attachment`` (create)."""
    attachment_content: str | None = Field(None, alias="attachmentContent")
    byte_size: int | None = Field(None, alias="byteSize")
    document_flow_purchase: bool | None = Field(None, alias="documentFlowPurchase")
    file_name: str | None = Field(None, alias="fileName")
    parent_id: str | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")

class DocumentAttachmentUpdate(BusinessCentralModel):
    """Generated schema for ``document_attachment`` (update)."""
    document_flow_sales: bool | None = Field(None, alias="documentFlowSales")
    file_name: str | None = Field(None, alias="fileName")

class Employee(BusinessCentralModel):
    """Generated schema for ``employee`` (response)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    birth_date: Date | None = Field(None, alias="birthDate")
    city: str | None = None
    country: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    employment_date: Date | None = Field(None, alias="employmentDate")
    given_name: str | None = Field(None, alias="givenName")
    id: UUID | None = None
    job_title: str | None = Field(None, alias="jobTitle")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    middle_name: str | None = Field(None, alias="middleName")
    mobile_phone: str | None = Field(None, alias="mobilePhone")
    number: str | None = None
    personal_email: str | None = Field(None, alias="personalEmail")
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    statistics_group_code: str | None = Field(None, alias="statisticsGroupCode")
    status: str | None = None
    surname: str | None = None
    termination_date: Date | None = Field(None, alias="terminationDate")

class EmployeeCreate(BusinessCentralModel):
    """Generated schema for ``employee`` (create)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    birth_date: Date | None = Field(None, alias="birthDate")
    city: str | None = None
    country: str | None = None
    email: str | None = None
    employment_date: Date | None = Field(None, alias="employmentDate")
    given_name: str | None = Field(None, alias="givenName")
    id: UUID | None = None
    job_title: str | None = Field(None, alias="jobTitle")
    middle_name: str | None = Field(None, alias="middleName")
    mobile_phone: str | None = Field(None, alias="mobilePhone")
    number: str | None = None
    personal_email: str | None = Field(None, alias="personalEmail")
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    statistics_group_code: str | None = Field(None, alias="statisticsGroupCode")
    status: str | None = None
    surname: str | None = None
    termination_date: Date | None = Field(None, alias="terminationDate")

class EmployeeUpdate(BusinessCentralModel):
    """Generated schema for ``employee`` (update)."""
    given_name: str | None = Field(None, alias="givenName")
    phone_number: str | None = Field(None, alias="phoneNumber")

class FixedAsset(BusinessCentralModel):
    """Generated schema for ``fixed_asset`` (response)."""
    acquisition_cost: Decimal | None = Field(None, alias="acquisitionCost")
    acquisition_date: Date | None = Field(None, alias="acquisitionDate")
    blocked: bool | None = None
    book_value: Decimal | None = Field(None, alias="bookValue")
    class_code: str | None = Field(None, alias="classCode")
    depreciation_method: str | None = Field(None, alias="depreciationMethod")
    depreciation_starting_date: Date | None = Field(None, alias="depreciationStartingDate")
    depreciation_years: int | None = Field(None, alias="depreciationYears")
    display_name: str | None = Field(None, alias="displayName")
    employee_id: UUID | None = Field(None, alias="employeeId")
    employee_number: str | None = Field(None, alias="employeeNumber")
    fixed_asset_location_code: str | None = Field(None, alias="fixedAssetLocationCode")
    fixed_asset_location_id: str | None = Field(None, alias="fixedAssetLocationId")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    serial_number: str | None = Field(None, alias="serialNumber")
    subclass_code: str | None = Field(None, alias="subclassCode")
    under_maintenance: bool | None = Field(None, alias="underMaintenance")

class FixedAssetCreate(BusinessCentralModel):
    """Generated schema for ``fixed_asset`` (create)."""
    blocked: bool | None = None
    class_code: str | None = Field(None, alias="classCode")
    display_name: str | None = Field(None, alias="displayName")
    employee_id: UUID | None = Field(None, alias="employeeId")
    employee_number: str | None = Field(None, alias="employeeNumber")
    fixed_asset_location_code: str | None = Field(None, alias="fixedAssetLocationCode")
    fixed_asset_location_id: str | None = Field(None, alias="fixedAssetLocationId")
    number: str | None = None
    serial_number: str | None = Field(None, alias="serialNumber")
    subclass_code: str | None = Field(None, alias="subclassCode")
    under_maintenance: bool | None = Field(None, alias="underMaintenance")

class FixedAssetLocation(BusinessCentralModel):
    """Generated schema for ``fixed_asset_location`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class FixedAssetLocationCreate(BusinessCentralModel):
    """Generated schema for ``fixed_asset_location`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class FixedAssetLocationUpdate(BusinessCentralModel):
    """Generated schema for ``fixed_asset_location`` (update)."""
    display_name: str | None = Field(None, alias="displayName")
    id: str | None = None

class FixedAssetUpdate(BusinessCentralModel):
    """Generated schema for ``fixed_asset`` (update)."""
    employee_id: UUID | None = Field(None, alias="employeeId")
    employee_number: str | None = Field(None, alias="employeeNumber")
    fixed_asset_location_code: str | None = Field(None, alias="fixedAssetLocationCode")
    fixed_asset_location_id: str | None = Field(None, alias="fixedAssetLocationId")
    id: str | None = None
    under_maintenance: bool | None = Field(None, alias="underMaintenance")

class GeneralLedgerEntry(BusinessCentralModel):
    """Generated schema for ``general_ledger_entry`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    account_number: str | None = Field(None, alias="accountNumber")
    credit_amount: Decimal | None = Field(None, alias="creditAmount")
    debit_amount: int | None = Field(None, alias="debitAmount")
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    document_type: str | None = Field(None, alias="documentType")
    entry_number: int | None = Field(None, alias="entryNumber")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    posting_date: Date | None = Field(None, alias="postingDate")

class GeneralLedgerSetup(BusinessCentralModel):
    """Generated schema for ``general_ledger_setup`` (response)."""
    additional_reporting_currency: str | None = Field(None, alias="additionalReportingCurrency")
    allow_posting_from: Date | None = Field(None, alias="allowPostingFrom")
    allow_posting_to: Date | None = Field(None, alias="allowPostingTo")
    allow_query_from_consolidation: bool | None = Field(None, alias="allowQueryFromConsolidation")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    local_currency_code: str | None = Field(None, alias="localCurrencyCode")
    local_currency_symbol: str | None = Field(None, alias="localCurrencySymbol")

class GeneralProductPostingGroup(BusinessCentralModel):
    """Generated schema for ``general_product_posting_group`` (response)."""
    auto_insert_default: bool | None = Field(None, alias="autoInsertDefault")
    code: str | None = None
    default_vat_product_posting_group: str | None = Field(
        None,
        alias="defaultVATProductPostingGroup",
    )
    description: str | None = None
    id: UUID | None = None
    odata_etag: str | None = Field(None, alias="@odata.etag")

class IncomeStatement(BusinessCentralModel):
    """Generated schema for ``income_statement`` (response)."""
    date_filter: Date | None = Field(None, alias="dateFilter")
    display: str | None = None
    id: UUID | None = None
    indentation: int | None = None
    line_number: int | None = Field(None, alias="lineNumber")
    line_type: str | None = Field(None, alias="lineType")
    net_change: int | None = Field(None, alias="netChange")

class InventoryPostingGroup(BusinessCentralModel):
    """Generated schema for ``inventory_posting_group`` (response)."""
    code: str | None = None
    description: str | None = None
    id: UUID | None = None
    odata_etag: str | None = Field(None, alias="@odata.etag")

class Item(BusinessCentralModel):
    """Generated schema for ``item`` (response)."""
    base_unit_of_measure_code: str | None = Field(None, alias="baseUnitOfMeasureCode")
    base_unit_of_measure_id: UUID | None = Field(None, alias="baseUnitOfMeasureId")
    blocked: bool | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_name2: str | None = Field(None, alias="displayName2")
    general_product_posting_group_code: str | None = Field(
        None,
        alias="generalProductPostingGroupCode",
    )
    general_product_posting_group_id: UUID | None = Field(
        None,
        alias="generalProductPostingGroupId",
    )
    gtin: str | None = None
    id: UUID | None = None
    inventory: int | None = None
    inventory_posting_group_code: str | None = Field(None, alias="inventoryPostingGroupCode")
    inventory_posting_group_id: UUID | None = Field(None, alias="inventoryPostingGroupId")
    item_category_code: str | None = Field(None, alias="itemCategoryCode")
    item_category_id: UUID | None = Field(None, alias="itemCategoryId")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    price_includes_tax: bool | None = Field(None, alias="priceIncludesTax")
    tax_group_code: str | None = Field(None, alias="taxGroupCode")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    type: str | None = None
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class ItemCategory(BusinessCentralModel):
    """Generated schema for ``item_category`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class ItemCategoryCreate(BusinessCentralModel):
    """Generated schema for ``item_category`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class ItemCategoryUpdate(BusinessCentralModel):
    """Generated schema for ``item_category`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class ItemCreate(BusinessCentralModel):
    """Generated schema for ``item`` (create)."""
    base_unit_of_measure_code: str | None = Field(None, alias="baseUnitOfMeasureCode")
    base_unit_of_measure_id: UUID | None = Field(None, alias="baseUnitOfMeasureId")
    blocked: bool | None = None
    display_name: str | None = Field(None, alias="displayName")
    gtin: str | None = None
    item_category_code: str | None = Field(None, alias="itemCategoryCode")
    item_category_id: UUID | None = Field(None, alias="itemCategoryId")
    number: str | None = None
    price_includes_tax: bool | None = Field(None, alias="priceIncludesTax")
    tax_group_code: str | None = Field(None, alias="taxGroupCode")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    type: str | None = None
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class ItemLedgerEntry(BusinessCentralModel):
    """Generated schema for ``item_ledger_entry`` (response)."""
    cost_amount_actual: Decimal | None = Field(None, alias="costAmountActual")
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    document_type: str | None = Field(None, alias="documentType")
    entry_number: int | None = Field(None, alias="entryNumber")
    entry_type: str | None = Field(None, alias="entryType")
    id: UUID | None = None
    item_number: str | None = Field(None, alias="itemNumber")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    odata_etag: str | None = Field(None, alias="@odata.etag")
    posting_date: Date | None = Field(None, alias="postingDate")
    quantity: int | None = None
    sales_amount_actual: int | None = Field(None, alias="salesAmountActual")
    source_number: str | None = Field(None, alias="sourceNumber")
    source_type: str | None = Field(None, alias="sourceType")

class ItemUpdate(BusinessCentralModel):
    """Generated schema for ``item`` (update)."""
    blocked: bool | None = None
    display_name: str | None = Field(None, alias="displayName")

class ItemVariant(BusinessCentralModel):
    """Generated schema for ``item_variant`` (response)."""
    code: str | None = None
    description: str | None = None
    id: UUID | None = None
    item_id: UUID | None = Field(None, alias="itemId")
    item_number: str | None = Field(None, alias="itemNumber")

class ItemVariantCreate(BusinessCentralModel):
    """Generated schema for ``item_variant`` (create)."""
    code: str | None = None
    description: str | None = None
    id: UUID | None = None
    item_id: UUID | None = Field(None, alias="itemId")
    item_number: str | None = Field(None, alias="itemNumber")

class ItemVariantUpdate(BusinessCentralModel):
    """Generated schema for ``item_variant`` (update)."""
    item_number: str | None = Field(None, alias="itemNumber")

class JobQueueEntry(BusinessCentralModel):
    """Generated schema for ``job_queue_entry`` (response)."""
    description: str | None = None
    earliest_start_date_time: DateTime | None = Field(None, alias="earliestStartDateTime")
    ending_time: str | None = Field(None, alias="endingTime")
    error_message: str | None = Field(None, alias="errorMessage")
    expiration_date_time: DateTime | None = Field(None, alias="expirationDateTime")
    id: UUID | None = None
    job_queue_category_code: str | None = Field(None, alias="jobQueueCategoryCode")
    job_queue_entry_id: str | None = Field(None, alias="jobQueueEntryId")
    job_time_out: int | None = Field(None, alias="jobTimeOut")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    last_ready_state: str | None = Field(None, alias="lastReadyState")
    manual_recurrence: bool | None = Field(None, alias="manualRecurrence")
    max_number_attempts_to_run: int | None = Field(None, alias="maxNumberAttemptsToRun")
    next_run_date_formula: str | None = Field(None, alias="nextRunDateFormula")
    notify_on_success: bool | None = Field(None, alias="notifyOnSuccess")
    number_of_attempts_to_run: int | None = Field(None, alias="numberOfAttemptsToRun")
    number_of_minutes_between_runs: int | None = Field(None, alias="numberOfMinutesBetweenRuns")
    object_caption_to_run: str | None = Field(None, alias="objectCaptionToRun")
    object_id_to_run: int | None = Field(None, alias="objectIdToRun")
    object_type_to_run: str | None = Field(None, alias="objectTypeToRun")
    parameter_string: str | None = Field(None, alias="parameterString")
    printer_name: str | None = Field(None, alias="printerName")
    priority_within_category: int | None = Field(None, alias="priorityWithinCategory")
    record_id_to_process: str | None = Field(None, alias="recordIdToProcess")
    recurring_job: bool | None = Field(None, alias="recurringJob")
    reference_starting_time: DateTime | None = Field(None, alias="referenceStartingTime")
    report_output_type: str | None = Field(None, alias="reportOutputType")
    report_request_page_options: str | None = Field(None, alias="reportRequestPageOptions")
    rerun_delay: int | None = Field(None, alias="rerunDelay")
    run_in_user_session: bool | None = Field(None, alias="runInUserSession")
    run_on_fridays: bool | None = Field(None, alias="runOnFridays")
    run_on_monday: bool | None = Field(None, alias="runOnMonday")
    run_on_saturdays: bool | None = Field(None, alias="runOnSaturdays")
    run_on_sundays: bool | None = Field(None, alias="runOnSundays")
    run_on_thursday: bool | None = Field(None, alias="runOnThursday")
    run_on_tuesday: bool | None = Field(None, alias="runOnTuesday")
    run_on_wednesday: bool | None = Field(None, alias="runOnWednesday")
    scheduled: bool | None = None
    starting_time: str | None = Field(None, alias="startingTime")
    status: str | None = None
    system_task_id: UUID | None = Field(None, alias="systemTaskId")
    user_id: UUID | None = Field(None, alias="userId")
    user_language_id: int | None = Field(None, alias="userLanguageId")
    user_service_instance_id: str | None = Field(None, alias="userServiceInstanceId")
    user_session_id: str | None = Field(None, alias="userSessionId")
    user_session_started: bool | None = Field(None, alias="userSessionStarted")

class JobQueueLogEntry(BusinessCentralModel):
    """Generated schema for ``job_queue_log_entry`` (response)."""
    description: str | None = None
    end_date_time: DateTime | None = Field(None, alias="endDateTime")
    error_call_stack: str | None = Field(None, alias="errorCallStack")
    error_message: str | None = Field(None, alias="errorMessage")
    id: UUID | None = None
    job_queue_category_code: str | None = Field(None, alias="jobQueueCategoryCode")
    job_queue_entry_id: str | None = Field(None, alias="jobQueueEntryId")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    object_id_to_run: int | None = Field(None, alias="objectIdToRun")
    object_type_to_run: str | None = Field(None, alias="objectTypeToRun")
    parameter_string: str | None = Field(None, alias="parameterString")
    start_date_time: DateTime | None = Field(None, alias="startDateTime")
    status: str | None = None
    system_task_id: UUID | None = Field(None, alias="systemTaskId")
    user_id: UUID | None = Field(None, alias="userId")
    user_service_instance_id: str | None = Field(None, alias="userServiceInstanceId")
    user_session_id: UUID | None = Field(None, alias="userSessionId")

class Journal(BusinessCentralModel):
    """Generated schema for ``journal`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class JournalCreate(BusinessCentralModel):
    """Generated schema for ``journal`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class JournalLine(BusinessCentralModel):
    """Generated schema for ``journal_line`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    account_number: str | None = Field(None, alias="accountNumber")
    account_type: str | None = Field(None, alias="accountType")
    amount: int | None = None
    balance_account_type: str | None = Field(None, alias="balanceAccountType")
    balancing_account_id: UUID | None = Field(None, alias="balancingAccountId")
    balancing_account_number: str | None = Field(None, alias="balancingAccountNumber")
    comment: str | None = None
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: UUID | None = None
    journal_display_name: str | None = Field(None, alias="journalDisplayName")
    journal_id: UUID | None = Field(None, alias="journalId")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    line_number: int | None = Field(None, alias="lineNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    tax_code: str | None = Field(None, alias="taxCode")

class JournalLineCreate(BusinessCentralModel):
    """Generated schema for ``journal_line`` (create)."""
    account_id: UUID | None = Field(None, alias="accountId")
    account_number: str | None = Field(None, alias="accountNumber")
    account_type: str | None = Field(None, alias="accountType")
    amount: int | None = None
    comment: str | None = None
    description: str | None = None
    document_number: str | None = Field(None, alias="documentNumber")
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: UUID | None = None
    journal_id: UUID | None = Field(None, alias="journalId")
    line_number: int | None = Field(None, alias="lineNumber")
    posting_date: Date | None = Field(None, alias="postingDate")

class JournalLineUpdate(BusinessCentralModel):
    """Generated schema for ``journal_line`` (update)."""
    amount: int | None = None

class JournalUpdate(BusinessCentralModel):
    """Generated schema for ``journal`` (update)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class Location(BusinessCentralModel):
    """Generated schema for ``location`` (response)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    city: str | None = None
    code: str | None = None
    contact: str | None = None
    country: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    id: UUID | None = None
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    website: str | None = None

class LocationCreate(BusinessCentralModel):
    """Generated schema for ``location`` (create)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    city: str | None = None
    code: str | None = None
    contact: str | None = None
    country: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    id: UUID | None = None
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    website: str | None = None

class LocationUpdate(BusinessCentralModel):
    """Generated schema for ``location`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class Opportunity(BusinessCentralModel):
    """Generated schema for ``opportunity`` (response)."""
    calculated_current_value: int | None = Field(None, alias="calculatedCurrentValue")
    chances_of_success_prc: int | None = Field(None, alias="chancesOfSuccessPrc")
    closed: bool | None = None
    completed_prc: int | None = Field(None, alias="completedPrc")
    contact_company_name: str | None = Field(None, alias="contactCompanyName")
    contact_name: str | None = Field(None, alias="contactName")
    contact_number: str | None = Field(None, alias="contactNumber")
    creation_date: Date | None = Field(None, alias="creationDate")
    date_closed: Date | None = Field(None, alias="dateClosed")
    description: str | None = None
    estimated_closing_date: Date | None = Field(None, alias="estimatedClosingDate")
    estimated_value: int | None = Field(None, alias="estimatedValue")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    odata_etag: str | None = Field(None, alias="@odata.etag")
    salesperson_code: str | None = Field(None, alias="salespersonCode")
    status: str | None = None
    system_created_at: DateTime | None = Field(None, alias="systemCreatedAt")

class OpportunityCreate(BusinessCentralModel):
    """Generated schema for ``opportunity`` (create)."""
    contact_number: str | None = Field(None, alias="contactNumber")
    description: str | None = None
    number: str | None = None
    salesperson_code: str | None = Field(None, alias="salespersonCode")

class OpportunityUpdate(BusinessCentralModel):
    """Generated schema for ``opportunity`` (update)."""
    description: str | None = None
    salesperson_code: str | None = Field(None, alias="salespersonCode")

class PaymentMethod(BusinessCentralModel):
    """Generated schema for ``payment_method`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class PaymentMethodCreate(BusinessCentralModel):
    """Generated schema for ``payment_method`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None

class PaymentMethodUpdate(BusinessCentralModel):
    """Generated schema for ``payment_method`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class PaymentTerm(BusinessCentralModel):
    """Generated schema for ``payment_term`` (response)."""
    calculate_discount_on_credit_memos: bool | None = Field(
        None,
        alias="calculateDiscountOnCreditMemos",
    )
    code: str | None = None
    discount_date_calculation: str | None = Field(None, alias="discountDateCalculation")
    discount_percent: int | None = Field(None, alias="discountPercent")
    display_name: str | None = Field(None, alias="displayName")
    due_date_calculation: str | None = Field(None, alias="dueDateCalculation")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class PaymentTermCreate(BusinessCentralModel):
    """Generated schema for ``payment_term`` (create)."""
    calculate_discount_on_credit_memos: bool | None = Field(
        None,
        alias="calculateDiscountOnCreditMemos",
    )
    code: str | None = None
    discount_date_calculation: str | None = Field(None, alias="discountDateCalculation")
    discount_percent: int | None = Field(None, alias="discountPercent")
    display_name: str | None = Field(None, alias="displayName")
    due_date_calculation: str | None = Field(None, alias="dueDateCalculation")

class PaymentTermUpdate(BusinessCentralModel):
    """Generated schema for ``payment_term`` (update)."""
    discount_percent: int | None = Field(None, alias="discountPercent")
    display_name: str | None = Field(None, alias="displayName")

class PdfDocument(BusinessCentralModel):
    """Generated schema for ``pdf_document`` (response)."""
    id: UUID | None = None
    parent_id: UUID | None = Field(None, alias="parentId")
    parent_type: str | None = Field(None, alias="parentType")
    pdf_document_content_odata_media_read_link: str | None = Field(
        None,
        alias="pdfDocumentContent@odata.mediaReadLink",
    )

class Picture(BusinessCentralModel):
    """Generated schema for ``picture`` (response)."""
    content_type: str | None = Field(None, alias="contentType")
    height: int | None = None
    id: UUID | None = None
    parent_type: str | None = Field(None, alias="parentType")
    picture_content_odata_media_edit_link: str | None = Field(
        None,
        alias="pictureContent@odata.mediaEditLink",
    )
    picture_content_odata_media_read_link: str | None = Field(
        None,
        alias="pictureContent@odata.mediaReadLink",
    )
    width: int | None = None

class Project(BusinessCentralModel):
    """Generated schema for ``project`` (response)."""
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    number: str | None = None

class ProjectCreate(BusinessCentralModel):
    """Generated schema for ``project`` (create)."""
    display_name: str | None = Field(None, alias="displayName")
    number: str | None = None

class ProjectUpdate(BusinessCentralModel):
    """Generated schema for ``project`` (update)."""
    number: str | None = None

class PurchaseCreditMemo(BusinessCentralModel):
    """Generated schema for ``purchase_credit_memo`` (response)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    credit_memo_date: Date | None = Field(None, alias="creditMemoDate")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    discount_amount: Decimal | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    id: UUID | None = None
    invoice_id: UUID | None = Field(None, alias="invoiceId")
    invoice_number: str | None = Field(None, alias="invoiceNumber")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    pay_to_address_line1: str | None = Field(None, alias="payToAddressLine1")
    pay_to_address_line2: str | None = Field(None, alias="payToAddressLine2")
    pay_to_city: str | None = Field(None, alias="payToCity")
    pay_to_country: str | None = Field(None, alias="payToCountry")
    pay_to_name: str | None = Field(None, alias="payToName")
    pay_to_post_code: str | None = Field(None, alias="payToPostCode")
    pay_to_state: str | None = Field(None, alias="payToState")
    pay_to_vendor_id: UUID | None = Field(None, alias="payToVendorId")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    purchaser: str | None = None
    shipment_method_id: UUID | None = Field(None, alias="shipmentMethodId")
    shortcut_dimension1_code: str | None = Field(None, alias="shortcutDimension1Code")
    shortcut_dimension2_code: str | None = Field(None, alias="shortcutDimension2Code")
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    vendor_id: UUID | None = Field(None, alias="vendorId")
    vendor_name: str | None = Field(None, alias="vendorName")
    vendor_number: str | None = Field(None, alias="vendorNumber")
    vendor_return_reason_id: UUID | None = Field(None, alias="vendorReturnReasonId")

class PurchaseCreditMemoCreate(BusinessCentralModel):
    """Generated schema for ``purchase_credit_memo`` (create)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    credit_memo_date: Date | None = Field(None, alias="creditMemoDate")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: str | None = Field(None, alias="currencyId")
    discount_amount: Decimal | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    invoice_id: str | None = Field(None, alias="invoiceId")
    invoice_number: str | None = Field(None, alias="invoiceNumber")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    pay_to_address_line1: str | None = Field(None, alias="payToAddressLine1")
    pay_to_address_line2: str | None = Field(None, alias="payToAddressLine2")
    pay_to_city: str | None = Field(None, alias="payToCity")
    pay_to_country: str | None = Field(None, alias="payToCountry")
    pay_to_name: str | None = Field(None, alias="payToName")
    pay_to_post_code: str | None = Field(None, alias="payToPostCode")
    pay_to_state: str | None = Field(None, alias="payToState")
    pay_to_vendor_id: str | None = Field(None, alias="payToVendorId")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    payment_terms_id: str | None = Field(None, alias="paymentTermsId")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    purchaser: str | None = None
    shipment_method_id: str | None = Field(None, alias="shipmentMethodId")
    shortcut_dimension1_code: str | None = Field(None, alias="shortcutDimension1Code")
    shortcut_dimension2_code: str | None = Field(None, alias="shortcutDimension2Code")
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    vendor_id: str | None = Field(None, alias="vendorId")
    vendor_name: str | None = Field(None, alias="vendorName")
    vendor_number: str | None = Field(None, alias="vendorNumber")
    vendor_return_reason_id: str | None = Field(None, alias="vendorReturnReasonId")

class PurchaseCreditMemoLine(BusinessCentralModel):
    """Generated schema for ``purchase_credit_memo_line`` (response)."""
    account_id: str | None = Field(None, alias="accountId")
    amount_excluding_tax: Decimal | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: Decimal | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None
    invoice_discount_allocation: Decimal | None = Field(None, alias="invoiceDiscountAllocation")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: str | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: int | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")

class PurchaseCreditMemoLineCreate(BusinessCentralModel):
    """Generated schema for ``purchase_credit_memo_line`` (create)."""
    description: str | None = None
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    quantity: int | None = None
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")

class PurchaseCreditMemoLineUpdate(BusinessCentralModel):
    """Generated schema for ``purchase_credit_memo_line`` (update)."""
    id: UUID | None = None
    quantity: int | None = None

class PurchaseCreditMemoUpdate(BusinessCentralModel):
    """Generated schema for ``purchase_credit_memo`` (update)."""
    id: UUID | None = None
    number: str | None = None

class PurchaseInvoice(BusinessCentralModel):
    """Generated schema for ``purchase_invoice`` (response)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    id: UUID | None = None
    invoice_date: Date | None = Field(None, alias="invoiceDate")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    order_id: UUID | None = Field(None, alias="orderId")
    order_number: str | None = Field(None, alias="orderNumber")
    pay_to_address_line1: str | None = Field(None, alias="payToAddressLine1")
    pay_to_address_line2: str | None = Field(None, alias="payToAddressLine2")
    pay_to_city: str | None = Field(None, alias="payToCity")
    pay_to_contact: str | None = Field(None, alias="payToContact")
    pay_to_country: str | None = Field(None, alias="payToCountry")
    pay_to_name: str | None = Field(None, alias="payToName")
    pay_to_post_code: str | None = Field(None, alias="payToPostCode")
    pay_to_state: str | None = Field(None, alias="payToState")
    pay_to_vendor_id: UUID | None = Field(None, alias="payToVendorId")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    shortcut_dimension1_code: str | None = Field(None, alias="shortcutDimension1Code")
    shortcut_dimension2_code: str | None = Field(None, alias="shortcutDimension2Code")
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    vendor_id: UUID | None = Field(None, alias="vendorId")
    vendor_invoice_number: str | None = Field(None, alias="vendorInvoiceNumber")
    vendor_name: str | None = Field(None, alias="vendorName")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class PurchaseInvoiceCreate(BusinessCentralModel):
    """Generated schema for ``purchase_invoice`` (create)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    invoice_date: Date | None = Field(None, alias="invoiceDate")
    pay_to_vendor_id: UUID | None = Field(None, alias="payToVendorId")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    vendor_id: UUID | None = Field(None, alias="vendorId")
    vendor_invoice_number: str | None = Field(None, alias="vendorInvoiceNumber")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class PurchaseInvoiceLine(BusinessCentralModel):
    """Generated schema for ``purchase_invoice_line`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: int | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: int | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    expected_receipt_date: Date | None = Field(None, alias="expectedReceiptDate")
    id: UUID | None = None
    invoice_discount_allocation: int | None = Field(None, alias="invoiceDiscountAllocation")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: Decimal | None = Field(None, alias="taxPercent")
    total_tax_amount: int | None = Field(None, alias="totalTaxAmount")
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")

class PurchaseInvoiceLineCreate(BusinessCentralModel):
    """Generated schema for ``purchase_invoice_line`` (create)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: int | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: int | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    expected_receipt_date: Date | None = Field(None, alias="expectedReceiptDate")
    id: UUID | None = None
    invoice_discount_allocation: int | None = Field(None, alias="invoiceDiscountAllocation")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")

class PurchaseInvoiceLineUpdate(BusinessCentralModel):
    """Generated schema for ``purchase_invoice_line`` (update)."""
    quantity: int | None = None

class PurchaseInvoiceUpdate(BusinessCentralModel):
    """Generated schema for ``purchase_invoice`` (update)."""
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class PurchaseOrder(BusinessCentralModel):
    """Generated schema for ``purchase_order`` (response)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    fully_received: bool | None = Field(None, alias="fullyReceived")
    id: UUID | None = None
    last_modified_date_time: Date | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    order_date: Date | None = Field(None, alias="orderDate")
    pay_to_address_line1: str | None = Field(None, alias="payToAddressLine1")
    pay_to_address_line2: str | None = Field(None, alias="payToAddressLine2")
    pay_to_city: str | None = Field(None, alias="payToCity")
    pay_to_country: str | None = Field(None, alias="payToCountry")
    pay_to_name: str | None = Field(None, alias="payToName")
    pay_to_post_code: str | None = Field(None, alias="payToPostCode")
    pay_to_state: str | None = Field(None, alias="payToState")
    pay_to_vendor_id: str | None = Field(None, alias="payToVendorId")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    purchaser: str | None = None
    requested_receipt_date: Date | None = Field(None, alias="requestedReceiptDate")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    shipment_method_id: str | None = Field(None, alias="shipmentMethodId")
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    vendor_id: str | None = Field(None, alias="vendorId")
    vendor_name: str | None = Field(None, alias="vendorName")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class PurchaseOrderCreate(BusinessCentralModel):
    """Generated schema for ``purchase_order`` (create)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    discount_amount: int | None = Field(None, alias="discountAmount")
    due_date: Date | None = Field(None, alias="dueDate")
    order_date: Date | None = Field(None, alias="orderDate")
    pay_to_vendor_id: str | None = Field(None, alias="payToVendorId")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    purchaser: str | None = None
    requested_receipt_date: Date | None = Field(None, alias="requestedReceiptDate")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    shipment_method_id: str | None = Field(None, alias="shipmentMethodId")
    vendor_id: str | None = Field(None, alias="vendorId")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class PurchaseOrderLine(BusinessCentralModel):
    """Generated schema for ``purchase_order_line`` (response)."""
    account_id: str | None = Field(None, alias="accountId")
    amount_excluding_tax: Decimal | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    direct_unit_cost: Decimal | None = Field(None, alias="directUnitCost")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    expected_receipt_date: Date | None = Field(None, alias="expectedReceiptDate")
    id: UUID | None = None
    invoice_discount_allocation: int | None = Field(None, alias="invoiceDiscountAllocation")
    invoice_quantity: int | None = Field(None, alias="invoiceQuantity")
    invoiced_quantity: int | None = Field(None, alias="invoicedQuantity")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    receive_quantity: int | None = Field(None, alias="receiveQuantity")
    received_quantity: int | None = Field(None, alias="receivedQuantity")
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: Decimal | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")

class PurchaseOrderLineCreate(BusinessCentralModel):
    """Generated schema for ``purchase_order_line`` (create)."""
    account_id: str | None = Field(None, alias="accountId")
    description: str | None = None
    direct_unit_cost: Decimal | None = Field(None, alias="directUnitCost")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    expected_receipt_date: Date | None = Field(None, alias="expectedReceiptDate")
    id: UUID | None = None
    invoice_quantity: int | None = Field(None, alias="invoiceQuantity")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    quantity: int | None = None
    receive_quantity: int | None = Field(None, alias="receiveQuantity")
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")

class PurchaseOrderLineUpdate(BusinessCentralModel):
    """Generated schema for ``purchase_order_line`` (update)."""
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None

class PurchaseOrderUpdate(BusinessCentralModel):
    """Generated schema for ``purchase_order`` (update)."""
    id: UUID | None = None
    number: str | None = None

class PurchaseReceipt(BusinessCentralModel):
    """Generated schema for ``purchase_receipt`` (response)."""
    buy_from_address_line1: str | None = Field(None, alias="buyFromAddressLine1")
    buy_from_address_line2: str | None = Field(None, alias="buyFromAddressLine2")
    buy_from_city: str | None = Field(None, alias="buyFromCity")
    buy_from_country: str | None = Field(None, alias="buyFromCountry")
    buy_from_post_code: str | None = Field(None, alias="buyFromPostCode")
    buy_from_state: str | None = Field(None, alias="buyFromState")
    currency_code: str | None = Field(None, alias="currencyCode")
    due_date: Date | None = Field(None, alias="dueDate")
    id: UUID | None = None
    invoice_date: Date | None = Field(None, alias="invoiceDate")
    last_modified_date_time: Date | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    pay_to_address_line1: str | None = Field(None, alias="payToAddressLine1")
    pay_to_address_line2: str | None = Field(None, alias="payToAddressLine2")
    pay_to_city: str | None = Field(None, alias="payToCity")
    pay_to_contact: str | None = Field(None, alias="payToContact")
    pay_to_country: str | None = Field(None, alias="payToCountry")
    pay_to_name: str | None = Field(None, alias="payToName")
    pay_to_post_code: str | None = Field(None, alias="payToPostCode")
    pay_to_state: str | None = Field(None, alias="payToState")
    pay_to_vendor_number: str | None = Field(None, alias="payToVendorNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    vendor_name: str | None = Field(None, alias="vendorName")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class PurchaseReceiptLine(BusinessCentralModel):
    """Generated schema for ``purchase_receipt_line`` (response)."""
    description: str | None = None
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    expected_receipt_date: Date | None = Field(None, alias="expectedReceiptDate")
    id: UUID | None = None
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    quantity: int | None = None
    sequence: str | None = None
    tax_percent: int | None = Field(None, alias="taxPercent")
    unit_cost: Decimal | None = Field(None, alias="unitCost")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")

class RetainedEarningsStatement(BusinessCentralModel):
    """Generated schema for ``retained_earnings_statement`` (response)."""
    date_filter: Date | None = Field(None, alias="dateFilter")
    display: str | None = None
    id: UUID | None = None
    indentation: int | None = None
    line_number: int | None = Field(None, alias="lineNumber")
    line_type: str | None = Field(None, alias="lineType")
    net_change: Decimal | None = Field(None, alias="netChange")

class SalesCreditMemo(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo`` (response)."""
    billing_postal_address: SalesCreditMemoBillingPostalAddress | None = Field(
        None,
        alias="billingPostalAddress",
    )
    contact_id: str | None = Field(None, alias="contactId")
    credit_memo_date: Date | None = Field(None, alias="creditMemoDate")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: str | None = Field(None, alias="currencyId")
    customer_id: str | None = Field(None, alias="customerId")
    customer_name: str | None = Field(None, alias="customerName")
    customer_number: str | None = Field(None, alias="customerNumber")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    id: str | None = None
    invoice_id: str | None = Field(None, alias="invoiceId")
    invoice_number: str | None = Field(None, alias="invoiceNumber")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    salesperson: str | None = None
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")

class SalesCreditMemoBillingPostalAddress(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo`` (response)."""
    city: str | None = None
    country_letter_code: str | None = Field(None, alias="countryLetterCode")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    street: str | None = None

class SalesCreditMemoCreate(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo`` (create)."""
    credit_memo_date: Date | None = Field(None, alias="creditMemoDate")
    currency_code: str | None = Field(None, alias="currencyCode")
    customer_number: str | None = Field(None, alias="customerNumber")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesCreditMemoLine(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo_line`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: Decimal | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None
    invoice_discount_allocation: int | None = Field(None, alias="invoiceDiscountAllocation")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: Decimal | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesCreditMemoLineCreate(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo_line`` (create)."""
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_percent: int | None = Field(None, alias="discountPercent")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    quantity: int | None = None
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    tax_code: str | None = Field(None, alias="taxCode")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesCreditMemoLineUpdate(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo_line`` (update)."""
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesCreditMemoUpdate(BusinessCentralModel):
    """Generated schema for ``sales_credit_memo`` (update)."""
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesInvoice(BusinessCentralModel):
    """Generated schema for ``sales_invoice`` (response)."""
    bill_to_address_line1: str | None = Field(None, alias="billToAddressLine1")
    bill_to_address_line2: str | None = Field(None, alias="billToAddressLine2")
    bill_to_city: str | None = Field(None, alias="billToCity")
    bill_to_country: str | None = Field(None, alias="billToCountry")
    bill_to_customer_id: UUID | None = Field(None, alias="billToCustomerId")
    bill_to_customer_number: str | None = Field(None, alias="billToCustomerNumber")
    bill_to_name: str | None = Field(None, alias="billToName")
    bill_to_post_code: str | None = Field(None, alias="billToPostCode")
    bill_to_state: str | None = Field(None, alias="billToState")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    customer_id: UUID | None = Field(None, alias="customerId")
    customer_name: str | None = Field(None, alias="customerName")
    customer_number: str | None = Field(None, alias="customerNumber")
    customer_purchase_order_reference: str | None = Field(
        None,
        alias="customerPurchaseOrderReference",
    )
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    due_date: Date | None = Field(None, alias="dueDate")
    email: str | None = None
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: UUID | None = None
    invoice_date: Date | None = Field(None, alias="invoiceDate")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    order_id: UUID | None = Field(None, alias="orderId")
    order_number: str | None = Field(None, alias="orderNumber")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    remaining_amount: int | None = Field(None, alias="remainingAmount")
    salesperson: str | None = None
    sell_to_address_line1: str | None = Field(None, alias="sellToAddressLine1")
    sell_to_address_line2: str | None = Field(None, alias="sellToAddressLine2")
    sell_to_city: str | None = Field(None, alias="sellToCity")
    sell_to_country: str | None = Field(None, alias="sellToCountry")
    sell_to_post_code: str | None = Field(None, alias="sellToPostCode")
    sell_to_state: str | None = Field(None, alias="sellToState")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    shipment_method_id: UUID | None = Field(None, alias="shipmentMethodId")
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")

class SalesInvoiceCreate(BusinessCentralModel):
    """Generated schema for ``sales_invoice`` (create)."""
    bill_to_customer_id: UUID | None = Field(None, alias="billToCustomerId")
    bill_to_customer_number: str | None = Field(None, alias="billToCustomerNumber")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    customer_id: UUID | None = Field(None, alias="customerId")
    customer_name: str | None = Field(None, alias="customerName")
    customer_number: str | None = Field(None, alias="customerNumber")
    customer_purchase_order_reference: str | None = Field(
        None,
        alias="customerPurchaseOrderReference",
    )
    discount_amount: int | None = Field(None, alias="discountAmount")
    due_date: Date | None = Field(None, alias="dueDate")
    email: str | None = None
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    invoice_date: Date | None = Field(None, alias="invoiceDate")
    number: str | None = None
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    salesperson: str | None = None
    sell_to_address_line1: str | None = Field(None, alias="sellToAddressLine1")
    sell_to_address_line2: str | None = Field(None, alias="sellToAddressLine2")
    sell_to_city: str | None = Field(None, alias="sellToCity")
    sell_to_country: str | None = Field(None, alias="sellToCountry")
    sell_to_post_code: str | None = Field(None, alias="sellToPostCode")
    sell_to_state: str | None = Field(None, alias="sellToState")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    shipment_method_id: UUID | None = Field(None, alias="shipmentMethodId")

class SalesInvoiceLine(BusinessCentralModel):
    """Generated schema for ``sales_invoice_line`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: Decimal | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None
    invoice_discount_allocation: int | None = Field(None, alias="invoiceDiscountAllocation")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: int | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesInvoiceLineCreate(BusinessCentralModel):
    """Generated schema for ``sales_invoice_line`` (create)."""
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_percent: int | None = Field(None, alias="discountPercent")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    quantity: int | None = None
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    tax_code: str | None = Field(None, alias="taxCode")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesInvoiceLineUpdate(BusinessCentralModel):
    """Generated schema for ``sales_invoice_line`` (update)."""
    discount_amount: int | None = Field(None, alias="discountAmount")

class SalesInvoiceUpdate(BusinessCentralModel):
    """Generated schema for ``sales_invoice`` (update)."""
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesOrder(BusinessCentralModel):
    """Generated schema for ``sales_order`` (response)."""
    bill_to_address_line1: str | None = Field(None, alias="billToAddressLine1")
    bill_to_address_line2: str | None = Field(None, alias="billToAddressLine2")
    bill_to_city: str | None = Field(None, alias="billToCity")
    bill_to_country: str | None = Field(None, alias="billToCountry")
    bill_to_customer_id: UUID | None = Field(None, alias="billToCustomerId")
    bill_to_customer_number: str | None = Field(None, alias="billToCustomerNumber")
    bill_to_name: str | None = Field(None, alias="billToName")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    customer_id: UUID | None = Field(None, alias="customerId")
    customer_name: str | None = Field(None, alias="customerName")
    customer_number: str | None = Field(None, alias="customerNumber")
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    document_lines: list[SalesOrderDocumentLines] | None = Field(None, alias="documentLines")
    email: str | None = None
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    fully_shipped: bool | None = Field(None, alias="fullyShipped")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    order_date: Date | None = Field(None, alias="orderDate")
    partial_shipping: bool | None = Field(None, alias="partialShipping")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    requested_delivery_date: Date | None = Field(None, alias="requestedDeliveryDate")
    salesperson: str | None = None
    sell_to_address_line1: str | None = Field(None, alias="sellToAddressLine1")
    sell_to_city: str | None = Field(None, alias="sellToCity")
    sell_to_country: str | None = Field(None, alias="sellToCountry")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    shipment_method_id: UUID | None = Field(None, alias="shipmentMethodId")
    shortcut_dimension1_code: str | None = Field(None, alias="shortcutDimension1Code")
    shortcut_dimension2_code: str | None = Field(None, alias="shortcutDimension2Code")
    status: str | None = None
    total_amount_excluding_tax: int | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: int | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: int | None = Field(None, alias="totalTaxAmount")

class SalesOrderCreate(BusinessCentralModel):
    """Generated schema for ``sales_order`` (create)."""
    currency_code: str | None = Field(None, alias="currencyCode")
    customer_number: str | None = Field(None, alias="customerNumber")
    order_date: Date | None = Field(None, alias="orderDate")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesOrderDocumentLines(BusinessCentralModel):
    """Generated schema for ``sales_order`` (response)."""
    item_no: str | None = Field(None, alias="itemNo")
    line_no: int | None = Field(None, alias="lineNo")
    line_type: str | None = Field(None, alias="lineType")
    quantity: int | None = None
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")

class SalesOrderLine(BusinessCentralModel):
    """Generated schema for ``sales_order_line`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: Decimal | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None
    invoice_discount_allocation: int | None = Field(None, alias="invoiceDiscountAllocation")
    invoice_quantity: int | None = Field(None, alias="invoiceQuantity")
    invoiced_quantity: int | None = Field(None, alias="invoicedQuantity")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    net_amount: Decimal | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    ship_quantity: int | None = Field(None, alias="shipQuantity")
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    shipped_quantity: int | None = Field(None, alias="shippedQuantity")
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: Decimal | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesOrderLineCreate(BusinessCentralModel):
    """Generated schema for ``sales_order_line`` (create)."""
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_percent: int | None = Field(None, alias="discountPercent")
    invoice_quantity: int | None = Field(None, alias="invoiceQuantity")
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    location_id: UUID | None = Field(None, alias="locationId")
    quantity: int | None = None
    ship_quantity: int | None = Field(None, alias="shipQuantity")
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    tax_code: str | None = Field(None, alias="taxCode")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesOrderLineUpdate(BusinessCentralModel):
    """Generated schema for ``sales_order_line`` (update)."""
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesOrderUpdate(BusinessCentralModel):
    """Generated schema for ``sales_order`` (update)."""
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesQuote(BusinessCentralModel):
    """Generated schema for ``sales_quote`` (response)."""
    accepted_date: Date | None = Field(None, alias="acceptedDate")
    billing_postal_address: SalesQuoteBillingPostalAddress | None = Field(
        None,
        alias="billingPostalAddress",
    )
    contact_id: str | None = Field(None, alias="contactId")
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: str | None = Field(None, alias="currencyId")
    customer_id: str | None = Field(None, alias="customerId")
    customer_name: str | None = Field(None, alias="customerName")
    customer_number: str | None = Field(None, alias="customerNumber")
    discount_amount: int | None = Field(None, alias="discountAmount")
    document_date: Date | None = Field(None, alias="documentDate")
    due_date: Date | None = Field(None, alias="dueDate")
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: str | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    salesperson: str | None = None
    sent_date: DateTime | None = Field(None, alias="sentDate")
    shipment_method: str | None = Field(None, alias="shipmentMethod")
    shipment_method_id: str | None = Field(None, alias="shipmentMethodId")
    status: str | None = None
    total_amount_excluding_tax: Decimal | None = Field(None, alias="totalAmountExcludingTax")
    total_amount_including_tax: Decimal | None = Field(None, alias="totalAmountIncludingTax")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    valid_until_date: Date | None = Field(None, alias="validUntilDate")

class SalesQuoteBillingPostalAddress(BusinessCentralModel):
    """Generated schema for ``sales_quote`` (response)."""
    city: str | None = None
    country_letter_code: str | None = Field(None, alias="countryLetterCode")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    street: str | None = None

class SalesQuoteCreate(BusinessCentralModel):
    """Generated schema for ``sales_quote`` (create)."""
    currency_code: str | None = Field(None, alias="currencyCode")
    customer_number: str | None = Field(None, alias="customerNumber")
    document_date: Date | None = Field(None, alias="documentDate")
    id: str | None = None
    number: str | None = None
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesQuoteLine(BusinessCentralModel):
    """Generated schema for ``sales_quote_line`` (response)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: int | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    net_amount: int | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: int | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesQuoteLineCreate(BusinessCentralModel):
    """Generated schema for ``sales_quote_line`` (create)."""
    account_id: UUID | None = Field(None, alias="accountId")
    amount_excluding_tax: int | None = Field(None, alias="amountExcludingTax")
    amount_including_tax: Decimal | None = Field(None, alias="amountIncludingTax")
    description: str | None = None
    discount_amount: int | None = Field(None, alias="discountAmount")
    discount_applied_before_tax: bool | None = Field(None, alias="discountAppliedBeforeTax")
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    id: UUID | None = None
    item_id: UUID | None = Field(None, alias="itemId")
    item_variant_id: UUID | None = Field(None, alias="itemVariantId")
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    net_amount: int | None = Field(None, alias="netAmount")
    net_amount_including_tax: Decimal | None = Field(None, alias="netAmountIncludingTax")
    net_tax_amount: Decimal | None = Field(None, alias="netTaxAmount")
    quantity: int | None = None
    sequence: int | None = None
    tax_code: str | None = Field(None, alias="taxCode")
    tax_percent: int | None = Field(None, alias="taxPercent")
    total_tax_amount: Decimal | None = Field(None, alias="totalTaxAmount")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalesQuoteLineUpdate(BusinessCentralModel):
    """Generated schema for ``sales_quote_line`` (update)."""
    line_type: str | None = Field(None, alias="lineType")

class SalesQuoteUpdate(BusinessCentralModel):
    """Generated schema for ``sales_quote`` (update)."""
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")

class SalesShipment(BusinessCentralModel):
    """Generated schema for ``sales_shipment`` (response)."""
    bill_to_address_line1: str | None = Field(None, alias="billToAddressLine1")
    bill_to_address_line2: str | None = Field(None, alias="billToAddressLine2")
    bill_to_city: str | None = Field(None, alias="billToCity")
    bill_to_country: str | None = Field(None, alias="billToCountry")
    bill_to_customer_number: str | None = Field(None, alias="billToCustomerNumber")
    bill_to_name: str | None = Field(None, alias="billToName")
    bill_to_post_code: str | None = Field(None, alias="billToPostCode")
    bill_to_state: str | None = Field(None, alias="billToState")
    currency_code: str | None = Field(None, alias="currencyCode")
    customer_name: str | None = Field(None, alias="customerName")
    customer_number: str | None = Field(None, alias="customerNumber")
    customer_purchase_order_reference: str | None = Field(
        None,
        alias="customerPurchaseOrderReference",
    )
    due_date: Date | None = Field(None, alias="dueDate")
    email: str | None = None
    external_document_number: str | None = Field(None, alias="externalDocumentNumber")
    id: str | None = None
    invoice_date: Date | None = Field(None, alias="invoiceDate")
    last_modified_date_time: Date | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    order_number: str | None = Field(None, alias="orderNumber")
    payment_terms_code: str | None = Field(None, alias="paymentTermsCode")
    phone_number: str | None = Field(None, alias="phoneNumber")
    posting_date: Date | None = Field(None, alias="postingDate")
    prices_include_tax: bool | None = Field(None, alias="pricesIncludeTax")
    salesperson: str | None = None
    sell_to_address_line1: str | None = Field(None, alias="sellToAddressLine1")
    sell_to_address_line2: str | None = Field(None, alias="sellToAddressLine2")
    sell_to_city: str | None = Field(None, alias="sellToCity")
    sell_to_country: str | None = Field(None, alias="sellToCountry")
    sell_to_post_code: str | None = Field(None, alias="sellToPostCode")
    sell_to_state: str | None = Field(None, alias="sellToState")
    ship_to_address_line1: str | None = Field(None, alias="shipToAddressLine1")
    ship_to_address_line2: str | None = Field(None, alias="shipToAddressLine2")
    ship_to_city: str | None = Field(None, alias="shipToCity")
    ship_to_contact: str | None = Field(None, alias="shipToContact")
    ship_to_country: str | None = Field(None, alias="shipToCountry")
    ship_to_name: str | None = Field(None, alias="shipToName")
    ship_to_post_code: str | None = Field(None, alias="shipToPostCode")
    ship_to_state: str | None = Field(None, alias="shipToState")
    shipment_method_code: str | None = Field(None, alias="shipmentMethodCode")

class SalesShipmentLine(BusinessCentralModel):
    """Generated schema for ``sales_shipment_line`` (response)."""
    description: str | None = None
    discount_percent: int | None = Field(None, alias="discountPercent")
    document_id: UUID | None = Field(None, alias="documentId")
    document_no: str | None = Field(None, alias="documentNo")
    id: UUID | None = None
    line_object_number: str | None = Field(None, alias="lineObjectNumber")
    line_type: str | None = Field(None, alias="lineType")
    quantity: int | None = None
    sequence: int | None = None
    shipment_date: Date | None = Field(None, alias="shipmentDate")
    tax_percent: int | None = Field(None, alias="taxPercent")
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_price: Decimal | None = Field(None, alias="unitPrice")

class SalespeoplePurchaser(BusinessCentralModel):
    """Generated schema for ``salespeople_purchaser`` (response)."""
    blocked: bool | None = None
    code: str | None = None
    commision_percent: Decimal | None = Field(None, alias="commisionPercent")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    email2: str | None = None
    id: UUID | None = None
    job_title: str | None = Field(None, alias="jobTitle")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    phone_no: str | None = Field(None, alias="phoneNo")
    privacy_blocked: bool | None = Field(None, alias="privacyBlocked")

class SalespeoplePurchaserCreate(BusinessCentralModel):
    """Generated schema for ``salespeople_purchaser`` (create)."""
    blocked: bool | None = None
    code: str | None = None
    commision_percent: Decimal | None = Field(None, alias="commisionPercent")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    email2: str | None = None
    job_title: str | None = Field(None, alias="jobTitle")
    phone_no: str | None = Field(None, alias="phoneNo")
    privacy_blocked: bool | None = Field(None, alias="privacyBlocked")

class SalespeoplePurchaserUpdate(BusinessCentralModel):
    """Generated schema for ``salespeople_purchaser`` (update)."""
    commision_percent: Decimal | None = Field(None, alias="commisionPercent")
    id: UUID | None = None
    job_title: str | None = Field(None, alias="jobTitle")
    phone_no: str | None = Field(None, alias="phoneNo")

class ShipmentMethod(BusinessCentralModel):
    """Generated schema for ``shipment_method`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: Any | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class ShipmentMethodCreate(BusinessCentralModel):
    """Generated schema for ``shipment_method`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class ShipmentMethodUpdate(BusinessCentralModel):
    """Generated schema for ``shipment_method`` (update)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class Subscription(BusinessCentralModel):
    """Generated schema for ``subscription`` (response)."""
    client_state: str | None = Field(None, alias="clientState")
    expiration_date_time: DateTime | None = Field(None, alias="expirationDateTime")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    notification_url: str | None = Field(None, alias="notificationUrl")
    resource: str | None = None
    subscription_id: UUID | None = Field(None, alias="subscriptionId")
    system_created_at: DateTime | None = Field(None, alias="systemCreatedAt")
    system_created_by: UUID | None = Field(None, alias="systemCreatedBy")
    system_modified_at: DateTime | None = Field(None, alias="systemModifiedAt")
    system_modified_by: UUID | None = Field(None, alias="systemModifiedBy")
    user_id: UUID | None = Field(None, alias="userId")

class SubscriptionCreate(BusinessCentralModel):
    """Generated schema for ``subscription`` (create)."""
    client_state: str | None = Field(None, alias="clientState")
    expiration_date_time: DateTime | None = Field(None, alias="expirationDateTime")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    notification_url: str | None = Field(None, alias="notificationUrl")
    resource: str | None = None
    subscription_id: UUID | None = Field(None, alias="subscriptionId")
    system_created_at: DateTime | None = Field(None, alias="systemCreatedAt")
    system_created_by: UUID | None = Field(None, alias="systemCreatedBy")
    system_modified_at: DateTime | None = Field(None, alias="systemModifiedAt")
    system_modified_by: UUID | None = Field(None, alias="systemModifiedBy")
    user_id: UUID | None = Field(None, alias="userId")

class TaxArea(BusinessCentralModel):
    """Generated schema for ``tax_area`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    tax_type: str | None = Field(None, alias="taxType")

class TaxAreaCreate(BusinessCentralModel):
    """Generated schema for ``tax_area`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class TaxGroup(BusinessCentralModel):
    """Generated schema for ``tax_group`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    tax_type: str | None = Field(None, alias="taxType")

class TaxGroupCreate(BusinessCentralModel):
    """Generated schema for ``tax_group`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class TaxGroupUpdate(BusinessCentralModel):
    """Generated schema for ``tax_group`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class TimeRegistrationEntry(BusinessCentralModel):
    """Generated schema for ``time_registration_entry`` (response)."""
    absence: str | None = None
    date: Date | None = None
    employee_id: UUID | None = Field(None, alias="employeeId")
    employee_number: str | None = Field(None, alias="employeeNumber")
    id: UUID | None = None
    job_id: UUID | None = Field(None, alias="jobId")
    job_number: str | None = Field(None, alias="jobNumber")
    job_task_number: str | None = Field(None, alias="jobTaskNumber")
    last_modfied_date_time: DateTime | None = Field(None, alias="lastModfiedDateTime")
    line_number: int | None = Field(None, alias="lineNumber")
    quantity: int | None = None
    status: str | None = None
    unit_of_measure_code: str | None = Field(None, alias="unitOfMeasureCode")
    unit_of_measure_id: UUID | None = Field(None, alias="unitOfMeasureId")

class TimeRegistrationEntryCreate(BusinessCentralModel):
    """Generated schema for ``time_registration_entry`` (create)."""
    date: Date | None = None
    employee_id: UUID | None = Field(None, alias="employeeId")
    employee_number: str | None = Field(None, alias="employeeNumber")
    job_id: UUID | None = Field(None, alias="jobId")
    job_number: str | None = Field(None, alias="jobNumber")
    job_task_number: str | None = Field(None, alias="jobTaskNumber")
    quantity: int | None = None

class TimeRegistrationEntryUpdate(BusinessCentralModel):
    """Generated schema for ``time_registration_entry`` (update)."""
    quantity: int | None = None

class TrialBalance(BusinessCentralModel):
    """Generated schema for ``trial_balance`` (response)."""
    balance_at_date_credit: str | None = Field(None, alias="balanceAtDateCredit")
    balance_at_date_debit: str | None = Field(None, alias="balanceAtDateDebit")
    date_filter: Date | None = Field(None, alias="dateFilter")
    display: str | None = None
    number: str | None = None
    total_credit: str | None = Field(None, alias="totalCredit")
    total_debit: str | None = Field(None, alias="totalDebit")

class UnitsOfMeasure(BusinessCentralModel):
    """Generated schema for ``units_of_measure`` (response)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    international_standard_code: str | None = Field(None, alias="internationalStandardCode")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    symbol: str | None = None

class UnitsOfMeasureCreate(BusinessCentralModel):
    """Generated schema for ``units_of_measure`` (create)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    international_standard_code: str | None = Field(None, alias="internationalStandardCode")
    symbol: str | None = None

class UnitsOfMeasureUpdate(BusinessCentralModel):
    """Generated schema for ``units_of_measure`` (update)."""
    display_name: str | None = Field(None, alias="displayName")

class Vendor(BusinessCentralModel):
    """Generated schema for ``vendor`` (response)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    balance: Decimal | None = None
    blocked: str | None = None
    city: str | None = None
    country: str | None = None
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    id: UUID | None = None
    irs1099_code: str | None = Field(None, alias="irs1099Code")
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")
    number: str | None = None
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    tax_liable: bool | None = Field(None, alias="taxLiable")
    tax_registration_number: str | None = Field(None, alias="taxRegistrationNumber")
    website: str | None = None

class VendorCreate(BusinessCentralModel):
    """Generated schema for ``vendor`` (create)."""
    address_line1: str | None = Field(None, alias="addressLine1")
    address_line2: str | None = Field(None, alias="addressLine2")
    blocked: str | None = None
    city: str | None = None
    country: str | None = None
    currency_code: str | None = Field(None, alias="currencyCode")
    currency_id: UUID | None = Field(None, alias="currencyId")
    display_name: str | None = Field(None, alias="displayName")
    email: str | None = None
    id: UUID | None = None
    irs1099_code: str | None = Field(None, alias="irs1099Code")
    number: str | None = None
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    payment_terms_id: UUID | None = Field(None, alias="paymentTermsId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    postal_code: str | None = Field(None, alias="postalCode")
    state: str | None = None
    tax_liable: bool | None = Field(None, alias="taxLiable")
    tax_registration_number: str | None = Field(None, alias="taxRegistrationNumber")
    website: str | None = None

class VendorPaymentJournal(BusinessCentralModel):
    """Generated schema for ``vendor_payment_journal`` (response)."""
    balancing_account_id: UUID | None = Field(None, alias="balancingAccountId")
    balancing_account_number: str | None = Field(None, alias="balancingAccountNumber")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    id: UUID | None = None
    last_modified_date_time: DateTime | None = Field(None, alias="lastModifiedDateTime")

class VendorPaymentJournalCreate(BusinessCentralModel):
    """Generated schema for ``vendor_payment_journal`` (create)."""
    balancing_account_id: UUID | None = Field(None, alias="balancingAccountId")
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class VendorPaymentJournalUpdate(BusinessCentralModel):
    """Generated schema for ``vendor_payment_journal`` (update)."""
    code: str | None = None
    display_name: str | None = Field(None, alias="displayName")

class VendorPurchase(BusinessCentralModel):
    """Generated schema for ``vendor_purchase`` (response)."""
    date_filter_filter_only: Date | None = Field(None, alias="dateFilter_FilterOnly")
    name: str | None = None
    total_purchase_amount: str | None = Field(None, alias="totalPurchaseAmount")
    vendor_id: UUID | None = Field(None, alias="vendorId")
    vendor_number: str | None = Field(None, alias="vendorNumber")

class VendorUpdate(BusinessCentralModel):
    """Generated schema for ``vendor`` (update)."""
    blocked: str | None = None
    display_name: str | None = Field(None, alias="displayName")

__all__ = [
    "BusinessCentralModel",
    "Account",
    "AccountingPeriod",
    "AgedAccountsPayable",
    "AgedAccountsReceivable",
    "ApplyVendorEntry",
    "ApplyVendorEntryUpdate",
    "Attachment",
    "AttachmentContent",
    "AttachmentCreate",
    "BalanceSheet",
    "BankAccount",
    "BankAccountCreate",
    "BankAccountUpdate",
    "CashFlowStatement",
    "Company",
    "CompanyInformation",
    "CompanyInformationUpdate",
    "Contact",
    "ContactCreate",
    "ContactUpdate",
    "ContactsInformation",
    "Content",
    "CountriesRegion",
    "CountriesRegionCreate",
    "CountriesRegionUpdate",
    "Currency",
    "CurrencyCreate",
    "CurrencyExchangeRate",
    "CurrencyUpdate",
    "Customer",
    "CustomerContact",
    "CustomerContactUpdate",
    "CustomerCreate",
    "CustomerFinancialDetail",
    "CustomerPayment",
    "CustomerPaymentCreate",
    "CustomerPaymentJournal",
    "CustomerPaymentJournalCreate",
    "CustomerPaymentJournalUpdate",
    "CustomerPaymentUpdate",
    "CustomerReturnReason",
    "CustomerReturnReasonCreate",
    "CustomerReturnReasonUpdate",
    "CustomerSale",
    "CustomerUpdate",
    "DefaultDimension",
    "Dimension",
    "DimensionSetLine",
    "DimensionSetLineCreate",
    "DimensionValue",
    "DisputeStatus",
    "DisputeStatusCreate",
    "DisputeStatusUpdate",
    "DocumentAttachment",
    "DocumentAttachmentCreate",
    "DocumentAttachmentUpdate",
    "Employee",
    "EmployeeCreate",
    "EmployeeUpdate",
    "FixedAsset",
    "FixedAssetCreate",
    "FixedAssetLocation",
    "FixedAssetLocationCreate",
    "FixedAssetLocationUpdate",
    "FixedAssetUpdate",
    "GeneralLedgerEntry",
    "GeneralLedgerSetup",
    "GeneralProductPostingGroup",
    "IncomeStatement",
    "InventoryPostingGroup",
    "Item",
    "ItemCategory",
    "ItemCategoryCreate",
    "ItemCategoryUpdate",
    "ItemCreate",
    "ItemLedgerEntry",
    "ItemUpdate",
    "ItemVariant",
    "ItemVariantCreate",
    "ItemVariantUpdate",
    "JobQueueEntry",
    "JobQueueLogEntry",
    "Journal",
    "JournalCreate",
    "JournalLine",
    "JournalLineCreate",
    "JournalLineUpdate",
    "JournalUpdate",
    "Location",
    "LocationCreate",
    "LocationUpdate",
    "Opportunity",
    "OpportunityCreate",
    "OpportunityUpdate",
    "PaymentMethod",
    "PaymentMethodCreate",
    "PaymentMethodUpdate",
    "PaymentTerm",
    "PaymentTermCreate",
    "PaymentTermUpdate",
    "PdfDocument",
    "Picture",
    "Project",
    "ProjectCreate",
    "ProjectUpdate",
    "PurchaseCreditMemo",
    "PurchaseCreditMemoCreate",
    "PurchaseCreditMemoLine",
    "PurchaseCreditMemoLineCreate",
    "PurchaseCreditMemoLineUpdate",
    "PurchaseCreditMemoUpdate",
    "PurchaseInvoice",
    "PurchaseInvoiceCreate",
    "PurchaseInvoiceLine",
    "PurchaseInvoiceLineCreate",
    "PurchaseInvoiceLineUpdate",
    "PurchaseInvoiceUpdate",
    "PurchaseOrder",
    "PurchaseOrderCreate",
    "PurchaseOrderLine",
    "PurchaseOrderLineCreate",
    "PurchaseOrderLineUpdate",
    "PurchaseOrderUpdate",
    "PurchaseReceipt",
    "PurchaseReceiptLine",
    "RetainedEarningsStatement",
    "SalesCreditMemo",
    "SalesCreditMemoBillingPostalAddress",
    "SalesCreditMemoCreate",
    "SalesCreditMemoLine",
    "SalesCreditMemoLineCreate",
    "SalesCreditMemoLineUpdate",
    "SalesCreditMemoUpdate",
    "SalesInvoice",
    "SalesInvoiceCreate",
    "SalesInvoiceLine",
    "SalesInvoiceLineCreate",
    "SalesInvoiceLineUpdate",
    "SalesInvoiceUpdate",
    "SalesOrder",
    "SalesOrderCreate",
    "SalesOrderDocumentLines",
    "SalesOrderLine",
    "SalesOrderLineCreate",
    "SalesOrderLineUpdate",
    "SalesOrderUpdate",
    "SalesQuote",
    "SalesQuoteBillingPostalAddress",
    "SalesQuoteCreate",
    "SalesQuoteLine",
    "SalesQuoteLineCreate",
    "SalesQuoteLineUpdate",
    "SalesQuoteUpdate",
    "SalesShipment",
    "SalesShipmentLine",
    "SalespeoplePurchaser",
    "SalespeoplePurchaserCreate",
    "SalespeoplePurchaserUpdate",
    "ShipmentMethod",
    "ShipmentMethodCreate",
    "ShipmentMethodUpdate",
    "Subscription",
    "SubscriptionCreate",
    "TaxArea",
    "TaxAreaCreate",
    "TaxGroup",
    "TaxGroupCreate",
    "TaxGroupUpdate",
    "TimeRegistrationEntry",
    "TimeRegistrationEntryCreate",
    "TimeRegistrationEntryUpdate",
    "TrialBalance",
    "UnitsOfMeasure",
    "UnitsOfMeasureCreate",
    "UnitsOfMeasureUpdate",
    "Vendor",
    "VendorCreate",
    "VendorPaymentJournal",
    "VendorPaymentJournalCreate",
    "VendorPaymentJournalUpdate",
    "VendorPurchase",
    "VendorUpdate",
]

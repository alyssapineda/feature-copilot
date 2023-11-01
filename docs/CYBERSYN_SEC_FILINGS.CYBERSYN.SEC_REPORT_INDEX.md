**Table 19: CYBERSYN_SEC_FILINGS.CYBERSYN.SEC_REPORT_INDEX** (U.S. Securities and Exchange Commission (SEC) Report Index Data)

This table contains information related to information that tracks and indexes the filings made by various business entities with the SEC. It captures key information about the filings, including the filing entity's unique identifiers, filing details, and acceptance timestamps

- EIN: Varchar (16777216) - Employee Identification Number, 9 digit identification number assigned by the Internal Revenue Service to business entities operating in the United States. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - Name of registrant. This corresponds to the name of the legal entity as recorded in EDGAR as of the filing date. (Nullable: YES)

- FISCAL_PERIOD: Varchar (16777216) - Fiscal Period (e.g., Q1, Q2, Q3, FY). (Nullable: YES)

- ADSH: Varchar (16777216) - Accession Number assigned to each filing in the EDGAR system. Unique identifier for each individual filing. The Accession number can be used to track all records from a single filing. (Nullable: YES)

- FISCAL_YEAR: Varchar (16777216) - Fiscal Year Focus. (Nullable: YES)

- FORM_TYPE: Varchar (16777216) - The submission type of the filing. (Nullable: YES)

- FILED_DATE: Date - Date of the TIMESTAMP_ACCEPTED column. If the filing was submitted after 5:30 PM, the filed_date is the next business day. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)

- TIMESTAMP_ACCEPTED: Date - The acceptance date and time of the filing with the SEC. Filings accepted after 5:30pm EST are considered filed on the following business day. (Nullable: YES)


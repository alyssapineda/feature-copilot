**Table 60: SEC_FILINGS.CYBERSYN.SEC_FISCAL_CALENDARS** (SEC_FISCAL_CALENDARS)

Company fiscal calendars by quarter, including period start and end dates, identified by unique Central Index Key (CIK) numbers.

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the Commission to each registrant that submits filings. (Nullable: YES)

- DAYS_IN_PERIOD: Number (10, 0) - The # of days in the Fiscal Period Focus. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - Name of registrant. This corresponds to the name of the legal entity as recorded in EDGAR as of the filing date. (Nullable: YES)

- PERIOD_START_DATE: Date - The Fiscal Period Start Date. (Nullable: YES)

- FISCAL_PERIOD: Varchar (16777216) - Fiscal Period (e.g., Q1, Q2, Q3, FY). (Nullable: YES)

- FISCAL_YEAR: Varchar (16777216) - Fiscal Year Focus. (Nullable: YES)

- PERIOD_END_DATE: Date - The Fiscal Period End Date. (Nullable: YES)


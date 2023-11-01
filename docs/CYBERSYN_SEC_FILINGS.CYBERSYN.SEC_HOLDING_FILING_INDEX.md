**Table 17: CYBERSYN_SEC_FILINGS.CYBERSYN.SEC_HOLDING_FILING_INDEX** (U.S. Securities and Exchange Commission (SEC) Holding Filing Index Data)

This table contains information related to filings and reports made with the U.S. Securities and Exchange Commission (SEC), specifically related to holdings and investments.

- ADDITIONAL_INFORMATION: Varchar (16777216) - Additional information the filer has opted to include in the report. (Nullable: YES)

- REPORTING_PERIOD_QUARTER: Number (2, 0) - Calendar quarter for this reporting period. (Nullable: YES)

- SUBMISSION_TYPE: Varchar (16777216) - Type of submission for this filing. One of 13F-HR(/A) to denote a holdings report (or its amendment), or 13F-NT(/A) to denote a notice report (or its amendment). (Nullable: YES)

- NUMBER_OF_HOLDINGS: Varchar (16777216) - Number of holdings included in this report. (Nullable: YES)

- TOTAL_HOLDING_VALUE: Varchar (16777216) - Aggregate value of the holdings in this report. (Nullable: YES)

- FILING_DATE: Date - Filing date with with SEC. (Nullable: YES)

- FILING_MANAGER_NAME: Varchar (16777216) - Filing manager's name. (Nullable: YES)

- ADSH: Varchar (16777216) - Unique accession number for the filing. Can be used to join to the sec_holding_filing_attributes table. (Nullable: YES)

- REPORTING_PERIOD_YEAR: Number (4, 0) - Calendary year for this reporting period. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)


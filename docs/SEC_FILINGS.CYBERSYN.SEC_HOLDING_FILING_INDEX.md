**Table 62: SEC_FILINGS.CYBERSYN.SEC_HOLDING_FILING_INDEX** (SEC_HOLDING_FILING_INDEX)

Report index for Form 13-F, a disclosure of equity holdings by institutional investment managers with over $100 million in assets under management, provided on a quarterly basis by the SEC.The SEC assigns a unique number, Central Index Key (CIK), to all entities (companies, individuals, and foreign governments) who file disclosures with the SEC. A filing is assigned a unique identifier called an ADSH, or Accession Number. The Report entity represents individual filings with the SEC. Provides a wide format overview of an SEC filing (13F fund holding reports) by ADSH with associated CIK and OpenFIGI IDs.

- REPORTING_PERIOD_YEAR: Number (4, 0) - Calendar year for this reporting period. (Nullable: YES)

- FILING_DATE: Date - Filing date with with SEC. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)

- FILING_MANAGER_NAME: Varchar (16777216) - Filing manager's name. (Nullable: YES)

- ADDITIONAL_INFORMATION: Varchar (16777216) - Additional information the filer has opted to include in the report. (Nullable: YES)

- SUBMISSION_TYPE: Varchar (16777216) - Type of submission for this filing. One of 13F-HR(/A) to denote a holdings report (or its amendment), or 13F-NT(/A) to denote a notice report (or its amendment). (Nullable: YES)

- REPORTING_PERIOD_QUARTER: Number (2, 0) - Calendar quarter for this reporting period. (Nullable: YES)

- ADSH: Varchar (16777216) - Unique accession number for the filing. Can be used to join to the sec_holding_filing_attributes table. (Nullable: YES)

- TOTAL_HOLDING_VALUE: Varchar (16777216) - Aggregate value of the holdings in this report. (Nullable: YES)

- NUMBER_OF_HOLDINGS: Varchar (16777216) - Number of holdings included in this report. (Nullable: YES)


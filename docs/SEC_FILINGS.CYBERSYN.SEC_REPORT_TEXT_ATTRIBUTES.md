**Table 65: SEC_FILINGS.CYBERSYN.SEC_REPORT_TEXT_ATTRIBUTES** (SEC_REPORT_TEXT_ATTRIBUTES)

Provides full text of company filings (10-Ks, 10-Qs, 8-Ks) submitted to the SEC, with unique identifiers for each document.Provides a wide format breakdown of each SEC document submission by SEC_DOCUMENT_ID and ADSH.Each row represents a report's full text. The SEC_DOCUMENT_ID is a unique document identifier. An ADSH can have multiple documents associated with it.

- ADSH: Varchar (16777216) - Accession Number assigned to each filing in the EDGAR system. Unique identifier for each individual filing. The Accession number can be used to track all records from a single filing. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for the variable. (Nullable: YES)

- SEC_DOCUMENT_ID: Varchar (16777216) - Unique identifier based on a concatenation of the ADSH and document type. (Nullable: YES)

- VALUE: Varchar (16777216) - The raw text output from the filing including management discussion and analysis, key risk factors, etc. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for each measure. (Nullable: YES)

- PERIOD_END_DATE: Date - Last day of the quarter or fiscal filing period related to the text. (Nullable: YES)


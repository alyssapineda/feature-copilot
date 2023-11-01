**Table 20: CYBERSYN_SEC_FILINGS.CYBERSYN.SEC_REPORT_TEXT_ATTRIBUTES** (Security Report Text Attributes Data)

This table contains information related to information that captures textual attributes and content from SEC reports and filings. It provides information related to the raw text content, including details about the reporting period, variable identification, and the entities involved in the filings.

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for the variable. (Nullable: YES)

- PERIOD_END_DATE: Date - Last day of the quarter or fiscal filing period related to the text. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for each measure. (Nullable: YES)

- VALUE: Varchar (16777216) - The raw text output from the filing including management discussion and analysis, key risk factors, etc. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)

- SEC_DOCUMENT_ID: Varchar (16777216) - Unique identifier based on a concatention of the ADSH and document type. (Nullable: YES)

- ADSH: Varchar (16777216) - Accession Number assigned to each filing in the EDGAR system. Unique identifier for each individual filing. The Accession number can be used to track all records from a single filing. (Nullable: YES)


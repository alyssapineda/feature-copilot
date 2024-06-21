**Table 63: SEC_FILINGS.CYBERSYN.SEC_REPORT_ATTRIBUTES** (SEC_REPORT_ATTRIBUTES)

Company KPIs published in SEC filings using XBRL format, provided on a monthly basis.Provides a wide format breakdown of variables included within an SEC report by ADSH and SIK.This table provides the parsed XBRL line items from financial statements by a unique variable ID, which are associated with a particular report. This includes detailed metadata, tags, measure descriptions, unit of measurement, associated values, report IDs, statement types, and date details.

- PERIOD_START_DATE: Date - Period start date of the value. For point-in-time values such as balance sheet items, this is the same as the period_end_date. (Nullable: YES)

- TAG: Varchar (16777216) - Unique name of the variable or measurement that pertains to the value. (Nullable: YES)

- VALUE: Varchar (16777216) - The value. This is not scaled, it is as found in the Interactive Data file, but is rounded to four digits to the right of the decimal point. (Nullable: YES)

- VARIABLE: Varchar (32) - Unique identifier for each individual measure. (Nullable: YES)

- METADATA: Date - Concatenation of tag names representing the axis and members appearing in the XBRL segments. Tag names have their first characters "Statement", last 4 characters "Axis", and last 6 characters "Member" or "Domain" truncated where they appear. Namespaces and prefixes are ignored because EDGAR validation guarantees that the local-names are unique with a submission. Each dimension is represented as the pair "{axis}={member};" and the axes concatenated in lexical order. Example: "LegalEntity=Xyz;Scenario=Restated;" represents the XBRL segment with dimension LegalEntityAxis and member XyzMember, dimension StatementScenarioAxis and member RestatedMember. (Nullable: YES)

- UNIT_OF_MEASURE: Varchar (16777216) - The unit of measure for the value. (Nullable: YES)

- COVERED_QTRS: Number (38, 0) - The count of the number of quarters represented by the data value, rounded to the nearest whole number. "0" indicates it is a point-in-time value (e.g., cash balance as of a particular date). (Nullable: YES)

- REPORT: Number (38, 0) - Represents the report grouping. This is the sequential order of the line item in the XBRL data. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)

- STATEMENT: Varchar (16777216) - The financial statement location to which the value of the "report" field pertains. (Nullable: YES)

- TAG_VERSION: Varchar (16777216) - An identifier for the naming convention version of a given tag. (Nullable: YES)

- ADSH: Varchar (16777216) - Accession Number assigned to each filing in the EDGAR system. Unique identifier for each individual filing. The Accession number can be used to track all records from a single filing. (Nullable: YES)

- MEASURE_DESCRIPTION: Varchar (16777216) - The text presented on the line item in the original filing. Also known as a "preferred" label. (Nullable: YES)

- PERIOD_END_DATE: Date - Period end date of the value. (Nullable: YES)


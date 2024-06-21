**Table 33: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_INSTITUTION_TIMESERIES** (FINANCIAL_INSTITUTION_TIMESERIES)

Financial metrics on FDIC-insured institutions, including financial statements, call reports, and performance analysis for individual banks over time.The FDIC BankSuite provides a comprehensive array of financial data and reports on FDIC-insured institutions in the United States. This suite typically includes detailed information such as bank financial statements, call reports (quarterly financial reports filed by banks), and Uniform Bank Performance Reports (UBPRs) which analyze the financial condition and performance of individual banks.Each row represents a distinct timeseries, date, and banking institution entity (ID_RSSD). Each variable is detailed in the financial_institution_attributes table.

- UNIT: Varchar (13) - Unit of measure for the value, examples (e.g., percentage, USD) (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable joinable to the timeseries table (Nullable: YES)

- VARIABLE_NAME: Varchar (242) - Human-readable name for the variable (Nullable: YES)

- VALUE: Number (28, 11) - Numeric value for the given data point (Nullable: YES)

- ID_RSSD: Varchar (16777216) - A unique identifier assigned by the Federal Reserve for the financial institution (Nullable: YES)

- DATE: Date - Date associated with the value (Nullable: YES)


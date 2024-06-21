**Table 29: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_INSTITUTION_ATTRIBUTES** (FINANCIAL_INSTITUTION_ATTRIBUTES)

Financial variables tracked by the FDIC for FDIC-insured institutions.The FDIC BankSuite provides a comprehensive array of financial data and reports on FDIC-insured institutions in the United States. This suite typically includes detailed information such as bank financial statements, call reports (quarterly financial reports filed by banks), and Uniform Bank Performance Reports (UBPRs) which analyze the financial condition and performance of individual banks.Provides a wide format breakdown of variables included in the financial_institution_timeseries table.The table includes a unique variable ID and a human-readable variable name. Additionally, each column represents a characteristic of the variable, including the definition of the variable, its reporting frequency, and unit of measurement.

- UNIT: Varchar (13) - Unit of measure for the value, examples (e.g., percentage, USD) (Nullable: YES)

- FREQUENCY: Varchar (9) - Measurement period (e.g., Annual, Quarterly) (Nullable: YES)

- DEFINITION: Varchar (5819) - Detailed description of the variable including calculation where applicable (Nullable: YES)

- VARIABLE: Varchar (25) - Unique identifier for a variable joinable to the timeseries table (Nullable: YES)

- VARIABLE_NAME: Varchar (242) - Human-readable name for the variable (Nullable: YES)


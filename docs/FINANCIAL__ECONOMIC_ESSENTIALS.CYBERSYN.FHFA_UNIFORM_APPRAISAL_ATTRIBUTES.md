**Table 22: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FHFA_UNIFORM_APPRAISAL_ATTRIBUTES** (FHFA_UNIFORM_APPRAISAL_ATTRIBUTES)

Single-family home appraisal trends, including home values and features, from a 5% nationally representative sample since 2013, sourced by the FHFA.The Federal Housing Finance Agency (FHFA) provides the Uniform Appraisal Dataset (UAD), which details trends found in single family appraisals (i.e. home values) collected by Fannie Mae and Freddie Mac for both new purchases and refinances since 2013. It is based on a 5% nationally representative random sample of appraisals for single-family mortgages acquired by the Enterprises.Provides a wide format breakdown of variables included in the fhfa_uniform_appraisal_timeseries table, including the reason for the appraisal request (e.g., Purchase, Refinance), the characteristic for category grouping based on home features, important home features, and unit of measurement.

- APPRAISAL_PURPOSE: Varchar (16777216) - Reason for appraisal request (e.g., Purchase, Refinance, Purchase & Refinance) (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measure for the variable: (e.g., Count, Percent, Ratio, USD) (Nullable: YES)

- VARIABLE_GROUP: Varchar (16777216) - Overall variable grouping for the timeseries (e.g., Median Appraised Value, Count of Appraisals, etc.) (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the timeseries table for filtering (Nullable: YES)

- CATEGORY: Varchar (16777216) - Actual category corresponding to the characteristic type. Notes important features of home (e.g. No Central Air, built between 1970 to 1979, etc.) (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of aggregations (e.g. Annual). (Nullable: YES)

- CHARACTERISTIC: Varchar (16777216) - Characteristic for category grouping based on home features (e.g., Central Air, Type of Foundation, etc) (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable description for the variable (Nullable: YES)


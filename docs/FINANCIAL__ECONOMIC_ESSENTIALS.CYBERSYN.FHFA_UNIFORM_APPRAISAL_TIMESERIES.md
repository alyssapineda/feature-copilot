**Table 23: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FHFA_UNIFORM_APPRAISAL_TIMESERIES** (FHFA_UNIFORM_APPRAISAL_TIMESERIES)

Single-family home appraisal trends, including home values and features, from a 5% nationally representative sample since 2013, sourced by the FHFA.The Federal Housing Finance Agency (FHFA) provides the Uniform Appraisal Dataset (UAD), which details trends found in single family appraisals (i.e. home values) collected by Fannie Mae and Freddie Mac for both new purchases and refinances since 2013. It is based on a 5% nationally representative random sample of appraisals for single-family mortgages acquired by the Enterprises.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the fhfa_uniform_appraisal_attributes. The table also flags values that were suppressed due to privacy reasons.

- DATE: Date - Date associated with the value (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measure for the variable (e.g., Count, Percent, Ratio, USD) (Nullable: YES)

- VALUE: Date - The reported numeric value for the variable and date (Nullable: YES)

- SUPPRESSED: Date - Boolean indicating whether the value has been suppressed in the underlying data for privacy purposes. Suppressed values appear as NULL (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable description for the variable (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the attributes table for filtering (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique geographic identifier joinable to the geography_index/relationships tables (Nullable: YES)


**Table 4: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.BUREAU_OF_LABOR_STATISTICS_EMPLOYMENT_TIMESERIES** (BUREAU_OF_LABOR_STATISTICS_EMPLOYMENT_TIMESERIES)

Employment, job openings, labor turnover, and wages tracked across US regions in the LAUS, JOLTS, and SAE reports from the BLS. The US Bureau of Labor Statistics (BLS) produces granular employment reports: Local Area Unemployment Statistics (LAUS) provides monthly and annual employment, unemployment, and labor force data for states and localities; Job Openings and Labor Turnover Survey (JOLTS) covers labor demand and turnover rates, including data on job openings, hires, and separations; and State and Metro Employment (SAE) delivers employment and wage data across various industries at state and metropolitan levels.Each row represents a distinct timeseries collected by the BLS reports (LAUS, JOLTS, and SAE), date, and value by geographic entity JOINABLE to Cybersyn's geography entity tables. Each variable is detailed in the bureau_of_labor_statistics_employment_attributes table.

- GEO_ID: Varchar (16777216) - A unique identifier for a place, joinable to the geography_index/relationships tables (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for a variable (Nullable: YES)

- VALUE: Date - Value of the metric (Nullable: YES)

- DATE: Date - Date associated with the value, which is set to the last day of the reporting period (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the attributes table (Nullable: YES)


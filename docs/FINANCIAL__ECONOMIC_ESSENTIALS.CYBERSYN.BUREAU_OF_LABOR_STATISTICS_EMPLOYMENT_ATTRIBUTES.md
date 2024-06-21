**Table 3: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.BUREAU_OF_LABOR_STATISTICS_EMPLOYMENT_ATTRIBUTES** (BUREAU_OF_LABOR_STATISTICS_EMPLOYMENT_ATTRIBUTES)

Employment, job openings, labor turnover, and wages tracked across US regions in the LAUS, JOLTS, and SAE reports from the BLS. The US Bureau of Labor Statistics (BLS) produces granular employment reports: Local Area Unemployment Statistics (LAUS) provides monthly and annual employment, unemployment, and labor force data for states and localities; Job Openings and Labor Turnover Survey (JOLTS) covers labor demand and turnover rates, including data on job openings, hires, and separations; and State and Metro Employment (SAE) delivers employment and wage data across various industries at state and metropolitan levels. Provides a wide format breakdown of variables included in the bureau_of_labor_statistics_employment_timeseries table. The BLS report is provided for reference. Additionally, variables are defined by seasonal adjustment, related industry, and size of the establishment referenced.

- UNIT: Varchar (16777216) - Unit of measure for the value (Nullable: YES)

- FREQUENCY: Varchar (7) - Frequency of the variable measurement (Nullable: YES)

- MEASURE: Varchar (72) - Description of type of statistic provided by the time series (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the timeseries table (Nullable: YES)

- INDUSTRY: Varchar (145) - Industry or sub-industry of the time series (Nullable: YES)

- ESTABLISHMENT_SIZE: Varchar (24) - Size of the establishment for the provided variable (Nullable: YES)

- REPORT: Varchar (26) - BLS dataset the time series originates from (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for a variable (Nullable: YES)

- SEASONALLY_ADJUSTED: Date - Boolean variable denoting if value is seasonally adjusted (Nullable: YES)


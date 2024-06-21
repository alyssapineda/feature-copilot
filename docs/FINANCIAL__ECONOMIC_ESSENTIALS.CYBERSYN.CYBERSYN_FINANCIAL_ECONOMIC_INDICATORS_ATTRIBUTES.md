**Table 11: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.CYBERSYN_FINANCIAL_ECONOMIC_INDICATORS_ATTRIBUTES** (CYBERSYN_FINANCIAL_ECONOMIC_INDICATORS_ATTRIBUTES)

Economic metrics including retail sales, consumer credit, mortgage rates, unemployment claims, GDP estimates, employment, and CPI data for various geographic entities, aggregated from various government sources.The Cybersyn Financial & Economic Indicators tables include data aggregated from various government sources. It features various economic metrics, such as the Census Bureau's retail sales, Federal Reserve's commercial paper and consumer credit, New York Fed's SOFR and EFFR data, Freddie Mac's house price index and mortgage rates, the Department of Labor's weekly unemployment claims, Bureau of Economic Analysis GDP estimates, Bureau of Labor Statistics employment and CPI data, and more.Provides a wide format breakdown of variables included in the cybersyn_financial_economic_indicators_timeseries table.

- FRED_SERIES_ID: Varchar (16777216) - Unique identifier for the variable from the FRED database. Visualize the timeseries by inputing this into https://fred.stlouisfed.org/series/{fred_series_id}. (Nullable: YES)

- RELEASE_NAME: Varchar (16777216) - The individual report or collection of data in which the data was released. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- SEASONALLY_ADJUSTED: Varchar (16777216) - Indicates whether the value is seasonally adjusted. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of aggregations. (Nullable: YES)

- RELEASE_SOURCE: Varchar (27) - Source where the variable is originally collected or published. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- MEASURE: Varchar (16777216) - Quantifiable attribute or subject; description of what is being recorded. (Nullable: YES)

- MEASUREMENT_TYPE: Varchar (16777216) - Details how the variable was measured or calculated; specifications for the type of unit measured. (Nullable: YES)

- INDUSTRY: Varchar (16777216) - Industry or sub-industry of the time series. (Nullable: YES)


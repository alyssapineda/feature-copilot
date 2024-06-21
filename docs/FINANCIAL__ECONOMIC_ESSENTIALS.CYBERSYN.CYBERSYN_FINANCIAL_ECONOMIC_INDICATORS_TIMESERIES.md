**Table 12: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.CYBERSYN_FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES** (CYBERSYN_FINANCIAL_ECONOMIC_INDICATORS_TIMESERIES)

Economic metrics including retail sales, consumer credit, mortgage rates, unemployment claims, GDP estimates, employment, and CPI data for various geographic entities, aggregated from various government sources.The Cybersyn Financial & Economic Indicators tables include data aggregated from various government sources. It features various economic metrics, such as the Census Bureau's retail sales, Federal Reserve's commercial paper and consumer credit, New York Fed's SOFR and EFFR data, Freddie Mac's house price index and mortgage rates, the Department of Labor's weekly unemployment claims, Bureau of Economic Analysis GDP estimates, Bureau of Labor Statistics employment and CPI data, and more.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the cybersyn_financial_economic_indicators_attributes table.

- VALUE: Date - Value reported for the variable. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place. Joinable to other geography tables including GEOGRAPHY_INDEX, GEOGRAPHY_RELATIONSHIPS, and GEOGRAPHY_CHARACTERISTICS. (Nullable: YES)


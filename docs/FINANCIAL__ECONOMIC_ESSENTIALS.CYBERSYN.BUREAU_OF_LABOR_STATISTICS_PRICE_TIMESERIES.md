**Table 6: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.BUREAU_OF_LABOR_STATISTICS_PRICE_TIMESERIES** (BUREAU_OF_LABOR_STATISTICS_PRICE_TIMESERIES)

US CPI and average price data, measuring average change in prices paid by consumers for goods and services over time and thus inflation, at the country, region, division, and CBSA levels, reported by the Bureau of Labor Statistics.The US Bureau of Labor Statistics (BLS) releases the Consumer Price Index (CPI) report, which measures the average change in prices paid by consumers for goods and services over time. This report serves as a key indicator of inflation. The Average Price report provides estimates of price levels (i.e. average price paid by the consumer for a good or service).Each row represents a distinct timeseries from the CPI & Average Price BLS reports, date, and value by geographic entity, joinable to Cybersyn's geography entity tables. Each variable is detailed in the bureau_of_labor_statistics_price_attributes table.

- DATE: Date - Date associated with the value, which is set to the last day of the reporting period (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place, joinable to the geography_index/relationships tables (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the attributes table (Nullable: YES)

- VALUE: Date - Value of the metric (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for a variable (Nullable: YES)


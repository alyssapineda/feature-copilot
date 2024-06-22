**Table 5: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.BUREAU_OF_LABOR_STATISTICS_PRICE_ATTRIBUTES** (BUREAU_OF_LABOR_STATISTICS_PRICE_ATTRIBUTES)

US CPI and average price data, measuring average change in prices paid by consumers for goods and services over time and thus inflation, reported by the Bureau of Labor Statistics.The US Bureau of Labor Statistics (BLS) releases the Consumer Price Index (CPI) report, which measures the average change in prices paid by consumers for goods and services over time. This report serves as a key indicator of inflation. The Average Price report provides estimates of price levels (i.e. average price paid by the consumer for a good or serviceProvides a wide format breakdown of variables included in the bureau_of_labor_statistics_price_timeseries table. The BLS report is provided for reference). Additionally, variables are defined by seasonal adjustment, consumer product, and CPI base type (e.g., standard or alternative).

- FREQUENCY: Varchar (11) - Frequency of the variable measurement (Nullable: YES)

- VARIABLE_NAME: Varchar (160) - Human-readable name for a variable (Nullable: YES)

- REPORT: Varchar (20) - BLS dataset the time series originates from (Nullable: YES)

- BASE_TYPE: Varchar (24) - Base type utilized for CPI measurement, standard or alternative (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the timeseries table (Nullable: YES)

- SEASONALLY_ADJUSTED: Date - Boolean variable denoting if value is seasonally adjusted (Nullable: YES)

- PRODUCT: Varchar (97) - Consumer product being measured (Nullable: YES)

- UNIT: Varchar (18) - Unit of measure for the value (Nullable: YES)


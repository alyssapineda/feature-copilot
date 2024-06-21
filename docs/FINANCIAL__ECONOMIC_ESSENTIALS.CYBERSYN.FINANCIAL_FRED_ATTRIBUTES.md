**Table 26: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_FRED_ATTRIBUTES** (FINANCIAL_FRED_ATTRIBUTES)

Economic and financial metrics including retail sales, foreign exchange rates, industrial production, and bank-specific data like deposits, liabilities, and loan balances.FRED, published by the St. Louis Federal Reserve, includes information aggregated from various government sources. It features various economic metrics such as monthly retail sales, foreign exchange rates, and industrial production as well as, financial-institution-specific data (e.g. flow of deposits for small and large banks, total bank liabilities, outstanding balance of commercial real estate loans).Provides a wide format breakdown of variables included in the financial_fred_timeseries table.The table includes a unique variable ID and a human-readable variable name. Additionally, each column represents a characteristic of the variable, including the type of value being measured, the specific FRED release, the release source, if the variable is seasonally adjusted, its unit of measurement, frequency of measurement, and measurement methodology.

- RELEASE_SOURCE: Varchar (16777216) - The original attribution of the data from which Fred aggregates. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - English name for the variable (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of the variable measurement (e.g., Daily, Monthly, or Quarterly) (Nullable: YES)

- MEASUREMENT_METHOD: Varchar (16777216) - Type of percent change measurement (Nullable: YES)

- VARIABLE: Varchar (16777216) - a unique identifier for a variable joinable to the time series table (Nullable: YES)

- SEASONALLY_ADJUSTED: Date - Boolean variable denoting if value is seasonally adjusted (Nullable: YES)

- VARIABLE_GROUP: Varchar (16777216) - Description of what is being measured (Nullable: YES)

- RELEASE_NAME: Varchar (16777216) - The individual report or collection of data in which the data was released. Sample reports include the Consumer Price Index release from the Bureau of Labor Statistics and the G.5 Foreign Exchange Rates release from the Federal Reserve. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measure for the value (e.g., USD, Percent, or ratio) (Nullable: YES)


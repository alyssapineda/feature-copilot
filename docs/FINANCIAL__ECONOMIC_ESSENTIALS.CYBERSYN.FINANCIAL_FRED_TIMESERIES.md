**Table 27: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_FRED_TIMESERIES** (FINANCIAL_FRED_TIMESERIES)

Economic and financial metrics including retail sales, foreign exchange rates, industrial production, and bank-specific data like deposits, liabilities, and loan balances.FRED, published by the St. Louis Federal Reserve, includes information aggregated from various government sources. It features various economic metrics such as monthly retail sales, foreign exchange rates, and industrial production as well as, financial-institution-specific data (e.g. flow of deposits for small and large banks, total bank liabilities, outstanding balance of commercial real estate loans).Provides historical values for variables collected by FRED by GEO_ID.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the financial_fred_attributes table.

- GEO_ID: Varchar (11) - a unique identifier for a place (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measure for the value, such as dollars, percent, or ratio (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - English name for the variable (Nullable: YES)

- VARIABLE: Varchar (16777216) - a unique identifier for a variable joinable to the attributes table (Nullable: YES)

- VALUE: Date - the actual numeric value for the variable (Nullable: YES)

- DATE: Date - Date associated with the value, which is set to the last day of the reporting period. (Nullable: YES)


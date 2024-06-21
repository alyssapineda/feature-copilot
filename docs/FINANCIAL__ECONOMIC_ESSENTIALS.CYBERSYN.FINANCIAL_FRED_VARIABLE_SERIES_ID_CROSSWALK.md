**Table 28: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_FRED_VARIABLE_SERIES_ID_CROSSWALK** (FINANCIAL_FRED_VARIABLE_SERIES_ID_CROSSWALK)

Map between FRED's reported SERIES_ID and Cybersyn's VARIABLE identifier, along with the associated GEO_ID.FRED, published by the St. Louis Federal Reserve, includes information aggregated from various government sources. It features various economic metrics such as monthly retail sales, foreign exchange rates, and industrial production as well as, financial-institution-specific data (e.g. flow of deposits for small and large banks, total bank liabilities, outstanding balance of commercial real estate loans).

- SERIES_ID: Varchar (16777216) - Series identifier from the FRED database. The combination of the geo_id and variable are needed together to identify a unique series_id (Nullable: YES)

- GEO_ID: Varchar (11) - Unique identifier for a place joinable to the timeseries table. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier joinable to the attributes and timeseries tables. (Nullable: YES)


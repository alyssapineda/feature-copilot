**Table 14: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.EUROPEAN_CENTRAL_BANK_TIMESERIES** (EUROPEAN_CENTRAL_BANK_TIMESERIES)

Consumer price indices, residential property prices, and valuations for European countries and country groups, provided by the European Central Bank.The European Central Bank (ECB) is a central institution of the Eurozone, primarily responsible for managing the euro and framing and implementing EU economic & monetary policy. Our ECB data covers the following: (1) Consumer Price Indices for a wide range of consumer goods, (2) Residential Property Prices, and (3) Residential Property Valuations. Data is provided for European countries as well as the European country groups.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the european_central_bank_attributes table.

- GEO_ID: Varchar (16777216) - A unique identifier for a place. Joinable to other geography tables including GEOGRAPHY_INDEX, GEOGRAPHY_RELATIONSHIPS, and GEOGRAPHY_CHARACTERISTICS. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- VALUE: Date - Value reported for the variable. (Nullable: YES)

- VALUE_COMMENT: Varchar (16777216) - Comment on the source, measurement, or definition of the value. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)


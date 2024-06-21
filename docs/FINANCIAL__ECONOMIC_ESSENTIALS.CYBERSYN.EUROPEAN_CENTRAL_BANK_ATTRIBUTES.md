**Table 13: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.EUROPEAN_CENTRAL_BANK_ATTRIBUTES** (EUROPEAN_CENTRAL_BANK_ATTRIBUTES)

Consumer price indices, residential property prices, and valuations for European countries and country groups, provided by the European Central Bank.The European Central Bank (ECB) is a central institution of the Eurozone, primarily responsible for managing the euro and framing and implementing EU economic & monetary policy. Our ECB data covers the following: (1) Consumer Price Indices for a wide range of consumer goods, (2) Residential Property Prices, and (3) Residential Property Valuations. Data is provided for European countries as well as the European country groups.Provides a wide format breakdown of variables included in the european_central_bank_timeseries table.

- MEASURE: Varchar (16777216) - Quantifiable attribute or subject; description of what is being recorded. (Nullable: YES)

- ITEM_DESCRIPTION: Varchar (16777216) - The item category referenced as part of the harmonized index of consumer prices. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- SOURCE: Varchar (16777216) - Source where the variable is originally collected or published. (Nullable: YES)

- MEASUREMENT_TYPE: Varchar (16777216) - Details how the variable was measured or calculated; specifications for the type of unit measured (e.g., 3-month moving average (Average of observations through period)). (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- SEASONALLY_ADJUSTED: Varchar (16777216) - Indicates whether the value is seasonally adjusted. (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of aggregations. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- GEO_COVERAGE: Varchar (16777216) - Determines whether the variable relates to part or all of a country (e.g., Whole country, Large cities, National excluding capital city). (Nullable: YES)


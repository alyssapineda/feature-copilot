**Table 1: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.BANK_FOR_INTERNATIONAL_SETTLEMENTS_ATTRIBUTES** (BANK_FOR_INTERNATIONAL_SETTLEMENTS_ATTRIBUTES)

Financial variables on international property prices, central bank policy rates, banking activities and risks, credit availabity to the non-financial sector, liquidity, and consumer prices from the BIS, a central bank for other central banks. The Bank for International Settlements (BIS) is an international financial organization that provides data series on Property Prices (real estate market trends), Central Bank Policy Rates (global monetary policy), Locational and Consolidated Banking Statistics (international banking activities and risks), Credit to the Non-Financial Sector (credit availability), Global Liquidity Indicators, and Consumer Prices (inflationary activity). Provides a wide format breakdown of variables included in the bank_for_international_settlements_timeseries table. The BIS Series ID is provided for reference.

- GEO_NAME: Varchar (16777216) - Country or country group, representing the primary geography for the variable. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for the variable. (Nullable: YES)

- COUNTERPARTY_GEO_NAME: Varchar (16777216) - Country or country group, representing the counterparty geography for the variable. (Nullable: YES)

- SERIES_ID: Varchar (16777216) - Unique identifier for a variable series (i.e., data flow) from the Bank for International Settlements (BIS). (Nullable: YES)

- MEASURE: Varchar (16777216) - Quantifiable attribute; description of what is being recorded. (Nullable: YES)

- MEASUREMENT_TYPE: Varchar (16777216) - Methodology for the collection of a variable over time. (Nullable: YES)

- SOURCE: Varchar (16777216) - Source where the variable is published. (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of aggregations. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable from the Bank for International Settlements (BIS) data flow and key IDs, joinable to the timeseries table. (Nullable: YES)


**Table 2: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.BANK_FOR_INTERNATIONAL_SETTLEMENTS_TIMESERIES** (BANK_FOR_INTERNATIONAL_SETTLEMENTS_TIMESERIES)

Country-level statistics on real estate market trends, monetary policy rates, banking activities, credit availability to the non-financial sector, liquidity conditions, and inflation, provided by the central bank for central banks, Bank for International Settlements (BIS). The Bank for International Settlements (BIS) is an international financial organization that provides data series on Property Prices (real estate market trends), Central Bank Policy Rates (global monetary policy), Locational and Consolidated Banking Statistics (international banking activities and risks), Credit to the Non-Financial Sector (credit availability), Global Liquidity Indicators, and Consumer Prices (inflationary activity). Each row represents a distinct timeseries, date, and value by primary and counterparty geographic entities (if available). Each variable is detailed in the bank_for_international_settlements_attributes table.

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable name for the variable. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a country or country group, joinable to the GEOGRAPHY_INDEX table, representing the primary geography for the variable. (Nullable: YES)

- COUNTERPARTY_GEO_ID: Varchar (16777216) - A unique identifier for a country or country group, joinable to the GEOGRAPHY_INDEX table, representing the counterparty geography for the variable. (Nullable: YES)

- VALUE: Date - Value reported for the variable. (Nullable: YES)


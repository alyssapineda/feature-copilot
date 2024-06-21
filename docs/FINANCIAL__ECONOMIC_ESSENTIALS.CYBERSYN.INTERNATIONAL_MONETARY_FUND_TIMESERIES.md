**Table 40: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.INTERNATIONAL_MONETARY_FUND_TIMESERIES** (INTERNATIONAL_MONETARY_FUND_TIMESERIES)

Economic and financial indicators for countries and regions, including commodity prices, balance of payments, government finances, investment, and regional economic outlooks, provided by the IMF.The International Monetary Fund (IMF) provides data on the following topics: Primary Commodity Price System (prices of commodities by country); Balance of Payments (countries’ economic transactions with the rest of the world, including trade balances, capital flows, and official reserves); Fiscal Monitor (detailed government finances); International Financial Statistics (macroeconomic and financial indicators); Coordinated Portfolio Investment Survey (cross-border holdings of equity and debt securities); Africa Regional Economic Outlook (economic indicators for Africa); Asia and Pacific Regional Economic Outlook (economic indicators for the Asia and Pacific region).Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the international_monetary_fund_attributes table.

- DATE: Date - Date associated with the value. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place. Joinable to other geography tables including GEOGRAPHY_INDEX, GEOGRAPHY_RELATIONSHIPS, and GEOGRAPHY_CHARACTERISTICS. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- VALUE: Date - Value reported for the variable. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)


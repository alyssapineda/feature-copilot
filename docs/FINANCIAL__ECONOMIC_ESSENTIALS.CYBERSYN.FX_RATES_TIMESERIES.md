**Table 34: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FX_RATES_TIMESERIES** (FX_RATES_TIMESERIES)

Foreign exchange rates for currency pairs (base and quote currencies), with data from FRED, ECB, and BIS.Foreign exchange (FX) rates are the rates at which one currency can be exchanged for another. These rates fluctuate based on various factors including economic indicators, market sentiment, political events, and global financial stability. Foreign exchange rates are crucial for international trade and finance, as they determine how much of one currency is needed to buy a unit of another currency. These rates can be floating, changing continuously based on market forces, or they might be pegged (fixed) to another major currency or basket of currencies, managed by a country's central bank. FX rates data is provided historically by FRED (pre-2000) and by the European Central Bank (ECB) and Bank for International Settlements (BIS) for 2000 onwards. To note, these data sources often do not publish the exchange rate every day.Provides historical values for each currency pair collected by BASE_CURRENCY_ID and QUOTE_CURRENCY_ID.Each row represents a distinct timeseries, date, and value by currency pair.

- QUOTE_CURRENCY_NAME: Varchar (16777216) - Long name of quote currency (Nullable: YES)

- VALUE: Date - Price for the base currency in terms of the quote currency (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for the currency pair (Nullable: YES)

- QUOTE_CURRENCY_ID: Varchar (16777216) - ISO 4217 currency code for the quote currency (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - A human-readable unique identifier for the currency pair (Nullable: YES)

- DATE: Date - Date for the foreign exchange spot rate (Nullable: YES)

- BASE_CURRENCY_ID: Varchar (16777216) - ISO 4217 currency code for the base currency (Nullable: YES)

- BASE_CURRENCY_NAME: Varchar (16777216) - Long name of base currency (Nullable: YES)


**Table 48: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.STOCK_PRICE_TIMESERIES** (STOCK_PRICE_TIMESERIES)

Cybersyn publishes daily prices (open/close, high/low) & trading volumes of US securities executed on the Nasdaq. The data is sourced from Databento's direct feed with Nasdaq TotalView. Cybersyn makes data from the previous trading day available around 6am ET.Trading volume, open/close, and high/low prices are based on full day trading, inclusive of pre-market, regular trading, and after hours sessions. For example, the open price will reflect the price of the first trade of the day in the pre-market. The trading volume will reflect the total number of trades executed on the Nasdaq throughout all sessions. 

- VALUE: Date - Value reported for the variable. (Nullable: YES)

- TICKER: Varchar (16777216) - Alphanumeric code that represents a specific publicly traded security on the NASDAQ exchange. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)

- VARIABLE_NAME: Varchar (17) - Human-readable unique name for the variable. (Nullable: YES)

- PRIMARY_EXCHANGE_NAME: Varchar (16777216) - The exchange name for the primary trading venue of a security. (Nullable: YES)

- PRIMARY_EXCHANGE_CODE: Varchar (16777216) - The exchange code for the primary trading venue of a security. (Nullable: YES)

- ASSET_CLASS: Varchar (16777216) - Type of security. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)


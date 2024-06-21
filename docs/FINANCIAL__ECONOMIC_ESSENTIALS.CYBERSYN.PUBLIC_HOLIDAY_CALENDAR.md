**Table 47: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.PUBLIC_HOLIDAY_CALENDAR** (PUBLIC_HOLIDAY_CALENDAR)

The Public Holiday Calendar provides reference data containing government-designated holidays for 119 countries since 1970, as well as the financial market holidays for the European Central Bank (ECB) and New York Stock Exchange (NYSE).Provides historical values for each public holiday by GEO_ID.Each row represents a distinct timeseries, date, and holiday name by geographic entity. It identifies whether the holiday is financial.

- IS_FINANCIAL: Date - Boolean denoting a stock market closure for the given region (Nullable: YES)

- DATE: Date - Date associated with the event (Nullable: YES)

- GEO_ID: Varchar (16777216) - GEO_ID from GEOGRAPHY_INDEX table (Nullable: YES)

- HOLIDAY_NAME: Varchar (16777216) - Name of the Holiday (Nullable: YES)

- ISO_ALPHA2: Varchar (16777216) - 2 letter country code from International Organization for Standardization (Nullable: YES)

- SUBDIVISION: Varchar (16777216) - State, province, or other underlying geography that is specific to the holiday (Nullable: YES)


**Table 42: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.NEWYORKFED_CONSUMER_TIMESERIES** (NEWYORKFED_CONSUMER_TIMESERIES)

Monthly household economic expectations and behavior data, and quarterly consumer debt and credit trends, including balances, delinquencies, and bankruptcies for the US.The Federal Reserve Bank of New York (or New York Fed) provides data on economic perspectives and behaviors of US households in the Survey of Consumer Expectations (SCE) and the Household Debt and Credit Report. The Survey of Consumer Expectations (SCE) collects monthly data on households' economic expectations and behavior on inflation, the labor market, and personal finance. This survey is unique in its detailed questioning regarding the probability of certain events occurring in the respondents' financial lives (e.g., inflation, spending, income), serving as a tool for understanding future consumer behavior and economic trends. The Household Debt and Credit Report provides quarterly updates on trends in consumer debt and credit, including breakdowns by debt type and credit score. It draws from a nationally representative sample of anonymized Equifax credit data to report on developments in mortgage, student loan, auto loan, and credit card balances, as well as bankruptcy filings and delinquencies.Provides historical values for each variable collected.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the newyorkfed_consumer_attributes table.

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place. Joinable to other geography tables including GEOGRAPHY_INDEX, GEOGRAPHY_RELATIONSHIPS, and GEOGRAPHY_CHARACTERISTICS. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- VALUE: Date - Value reported for the variable. (Nullable: YES)


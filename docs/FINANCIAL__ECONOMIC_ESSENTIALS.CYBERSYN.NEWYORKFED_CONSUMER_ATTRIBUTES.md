**Table 41: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.NEWYORKFED_CONSUMER_ATTRIBUTES** (NEWYORKFED_CONSUMER_ATTRIBUTES)

Monthly household economic expectations and behavior data, and quarterly consumer debt and credit trends, including balances, delinquencies, and bankruptcies.The Federal Reserve Bank of New York (or New York Fed) provides data on economic perspectives and behaviors of US households in the Survey of Consumer Expectations (SCE) and the Household Debt and Credit Report. The Survey of Consumer Expectations (SCE) collects monthly data on households' economic expectations and behavior on inflation, the labor market, and personal finance. This survey is unique in its detailed questioning regarding the probability of certain events occurring in the respondents' financial lives (e.g., inflation, spending, income), serving as a tool for understanding future consumer behavior and economic trends. The Household Debt and Credit Report provides quarterly updates on trends in consumer debt and credit, including breakdowns by debt type and credit score. It draws from a nationally representative sample of anonymized Equifax credit data to report on developments in mortgage, student loan, auto loan, and credit card balances, as well as bankruptcy filings and delinquencies.Provides a wide format breakdown of variables included in the newyorkfed_consumer_timeseries table.

- MEASURE: Varchar (16777216) - Quantifiable attribute or subject; description of what is being recorded. (Nullable: YES)

- REPORT: Varchar (34) - Name of the New York Fed report that the data pertains to. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- FREQUENCY: Varchar (9) - Frequency of aggregations. (Nullable: YES)


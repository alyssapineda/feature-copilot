**Table 20: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FHFA_MORTGAGE_PERFORMANCE_ATTRIBUTES** (FHFA_MORTGAGE_PERFORMANCE_ATTRIBUTES)

Loan-level mortgage data from the FHFA including originations, terms, performance, borrower demographics, and delinquency rates at national, state, and local levels from 2002 onwards.The Federal Housing Finance Agency (FHFA) in partnership with the Consumer Financial Protection Bureau (CFPB) developed the National Mortgage Database (NMDB), a nationally representative 5% sample of residential mortgages in the US. It details loan-level data covering mortgage originations, terms, and performance, along with borrower demographics.; and indicates rates of delayed payments, foreclosures and bankruptcies, and forbearance. The data is grouped by geographic levels (national, state, CBSA/MSD level) and includes both Enterprise and non-Enterprise individual mortgages from 2002 onwards.Provides a wide format breakdown of variables included in the fhfa_mortgage_performance_timeseries table.

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the timeseries table for filtering (Nullable: YES)

- UNIT: Varchar (7) - Unit of measure for the variable:  (e.g., Percent) (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of aggregations (e.g. Annual). (Nullable: YES)

- MARKET: Varchar (16777216) - Market segment (e.g., Overall Market, Enterprise, Government, etc.) (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable description for the variable (Nullable: YES)

- VARIABLE_GROUP: Varchar (16777216) - Overall variable grouping for the timeseries (e.g., Percent in Forbearance, Percent 30 or 60 Days Past Due Date, etc.) (Nullable: YES)


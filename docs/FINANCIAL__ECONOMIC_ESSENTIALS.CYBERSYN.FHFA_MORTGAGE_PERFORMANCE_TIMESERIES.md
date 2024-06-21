**Table 21: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FHFA_MORTGAGE_PERFORMANCE_TIMESERIES** (FHFA_MORTGAGE_PERFORMANCE_TIMESERIES)

Loan-level mortgage data from the FHFA including originations, terms, performance, borrower demographics, and delinquency rates at national, state, and local levels from 2002 onwards.The Federal Housing Finance Agency (FHFA) in partnership with the Consumer Financial Protection Bureau (CFPB) developed the National Mortgage Database (NMDB), a nationally representative 5% sample of residential mortgages in the US. It details loan-level data covering mortgage originations, terms, and performance, along with borrower demographics.; and indicates rates of delayed payments, foreclosures and bankruptcies, and forbearance. The data is grouped by geographic levels (national, state, CBSA/MSD level) and includes both Enterprise and non-Enterprise individual mortgages from 2002 onwards.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the fhfa_mortgage_performance_attributes table.

- VARIABLE_NAME: Varchar (16777216) - Human-readable description for the variable (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique geographic identifier joinable to the geography_index/relationships tables (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the attributes table for filtering (Nullable: YES)

- UNIT: Varchar (7) - Unit of measure for the variable (e.g., Percent) (Nullable: YES)

- VALUE: Date - The reported numeric value for the variable and date (Nullable: YES)

- DATE: Date - Date associated with the value (Nullable: YES)


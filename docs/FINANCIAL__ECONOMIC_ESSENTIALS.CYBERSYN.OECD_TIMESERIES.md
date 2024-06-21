**Table 44: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.OECD_TIMESERIES** (OECD_TIMESERIES)

Economic, demographic, and labor market data for OECD countries and select non-members, including trade, wages, income distribution, population projections, and social expenditure, provided by the OECD.The OECD, or Organisation for Economic Co-operation and Development, conducts research, collects data, and provides analysis to help governments develop effective policies and address global challenges. The OECD database provides data on OECD member countries and select non-member countries. The data includes (1) Balance of payments - Financial transactions of a country with the rest of the world. (2) Composite leading indicators - Future economic trends. (3) Venture capital investments - Market statistics on entrepreneurial finance. (4) Average annual wages and hours worked per worker - Labor market trends. (5) Decile ratios of gross earnings - Income distribution. (6) Trade union density and wage gap by age - Labor force dynamics. (7) Population data and projections - Demographic trends. (8) Public and private social expenditure - Government and private sector investments in social welfare.Provides historical values for each variable collected.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the oecd_attributes table.

- VALUE: Date - Value reported for the variable. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place. Joinable to other geography tables including GEOGRAPHY_INDEX, GEOGRAPHY_RELATIONSHIPS, and GEOGRAPHY_CHARACTERISTICS. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)


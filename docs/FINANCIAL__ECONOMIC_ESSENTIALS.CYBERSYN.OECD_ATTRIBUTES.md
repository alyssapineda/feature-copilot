**Table 43: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.OECD_ATTRIBUTES** (OECD_ATTRIBUTES)

Economic, demographic, and labor market data for OECD countries and select non-members, including trade, wages, income distribution, population projections, and social expenditure, provided by the OECD.The OECD, or Organisation for Economic Co-operation and Development, conducts research, collects data, and provides analysis to help governments develop effective policies and address global challenges. The OECD database provides data on OECD member countries and select non-member countries. The data includes (1) Balance of payments - Financial transactions of a country with the rest of the world. (2) Composite leading indicators - Future economic trends. (3) Venture capital investments - Market statistics on entrepreneurial finance. (4) Average annual wages and hours worked per worker - Labor market trends. (5) Decile ratios of gross earnings - Income distribution. (6) Trade union density and wage gap by age - Labor force dynamics. (7) Population data and projections - Demographic trends. (8) Public and private social expenditure - Government and private sector investments in social welfare.Provides a wide format breakdown of variables included in the oecd_timeseries table.The table includes a unique variable ID and a human-readable variable name. Additionally, each column represents a characteristic of the variable, including the type of value being measured, unit of measurement, frequency of aggregations, and details on adjustments applied to the data.

- SEASONALLY_ADJUSTED: Varchar (16777216) - Indicates whether the value is seasonally adjusted. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit of measurement for the reported value. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- MEASURE: Varchar (16777216) - Quantifiable attribute or subject; description of what is being recorded. (Nullable: YES)

- MEASUREMENT_TYPE: Varchar (16777216) - Details how the variable was measured or calculated. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of aggregations. (Nullable: YES)


**Table 50: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.US_ECONOMIC_CENSUS_TIMESERIES** (US_ECONOMIC_CENSUS_TIMESERIES)

Detailed economic data on US businesses, such as number of establishments, types of goods and services provided, employment figures, payroll expenses, and operational costs, across different industries and geographic regions.The Economic Census is a survey conducted by the US Census Bureau every 5 years on number of firms, number of establishments; number of employees, payroll and sales, value and percentage of product shipments, revenue by geographic area for establishments and firms by NAICS code.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the us_economic_census_attributes table.

- DATE: Varchar (16777216) - Date associated with the value. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place. Joinable to other geography tables including GEOGRAPHY_INDEX, GEOGRAPHY_RELATIONSHIPS, and GEOGRAPHY_CHARACTERISTICS. (Nullable: YES)

- VALUE: Date - Value reported for the variable. (Nullable: YES)

- UNIT: Varchar (13) - Unit of measurement for the reported value. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)


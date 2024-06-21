**Table 49: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.US_ECONOMIC_CENSUS_ATTRIBUTES** (US_ECONOMIC_CENSUS_ATTRIBUTES)

Detailed economic data on US businesses, such as number of establishments, types of goods and services provided, employment figures, payroll expenses, and operational costs, across different industries and geographic regions.The Economic Census is a survey conducted by the US Census Bureau every 5 years on number of firms, number of establishments; number of employees, payroll and sales, value and percentage of product shipments, revenue by geographic area for establishments and firms by NAICS code.Provides a wide format breakdown of variables included in the us_economic_census_timeseries table. Following attributes are provides for reference: NAICS industry classification, type of operation run by the establishment, establishment's tax status, Products and Services Code and sources of credit card services income.

- CREDIT_CARD_SERVICES_INCOME: Varchar (16777216) - Specific source of credit card products or services income category (e.g., from cardholder fees, interest, merchant fees). (Nullable: YES)

- NAICS_DESCRIPTION: Varchar (16777216) - Description of Industry classification according to North American Industry Classification System. (Nullable: YES)

- NAICS_CODE: Varchar (16777216) - Industry classification according to North American Industry Classification System. (Nullable: YES)

- PRODUCT_SERVICES_LINE: Varchar (16777216) - Related product or service. (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable unique name for the variable. (Nullable: YES)

- OPERATION_TYPE: Varchar (16777216) - Type of operation run by the establishment (e.g., Merchant wholesalers; Manufacturer's sales branches and offices). (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique identifier for a variable, joinable to the timeseries table. (Nullable: YES)

- MEASURE: Varchar (16777216) - Quantifiable attribute or subject; description of what is being recorded. (Nullable: YES)

- TAX_STATUS: Varchar (16777216) - Establishment's tax status (e.g., exempt from or subject to federal income tax). (Nullable: YES)

- UNIT: Varchar (13) - Unit of measurement for the reported value. (Nullable: YES)

- FREQUENCY: Varchar (6) - Frequency of aggregations. (Nullable: YES)


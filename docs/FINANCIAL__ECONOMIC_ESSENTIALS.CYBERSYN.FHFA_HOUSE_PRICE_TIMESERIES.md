**Table 19: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FHFA_HOUSE_PRICE_TIMESERIES** (FHFA_HOUSE_PRICE_TIMESERIES)

House price indexes measuring single-family home price changes in the US since 1975, across various geographic levels and property classifications, provided from the FHFA based on Fannie Mae and Freddie Mac mortgage data.The Federal Housing Finance Agency (FHFA) provides the House Price Index (HPI), a collection of publicly available price indexes that measure movement of single-family house prices in the US since 1975. The FHFA compiles this data by examining repeat mortgage transactions on single-family properties whose mortgages have been purchased or securitized by Fannie Mae or Freddie Mac, across various geographic levels.Provides historical values for each variable collected by the FHFA HPI by GEO_ID.Each row represents a distinct timeseries, date, and value by geographic entity. Each variable is detailed in the fhfa_house_price_attributes table.

- UNIT: Varchar (5) - Unit of measure for the variable (e.g., Index) (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable description for the variable (Nullable: YES)

- VALUE: Number (6, 2) - The reported numeric value for the variable and date (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique geographic identifier joinable to the geography_index/relationships tables (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the attributes table for filtering (Nullable: YES)

- DATE: Date - Date associated with the value (Nullable: YES)


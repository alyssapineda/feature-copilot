**Table 18: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FHFA_HOUSE_PRICE_ATTRIBUTES** (FHFA_HOUSE_PRICE_ATTRIBUTES)

House price indexes measuring single-family home price changes in the US since 1975, across various geographic levels and property classifications, provided from the FHFA based on Fannie Mae and Freddie Mac mortgage data.The Federal Housing Finance Agency (FHFA) provides the House Price Index (HPI), a collection of publicly available price indexes that measure movement of single-family house prices in the US since 1975. The FHFA compiles this data by examining repeat mortgage transactions on single-family properties whose mortgages have been purchased or securitized by Fannie Mae or Freddie Mac, across various geographic levels.Provides a wide format breakdown of variables included in the fhfa_house_price_timeseries table.The table includes a unique variable ID and a human-readable variable name. Additionally, each column represents a characteristic of the variable, including its property classification (traditional, distress-free, non-metro), how the index is measured (all-transactions, purchase-only, expanded-data), the frequency of the measurement, whether the variable is seasonally adjusted, and its unit of measurement.

- VARIABLE_NAME: Varchar (16777216) - Human-readable description for the variable (Nullable: YES)

- SEASONALLY_ADJUSTED: Date - Boolean field indicating if a series is seasonally adjusted (Nullable: YES)

- FREQUENCY: Varchar (16777216) - Frequency of the variable measurement (e.g., Daily, Monthly, Quarterly) (Nullable: YES)

- UNIT: Varchar (5) - Unit of measure for the variable:  (e.g., Index) (Nullable: YES)

- INDEX_TYPE: Varchar (16777216) - Type of House Price Index measured in the index (all-transactions, purchase-only, expanded-data) (Nullable: YES)

- PROPERTY_CLASSIFICATION: Varchar (16777216) - House Price Index classification (traditional, distress-free, non-metro) (Nullable: YES)

- VARIABLE: Varchar (16777216) - A unique identifier for a variable joinable to the timeseries table for filtering (Nullable: YES)


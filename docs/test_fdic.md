**Table 5: BANKING_ANALYTICS_BUNDLE.BANKING_INSIGHTS.FDIC** (Financial Institution Data information)

This table contains information about financial institution data and their attributes

- CBSA_DIV: Varchar (50) - related to divisions or segments within Core-Based Statistical Areas (CBSAs) in the United States. (Nullable: YES)

- BANK_CLASS: Varchar (50) - The "bank_class" column  typically refers to the classification or category of the financial institution based on its characteristics and activities. (Nullable: YES)

- CBSA_METRO: Number (20, 0) -  indicates whether the institutions location falls within a Metropolitan Statistical Area (MSA), as defined by the U.S. Office of Management and Budget (OMB). This classification helps 

                                  provide insights into the institutions geographic context and its relation to urban centers. (Nullable: YES)

- CBSA_MICRO_FLG: Number (20, 0) -  it appears that this column might relate to a flag or indicator associated with the Core-Based Statistical Area (CBSA) classification, specifically for Micropolitan Statistical Areas 

                                (μSAs), as defined by the United States Office of Management and Budget (OMB). (Nullable: YES)

- RUNDATE: Date -  represent the date on which the dataset was generated. (Nullable: YES)

- FAILED_BANK_CLOSING_DATE: Date - refers to the date on which the financial institution was closed or taken over by regulators due to financial distress or insolvency. (Nullable: YES)

- COUNTY: Varchar (225) - the "County" column typically refers to the geographic location or jurisdiction where the financial institutions primary office or branch is located (Nullable: YES)

- CBSA_DIV_NO: Number (20, 0) - refer to a code or identifier associated with a Core-Based Statistical Area (CBSA) division number (Nullable: YES)

- FAILED_BANK_DEPOSIT_INSURED_FUND: Number (38, 0) -  refers to the amount of insured deposits that were covered by the Federal Deposit Insurance Corporation (FDIC) when a financial institution failed (Nullable: YES)

- CITY: Varchar (225) -  the "City" column typically refers to the name of the city where a specific branch or location of the financial institution is located. (Nullable: YES)

- NAME: Varchar (225) - the column refers to the name of institution (Nullable: YES)

- ADDRESS: Varchar (225) - the "address" column typically refers to the physical location or mailing address of the financial institution. (Nullable: YES)

- CBSA_DIV_FLG: Number (20, 0) -  this column could potentially indicate whether a particular institutions location falls within a designated division of a Core-Based Statistical Area (CBSA) in the United States (Nullable: YES)

- FAILED_BANKLIST: Number (1, 0) - refer to its failed bank or not according to fdic (Nullable: NO)

- FAILED_BANK_ACQUIRING_INSITUTION: Varchar (16777216) - refers to the financial institution that takes over the operations and assets of a failed or troubled bank through a merger or acquisition facilitated by the Federal Deposit Insurance Corporation (FDIC). (Nullable: YES)

- CBSA_METRO_FLG: Number (20, 0) - contain a binary indicator (0 or 1) to specify whether the institutions location falls within a metropolitan or micropolitan statistical area (Nullable: YES)

- CBSA_NO: Number (20, 0) - "CSBA_NO" might refer to a unique identifier or code associated with a Core-Based Statistical Area (CBSA). (Nullable: YES)

- STATE_NAME: Varchar (50) -  the "state_name" column typically refers to the name of the state where a specific branch or location of the financial institution is located. (Nullable: YES)

- STALP: Varchar (225) - related to state abbreviations (Nullable: YES)

- ZIP: Varchar (225) - refer to the ZIP codes associated with the location of a financial institution.  (Nullable: YES)

- ACTIVE: Number (20, 0) - the "Active" column in FDIC insured financial institution datasets indicates whether a particular institution is currently operational and offering its services. (Nullable: YES)

- CBSA: Varchar (50) - A Core-Based Statistical Area (CbSA) is a term used by the United States Office of Management and Budget (OMB) to define geographic regions in the United States. (Nullable: YES)

- CBSA_METRO_NAME: Varchar (50) - refer to a column containing names or identifiers related to Micropolitan Statistical Areas (μSAs), which are part of the Core-Based Statistical Area (CBSA) classification system 

                                  used by the United States Office of Management and Budget (OMB). (Nullable: YES)

- DOCKET: Number (20, 0) - the "docket" column likely refers to a unique identifier or reference number assigned to a specific legal or regulatory case related to the financial institution (Nullable: YES)

- DATE_UPDATED: Date - the column refers to the date on which the information or data related to a specific financial institution was last updated by  (FDIC). (Nullable: YES)

- CERTIFICATE_NUMBER: Number (38, 0) - the column refers to a unique identification number assigned by the Federal Deposit Insurance Corporation (FDIC) to each financial institution that is insured by the FDIC. (Nullable: NO)

- ASSET: Number (20, 0) - the "Asset" column refers to the total value of assets held by the financial institution. (Nullable: YES)


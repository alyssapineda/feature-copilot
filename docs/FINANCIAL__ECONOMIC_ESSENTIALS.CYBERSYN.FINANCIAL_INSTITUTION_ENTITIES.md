**Table 30: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_INSTITUTION_ENTITIES** (FINANCIAL_INSTITUTION_ENTITIES)

Index of all financial institutions and banks in the US regulated by the Federal Deposit Insurance Corporation (FDIC) and Federal Financial Institutions Examination Council (FFIEC). The FDIC BankSuite provides a comprehensive array of financial data and reports on FDIC-insured institutions in the United States. This suite typically includes detailed information such as bank financial statements, call reports (quarterly financial reports filed by banks), and Uniform Bank Performance Reports (UBPRs) which analyze the financial condition and performance of individual banks.Provides a wide format breakdown of FDIC-insured entities by ID_RSSD.The table includes a unique institution ID (ID_RSSD), geographic location, start and end dates, charter types, other identifiers for the institution, associated NAICS codes, and more.

- FDIC_CERT: Number (38, 0) - A unique identifier for the financial institution assigned by the FDIC (Nullable: YES)

- ID_COUNTRY: Varchar (11) - A unique geographic identifier for the country where the bank is located (Nullable: YES)

- EMPLOYER_IDENTIFICATION_NUMBER: Varchar (16777216) - Employer identification number (EIN), a number assigned to a business by the Internal Revenue Service, effective 2008-12-31. (Nullable: YES)

- IS_ACTIVE: Date - Status of the bank to determine active or closed (Nullable: YES)

- NAICS_CODE: Varchar (16777216) - NAICS code of the primary activity conducted by an entity. (Nullable: YES)

- NAME: Varchar (16777216) - Name of the bank (Nullable: YES)

- LEGAL_ENTITY_IDENTIFIER: Varchar (16777216) - Code to identify a legally distinct entity that engages in a financial transaction. Issued by approved local operating units around the world in conjunction with the Global LEI Foundation. (Nullable: YES)

- ADDRESS: Varchar (16777216) - Stree-level address of the bank (Nullable: YES)

- ENTITY_TYPE: Varchar (85) - The institution grouping for the bank (National Bank, Non-member Bank, etc.) (Nullable: YES)

- STATE_ABBREVIATION: Varchar (16777216) - State of the bank (Nullable: YES)

- URL: Varchar (16777216) - Link to the bank website (Nullable: YES)

- OCC_ID: Number (38, 0) - A unique identifier for the financial institution assigned by the Office of the Comptroller of the Currency (Nullable: YES)

- ID_ZIP: Varchar (16777216) - A unique geographic identifier for the zip code where the bank is located (Nullable: YES)

- CATEGORY: Varchar (27) - Category for the entity (Nullable: YES)

- ID_STATE: Varchar (16777216) - A unique geographic identifier for the state where the bank is located (Nullable: YES)

- ZIP_CODE: Varchar (16777216) - Zip code of the bank (Nullable: YES)

- MAJORITY_OWNED_BY_MINORITY_OR_WOMEN: Varchar (23) - Indicates whether the entity is more than 50% owned by one or more minorities or women with identification of the minority. If the ownership is by a woman who is also a member of a minority, the item is coded as minority. Not all codes provided by the FFIEC data were mapped in the reference data (Nullable: YES)

- REASON_FOR_ENTITY_TERMINATION: Number (38, 0) - The circumstances under which an entity ceased to exist or an indicator that an entity failed but remained open. (Nullable: YES)

- FEDERAL_REGULATOR: Varchar (16777216) - The abbreviation for the banking regulator (OCC, FED, FDIC) (Nullable: YES)

- INSURER: Varchar (16777216) - Indicates whether an institution is insured under the Deposit Insurance Fund (DIF). (Nullable: YES)

- THRIFT_ID: Varchar (16777216) - A unique identifier for the financial institution assigned by the Office of Thrift Supervision, last 5 characters only (Nullable: YES)

- INTERNATIONAL_BANKING_FACILITY: Date - Indicates whether an entity has an International Banking Facility. (Nullable: YES)

- ID_RSSD: Number (38, 0) - A unique identifier assigned by the Federal Reserve for the financial institution (Nullable: YES)

- SPECIALIZATION_GROUP: Varchar (16777216) - Specialization Group from FDIC, defined as Asset Concentration Hierarchy (e.g., Agricultural Specialization) (Nullable: YES)

- START_DATE: Date - First date for which the bank was open (Nullable: YES)

- ID_COUNTY: Varchar (16777216) - A unique geographic identifier for the county where the bank is located (Nullable: YES)

- END_DATE: Date - Last date for which the bank was open. NULL if still active (Nullable: YES)

- CHARTER_TYPE: Varchar (55) - The particular charter assigned to the bank (Industrial Bank, Commercial Bank, etc.) (Nullable: YES)

- CITY: Varchar (16777216) - City of the bank (Nullable: YES)

- CHARTERING_AUTHORITY: Varchar (16777216) - The level of the chartering agency of the institution (State, Federal) (Nullable: YES)


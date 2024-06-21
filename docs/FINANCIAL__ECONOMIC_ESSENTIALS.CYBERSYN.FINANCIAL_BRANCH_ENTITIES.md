**Table 24: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_BRANCH_ENTITIES** (FINANCIAL_BRANCH_ENTITIES)

All bank branch locations in the United States, including a unique identifier for a branch (ID_RSSD) as well as detailed information on the branch's geographic location and parent institution.The Federal Financial Institutions Examination Council (FFIEC) is a U.S. government interagency body that prescribes uniform principles, standards, and report forms for the federal examination of financial institutions. It does not provide deposit insurance. The FFIEC provides detailed branch-level data for these institutions, which includes information on branch locations, deposits, and other financial metrics. This data is provided to support the public and regulatory oversight, promoting understanding and informed decision-making regarding the nation's financial systems and aiding in the assessment of local banking market conditions.Provides a wide format overview of bank branches monitored by the FFIEC by ID_RSSD.

- ID_ZIP: Varchar (16777216) - Unique identifier of the zip code where the entity is located (Nullable: YES)

- ID_COUNTY: Varchar (16777216) - Unique identifier of the county where the entity is located (Nullable: YES)

- STATE_ABBREVIATION: Varchar (16777216) - Abbreviation of the state the entity is physically located in (Nullable: YES)

- END_DATE: Date - Last date for which the branch was open. NULL if still active (Nullable: YES)

- ID_RSSD_PARENT: Number (38, 0) - Unique identifier for the head office of the entity if the entity is a branch (Nullable: YES)

- CATEGORY: Varchar (27) - Category of the entity for a given RSSD. Branch or bank (Nullable: YES)

- IS_ACTIVE: Date - Status of the branch to determine active or closed (Nullable: YES)

- BRANCH_NAME: Varchar (16777216) - Name of the banking branch (Nullable: YES)

- ID_STATE: Varchar (16777216) - Unique identifier of the state where the entity is located (Nullable: YES)

- ID_RSSD: Number (38, 0) - A unique identifier assigned by the Federal Reserve for the financial institution (Nullable: YES)

- ADDRESS_LINE2: Varchar (16777216) - Second line of the physical address at the street level (Nullable: YES)

- ADDRESS: Varchar (16777216) - First line of the physical address at the street level (Nullable: YES)

- START_DATE: Date - First date for which the branch was open (Nullable: YES)

- CITY: Varchar (16777216) - City the entity is physically located in (Nullable: YES)

- NAME_PARENT: Varchar (16777216) - Name of the parent bank (Nullable: YES)

- ZIP_CODE: Varchar (16777216) - Zip code the entity is physically located in (Nullable: YES)

- ID_COUNTRY: Varchar (11) - Unique identifier of the country where the entity is located (Nullable: YES)


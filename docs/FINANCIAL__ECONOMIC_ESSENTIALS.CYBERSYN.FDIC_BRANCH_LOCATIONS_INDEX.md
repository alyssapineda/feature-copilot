**Table 15: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FDIC_BRANCH_LOCATIONS_INDEX** (FDIC_BRANCH_LOCATIONS_INDEX)

Index of each FDIC banking institutions' branches.The Federal Deposit Insurance Corporation (FDIC) is an independent agency of the US government that insures deposits at banks and thrift institutions, up to an insured limit, and promotes the safety and soundness of these financial institutions by identifying, monitoring, and addressing risks. They monitor financial institutions at 3 levels: (1) holding company, (2) institution, and (3) branch. On an annual basis, they conduct the Summary of Deposits survey that gathers data on the deposits held at each FDIC-insured banks' branches (if the bank has at least one branch).Provides a wide format overview of each banking institutions' branches by FDIC_BRANCH_ID.The table includes an ID and name for each branch and its associated institution and holding company. It also includes branch-specific location information as well as institution-level regulatory and insurance data.

- GEO_ID_COUNTY: Varchar (16777216) - Geographic ID representing the county where the branch is physically located. Can be joined to the GEOGRAPHY_INDEX table. (Nullable: YES)

- INSTITUTION_CHARTER_AGENCY: Varchar (16777216) - The chartering agency of the institution that granted the license or charter for the institution to operate and regulates and supervises the financial and operational activities of that institution. (Nullable: YES)

- BRANCH_NUMBER: Varchar (16777216) - The branch's corresponding office number. (Nullable: YES)

- INSTITUTION_PRIMARY_INSURER: Varchar (16777216) - Primary insurer, insurance agent, or insurance status of an institution. (Nullable: YES)

- INSTITUTION_PRIMARY_ASSET_SPECIALIZATION: Varchar (16777216) - Description of a mutually exclusive industry classification grouping which indicates the institution's primary asset specialization. (Nullable: YES)

- GEO_ID_STATE: Varchar (16777216) - Geographic ID representing the state where the branch is physically located. Can be joined to the GEOGRAPHY_INDEX table. (Nullable: YES)

- BRANCH_NAME: Varchar (16777216) - Name of the branch (e.g., Magnolia Branch). (Nullable: YES)

- GEO_ID_CBSA: Varchar (16777216) - Geographic ID representing the core-based statistical area where the branch is physically located. Can be joined to the GEOGRAPHY_INDEX table. (Nullable: YES)

- FEDERAL_RESERVE_DISTRICT: Varchar (16777216) - Name of the Federal Reserve District where the institution is located. (Nullable: YES)

- INSTITUTION_MINORITY_DEPOSITORY_STATUS: Varchar (16777216) - Description of the regulatory status of the financial institution associated with the location. (Nullable: YES)

- ADDRESS: Varchar (16777216) - Street address at which the branch is physically located. (Nullable: YES)

- FDIC_INSTITUTION_ID: Varchar (16777216) - Unique FDIC ID of the institution that owns the branch. It is a unique number, sequentially added to the FDIC database for both banks and branches. This ID is updated with every merger or purchase of branches to reflect the most current owner. (Nullable: YES)

- RSSDHCR: Varchar (16777216) - Unique number assigned by the Federal Reserve Board (FRB) to the regulatory bank holding company of the institution. (Nullable: YES)

- RSSDID: Varchar (16777216) - Unique number assigned by the Federal Reserve Board (FRB) to the institution. (Nullable: YES)

- ESTABLISHED_DATE: Date - Date on which the branch began operations. (Nullable: YES)

- CHARTER_TYPE: Varchar (16777216) - Identifies whether an institution is federally or state chartered. (Nullable: YES)

- FDIC_CLASSIFICATION_CODE: Varchar (16777216) - A classification code assigned by the FDIC based on the institution's charter type (commercial bank or savings institution), charter agent (state or federal), Federal Reserve membership status (Fed member, Fed nonmember) and its primary federal regulator (state chartered institutions are subject to both federal and state supervision). (Nullable: YES)

- FDIC_REGIONAL_OFFICE: Varchar (16777216) - Name of the FDIC Regional Office that services the institution. (Nullable: YES)

- HOLDING_COMPANY_NAME: Varchar (16777216) - Name of the holding company for the institution (e.g., JPMorgan Chase & Co.). (Nullable: YES)

- ACQUIRED_DATE: Date - Date that a branch was last acquired by another institution. (Nullable: YES)

- INSTITUTION_PRIMARY_REGULATORY_AGENCY: Varchar (16777216) - Primary regulatory agency of the institution. (Nullable: YES)

- GEO_ID_ZIP: Varchar (16777216) - Geographic ID representing the zip code where the branch is physically located. Can be joined to the GEOGRAPHY_INDEX table. (Nullable: YES)

- LATITUDE: Date - Latitude of the branch's physical location. (Nullable: YES)

- LONGITUDE: Date - Longitude of the branch's physical location. (Nullable: YES)

- OTS_ID: Varchar (16777216) - Unique identification number assigned to institutions chartered by the Office of the Thrift Supervision (OTS) or that become members of the Federal Home Loan System. (Nullable: YES)

- MAIN_OFFICE_FLAG: Number (38, 0) - Flag identifying the main office for the institution. (Nullable: YES)

- GEO_ID_METRO_DIV: Varchar (16777216) - Geographic ID representing the metropolitan division where the branch is physically located. Can be joined to the GEOGRAPHY_INDEX table. (Nullable: YES)

- HOLDING_COMPANY_TYPE: Varchar (16777216) - Identifies the type of holding company associated with the branch. (Nullable: YES)

- INSTITUTION_NAME: Varchar (16777216) - Legal name of the FDIC Insured Institution (e.g., JPMorgan Chase Bank, National Association). (Nullable: YES)

- FDIC_INSTITUTION_CERTIFICATE_NUMBER: Varchar (16777216) - Unique number assigned by the FDIC used to identify institutions and for for the issuance of insurance certificates. (Nullable: YES)

- CITY: Varchar (16777216) - City at which the branch is physically located. (Nullable: YES)

- INSTITUTION_CATEGORY: Varchar (16777216) - Type of financial institution defined by its charter type, ownership structure, regulatory oversight, and other characteristics. (Nullable: YES)

- FDIC_BRANCH_ID: Varchar (16777216) - Unique FDIC ID for each bank branch. The branch ID for the Headquarters branch is the same as the branch ID for the entire bank or savings institution. (Nullable: YES)

- BRANCH_TYPE: Varchar (16777216) - Description of the branch's main function (e.g., Full Service Brick and Mortar Office). (Nullable: YES)

- COMPTROLLER_DISTRICT: Varchar (16777216) - Name of the Comptroller of the Currency district in which the institution is located. (Nullable: YES)


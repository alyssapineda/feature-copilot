**Table 32: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_INSTITUTION_HIERARCHY** (FINANCIAL_INSTITUTION_HIERARCHY)

Provides FDIC financial institution relationships, including parent and offspring IDs, institution categories, relationship types, percent control, and active status.The FDIC BankSuite provides a comprehensive array of financial data and reports on FDIC-insured institutions in the United States. This suite typically includes detailed information such as bank financial statements, call reports (quarterly financial reports filed by banks), and Uniform Bank Performance Reports (UBPRs) which analyze the financial condition and performance of individual banks.Provides a wide format breakdown of relationships between various levels of financial institutions by ID_RSSD_PARENT and ID_RSSD_OFFSPRING.Each row represents a unique relationship between two financial institutions, the category definition of each institution, the type of relationship and percent control, and whether the relationship is active.

- PARENT_CONTROLS_OFFSPRING: Date - Indication if the parent has direct control over the offspring (Nullable: YES)

- CATEGORY_PARENT: Varchar (27) - High-level category of successor entity legal structure (e.g., Bank Holding Company) (Nullable: YES)

- PERCENT_CONTROL_OF_OFFSPRING: Number (38, 0) - Parent percentage of controlling interest in the offspring (Nullable: YES)

- NAME_PARENT: Varchar (16777216) - Name of parent entity (Nullable: YES)

- CATEGORY_OFFSPRING: Varchar (27) - High-level category of successor entity legal structure (e.g., Branch, Bank) (Nullable: YES)

- ID_RSSD_PARENT: Number (38, 0) - Unique identifier for parent entity. Joinable to entities table (Nullable: YES)

- ACTIVE_OFFSPRING: Date - Flag to indicate if offspring is active (Nullable: YES)

- RELATIONSHIP_TERMINATED: Date - Indication if the relationship is still current (Nullable: YES)

- RELATIONSHIP_LEVEL: Varchar (16777216) - Description of the type of relationship between the two entities (Nullable: YES)

- ID_RSSD_OFFSPRING: Number (38, 0) - Unique identifier for offspring entity. Joinable to entities table (Nullable: YES)

- NAME_OFFSPRING: Varchar (16777216) - Name of offspring entity (Nullable: YES)

- ACTIVE_PARENT: Date - Flag to indicate if parent is active (Nullable: YES)


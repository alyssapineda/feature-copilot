**Table 31: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_INSTITUTION_EVENTS** (FINANCIAL_INSTITUTION_EVENTS)

Bank events data related to FDIC institutions, including splits, discontinued charters, asset sales, retained charters, and failures, with transaction dates and accounting methods.The FDIC BankSuite provides a comprehensive array of financial data and reports on FDIC-insured institutions in the United States. This suite typically includes detailed information such as bank financial statements, call reports (quarterly financial reports filed by banks), and Uniform Bank Performance Reports (UBPRs) which analyze the financial condition and performance of individual banks.The table includes ID_RSSDs for the predecessor and successor of different event types. Events include splits, discontinued charters, sale of assets, retained charters, and failures. It details the transaction date and the merge accounting method utilized.

- ID_RSSD_PREDECESSOR: Number (38, 0) - Unique identifier for predecessor entity joinable to entities table (Nullable: YES)

- MERGER_ACCOUNTING_METHOD_UTILIZED: Varchar (16777216) - Accounting method used in resolving a non-failure merger (Nullable: YES)

- TRANSACTION_DATE: Date - Date of transaction (Nullable: YES)

- NAME_PREDECESSOR: Varchar (16777216) - Name of predecessor entity (Nullable: YES)

- ID_RSSD_SUCCESSOR: Number (38, 0) - Unique identifier for successor entity joinable to entities table (Nullable: YES)

- ACTIVE_PREDECESSOR: Date - Flag to indicate if predecessor is active (Nullable: YES)

- NAME_SUCCESSOR: Varchar (16777216) - Name of successor entity (Nullable: YES)

- CATEGORY_SUCCESSOR: Varchar (27) - High-level category of successor entity legal structure (Nullable: YES)

- ACTIVE_SUCCESSOR: Date - Flag to indicate if successor is active (Nullable: YES)

- CATEGORY_PREDECESSOR: Varchar (27) - High-level category of predecessor entity legal structure (Nullable: YES)

- TRANSFORMATION_TYPE: Varchar (16777216) - Description of transformation (Nullable: YES)


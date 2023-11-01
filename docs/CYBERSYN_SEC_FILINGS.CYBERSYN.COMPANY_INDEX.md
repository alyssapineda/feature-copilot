**Table 9: CYBERSYN_SEC_FILINGS.CYBERSYN.COMPANY_INDEX** (Company Index Data)

This table contains information related to various companies, including their unique identifiers, regulatory IDs and other characteristics.

- COMPANY_NAME: Varchar (16777216) - The name of the company. (Nullable: YES)

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key, a unique identifier for corporations registered with the United States Securities and Exchange Commission (SEC). (Nullable: YES)

- EIN: Varchar (16777216) - Employer Identification Number, a unique identification number that is assigned to a business by the IRS. (Nullable: YES)

- PERMID_COMPANY_ID: Varchar (16777216) - Permanent Identifier, which is a identifier provided by Refinitive (via PermID) to provide a way to uniquely identify a company. (Nullable: YES)

- ENTITY_LEVEL: Varchar (9) - Describes the type or level of the entity for additional convenience. Potential values include 'brands' (Amazon Basics), 'merchants' (Amazon.com), and 'companies' (Amazon Inc.) (Nullable: YES)

- LEI: Date - Legal Entity Identifier, a unique identifier from GLEIF that identifies legal entities that engage in financial transactions. (Nullable: YES)


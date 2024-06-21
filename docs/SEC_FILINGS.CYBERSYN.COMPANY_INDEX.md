**Table 52: SEC_FILINGS.CYBERSYN.COMPANY_INDEX** (COMPANY_INDEX)

Compiled list of public and private companies with a unique Cybersyn company identifier (company_id) mapped to public identifiers like CIK, EIN, PermID, and LEI. This table serves as the spine for Cybersyn data that involves company-level identifiers.Cybersyn has compiled a list of public and private companies companies through various sources including from the Securities and Exchange Commission (SEC), PermID from Refinitiv, and Global Legal Entity Identifier Foundation (GLEIF). Each of these sources uses their own unique identifier for companies, and Cybersyn maps these IDs together to allow users to join datasets together using common unique identifiers. Cybersyn datasets that include company entities use the COMPANY_ID field as the unique ID for the company.The EIN (Employer Identification Number) is issued by the US Internal Revenue Service (IRS) and is a unique 9-digit number used to identify business entities for tax purposes. The CIK (Central Index Key) is issued by the US Securities and Exchange Commission (SEC) and is a unique number assigned to corporations, individuals, and foreign governments who are required to file disclosures with the SEC. The LEI (Legal Entity Identifier) is a 20-character, alpha-numeric code based on the ISO 17442 standard, assigned to distinct legal entities that engage in financial transactions and administered by the Global Legal Entity Identifier Foundation (GLEIF). The PERMID_COMPANY_ID is issued by PermID from Refinitiv and is a permanent identifier that they publish for organization entities.  Provides a wide format overview of companies by COMPANY_ID, which can be used across Cybersyn's datasets as a unique identifier for corporate entities.

- EIN: Varchar (16777216) - Employer Identification Number, a unique identification number that is assigned to a business by the IRS. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - The name of the company. (Nullable: YES)

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. (Nullable: YES)

- PRIMARY_EXCHANGE_CODE: Varchar (16777216) - The exchange code for the primary trading venue of a security. (Nullable: YES)

- PERMID_COMPANY_ID: Varchar (16777216) - Permanent Identifier, which is a identifier provided by Refinitiv (via PermID) to provide a way to uniquely identify a company. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key, a unique identifier for corporations registered with the United States Securities and Exchange Commission (SEC). (Nullable: YES)

- ENTITY_LEVEL: Varchar (16777216) - Describes the type or level of the entity for additional convenience. Currently, all entities are corporate entities and are denoted as 'Corporate'. (Nullable: YES)

- PRIMARY_EXCHANGE_NAME: Varchar (16777216) - The exchange name for the primary trading venue of a security. (Nullable: YES)

- LEI: Date - Legal Entity Identifier, a unique identifier from GLEIF that identifies legal entities that engage in financial transactions. (Nullable: YES)

- GLOBAL_TICKERS: Date - An array of ticker symbols under which the security may be traded globally on all exchanges. (Nullable: YES)

- PRIMARY_TICKER: Varchar (16777216) - The ticker for the primary trading venue of a security. If a security trades on multiple exchanges or has numerous tickers, an attempt is made to select the ticker from the home market. (Nullable: YES)


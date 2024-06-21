**Table 61: SEC_FILINGS.CYBERSYN.SEC_HOLDING_FILING_ATTRIBUTES** (SEC_HOLDING_FILING_ATTRIBUTES)

Disclosure of equity holdings by institutional investment managers with over $100 million in assets under management, provided in the Form 13-F on a quarterly basis by the SEC.The SEC assigns a unique number, Central Index Key (CIK), to all entities (companies, individuals, and foreign governments) who file disclosures with the SEC. A filing is assigned a unique identifier called an ADSH, or Accession Number. The Report entity represents individual filings with the SEC. Provides a wide format overview of an SEC filing by ADSH with associated CIK and OpenFIGI IDs.This table provides details on each 13-F filing to the SEC, including the securities' name, market value, number of shares, and OpenFIGI IDs.

- SECURITY_NAME: Varchar (16777216) - Name of the security or of the issuer of the security. (Nullable: YES)

- NUMBER_OF_SHARES: Number (38, 0) - Number of shares held. When NULL, the principal amount was disclosed instead, and can be found in the principal_amount column. (Nullable: YES)

- ASSET_CLASS: Varchar (16777216) - Broad-based class of the asset, such as 'Equity', 'Muni', etc. (Nullable: YES)

- INVESTMENT_DISCRETION: Varchar (14) - One of shared-defined, sole, or shared-other. Denotes the nature of the investment discretion for this holding by the filing manager. (Nullable: YES)

- SECURITY_TYPE: Varchar (16777216) - The type of security, such as "Common Stock" for equities. Securities can fall into multiple categories such as when a company has both tradable shares of Common Stock and an ADR. (Nullable: YES)

- OPENFIGI_COMPOSITE_ID: Date - Array of the country-level composite FIGI ID(s) for the security. In cases where there is a share class FIGI (global ID) and the security is tradable in more than one country there may be multiple composite IDs associated with a single security. (Nullable: YES)

- PRINCIPAL_AMOUNT: Number (38, 0) - The principal amount held. When NULL, the number of shares was disclosed instead, and can be found in the number_of_shares column. (Nullable: YES)

- HOLDER_CIK: Varchar (16777216) - Central Index Key (CIK) of the holding manager. (Nullable: YES)

- OPENFIGI_FIGI_ID: Date - Array of the FIGI (Financial Instrument Global Identifier) ID(s) for the security. In cases where there is a share class FIGI (global ID) or composite FIGI (country-level ID) because a security trades across multiple countries or exchanges, there may be multiple FIGI IDs associated with a single security. (Nullable: YES)

- MARKET_VALUE: Number (38, 0) - Market value of the security held in USD. (Nullable: YES)

- TOP_LEVEL_OPENFIGI_ID_TYPE: Varchar (16777216) - The highest level of the OpenFIGI ID in the hierarchy for the security held. The hierarchy follows the order "share class FIGI" (global) > "composite FIGI" (country-level) > "FIGI" (exchange-level). For example, if the highest level of ID (recorded in TOP_LEVEL_OPENFIGI_ID) is the composite FIGI, then this will be equal to 'openfigi_composite_id'. (Nullable: YES)

- TOP_LEVEL_OPENFIGI_ID: Varchar (16777216) - OpenFIGI ID of the highest, most widely encompassing level for a particular security. The hierarchy follows the order "share class FIGI" (global) > "composite FIGI" (country-level) > "FIGI" (exchange-level). (Nullable: YES)

- PUTCALL: Varchar (16777216) - One of Put, Call, or NULL. When disclosed as Put or Call, the security is held as a put option or call option, respectively. (Nullable: YES)

- ADSH: Varchar (16777216) - Unique accession number for the filing. Can be used to join to the sec_holding_filing_index table. (Nullable: YES)

- PRIMARY_TICKER: Varchar (16777216) - The ticker for the primary trading venue of a security. If a security trades on multiple exchanges or has numerous tickers, an attempt is made to select the ticker from the home market. (Nullable: YES)

- OPENFIGI_SHARE_CLASS_ID: Date - The global share class FIGI ID(s) for the security. This is meant to be the most broad classification in the FIGI classification hierarchy. (Nullable: YES)

- PERMID_SECURITY_ID: Varchar (16777216) - PermID for the security. (Nullable: YES)


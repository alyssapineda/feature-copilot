**Table 12: CYBERSYN_SEC_FILINGS.CYBERSYN.OPENFIGI_SECURITY_INDEX** (Open Financial Instrument Global Identifier (FIGI) Security Index Data)

This table contains information related to information about financial securities, their identifiers, trading data, and classifications, especially in the context of the Financial Instrument Global Identifier (FIGI) system

- GLOBAL_TICKERS: Date - An array of ticker symbols under which the security may be traded globally on all exchanges. (Nullable: YES)

- PRIMARY_TICKER: Varchar (16777216) - The ticker for the primary trading venue of a security. If a security trades on multiple exchanges or has numerous tickers, an attempt is made to select the ticker from the home market. (Nullable: YES)

- SECURITY_TYPE: Date - The type of security, such as "Common Stock" for equities. Securities can fall into multiple categories such as when a company has both tradable shares of Common Stock and an ADR. (Nullable: YES)

- SECURITY_SUBTYPE: Date - Sub-type of the security, providing further classification. Like SECURITY_TYPE, securities can also have multiple subtypes. (Nullable: YES)

- EXCHANGE_CODES: Date - Codes representing the exchanges where the security is traded. An empty array means that exchange information is not available. (Nullable: YES)

- ASSET_CLASS: Varchar (16777216) - Broad-based class of the asset, such as 'Equity', 'Muni', etc. (Nullable: YES)

- SECURITY_NAME: Varchar (16777216) - Name of the security. (Nullable: YES)

- OPENFIGI_FIGI_ID: Date - Array of the FIGI (Financial Instrument Global Identifier) ID(s) for the security. In cases where there is a share class FIGI (global ID) or composite FIGI (country-level ID) becase a security trades across multiple countries or exchanges, there may be multiple FIGI IDs associated with a single security. (Nullable: YES)

- TOP_LEVEL_OPENFIGI_ID_TYPE: Varchar (23) - The highest level of the OpenFIGI ID in the hierarchy for the security held. The hierarchy follows the order "share class FIGI" (global) > "composite FIGI" (country-level) > "FIGI" (exchange-level). For example, if the highest level of ID (recorded in TOP_LEVEL_OPENFIGI_ID) is the composite FIGI, then this will be equal to 'openfigi_composite_id'. (Nullable: YES)

- OPENFIGI_COMPOSITE_ID: Date - Array of the country-level composite FIGI ID(s) for the security. In cases where there is a share class FIGI (global ID) and the security is tradable in more than one country there may be multiple composite IDs associated with a single security. (Nullable: YES)

- OPENFIGI_SHARE_CLASS_ID: Date - The global share class FIGI ID(s) for the security. This is meant to be the most broad classification in the FIGI classification hierarchy. (Nullable: YES)

- TOP_LEVEL_OPENFIGI_ID: Varchar (16777216) - OpenFIGI ID of the highest, most widely encompassing level for a particular security. The hierarchy follows the order "share class FIGI" (global) > "composite FIGI" (country-level) > "FIGI" (exchange-level). (Nullable: YES)


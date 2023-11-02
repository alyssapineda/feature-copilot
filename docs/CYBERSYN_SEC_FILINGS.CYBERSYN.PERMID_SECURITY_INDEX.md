**Table 13: CYBERSYN_SEC_FILINGS.CYBERSYN.PERMID_SECURITY_INDEX** (Permanent ID Security Index Data)

This table contains information related to comprehensive information about financial securities, including their names, trading venues, asset class, status, exchange codes, unique PermID identifiers, and tickers

- SECURITY_NAME: Varchar (16777216) - Name of the security. (Nullable: YES)

- PRIMARY_EXCHANGE_NAME: Varchar (16777216) - The exchange name for the primary trading venue of a security. (Nullable: YES)

- ASSET_CLASS: Varchar (28) - Broad-based class of the asset, such as 'Ordinary Shares', 'Depositary Receipts', etc. (Nullable: YES)

- SECURITY_STATUS: Varchar (8) - Status of the security, i.e. 'Active' or 'Inactive'. An active security is a security that has active quotes and an inactive security has no active quotes. This status changes over time. (Nullable: YES)

- EXCHANGE_CODE: Date - An array of codes representing the exchanges where the security is traded. An empty array means that exchange information is not available. (Nullable: YES)

- PRIMARY_EXCHANGE_CODE: Varchar (16777216) - The exchange code for the primary trading venue of a security. (Nullable: YES)

- PERMID_QUOTE_ID: Date - An array of PermIDs for the quotes for each exchange where the security is traded. An empty array means that quote information is not available. (Nullable: YES)

- PERMID_SECURITY_ID: Varchar (16777216) - PermID for the security. (Nullable: YES)

- PRIMARY_TICKER: Varchar (16777216) - The ticker for the primary trading venue of a security. If a security trades on multiple exchanges or has numerous tickers, an attempt is made to select the ticker from the home market. (Nullable: YES)

- GLOBAL_TICKERS: Date - An array of ticker symbols under which the security may be traded globally on all exchanges. (Nullable: YES)


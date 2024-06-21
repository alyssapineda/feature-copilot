**Table 59: SEC_FILINGS.CYBERSYN.SEC_CIK_INDEX** (SEC_CIK_INDEX)

Map between company identifiers (including Cybersyn's COMPANY_ID) and the SEC Central Index Keys (CIKs), along with geographic and industry classification details for SEC filers.The SEC assigns a unique number, Central Index Key (CIK), to all entities (companies, individuals, and foreign governments) who file disclosures with the SEC. SIC, or Standard Industrial Classification, is a four-digit code provided by the SEC to classify the primary industry of a company. Originally developed by the U.S. government in the 1930s, SIC codes are used to categorize companies and facilitate the analysis of economic activities across government and private sectors.

- EIN: Varchar (16777216) - Employee Identification Number assigned by the Internal Revenue Service (IRS) (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - Name of registrant. This corresponds to the name of the legal entity as of the latest filing date. (Nullable: YES)

- SIC_CODE_CATEGORY: Varchar (16777216) - Standard Industrial Classification (SIC) code category. (Nullable: YES)

- COUNTRY: Varchar (16777216) - The country of the registrant. (Nullable: YES)

- CITY: Varchar (16777216) - The city of the registrant. (Nullable: YES)

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. (Nullable: YES)

- COUNTRY_GEO_ID: Varchar (16777216) - A unique identifier of the country where the business is headquartered. Joinable to the GEOGRAPHY_INDEX table (Nullable: YES)

- STATE_GEO_ID: Varchar (16777216) - A unique identifier of the state where the business is headquartered. Joinable to the GEOGRAPHY_INDEX table (Nullable: YES)

- SIC_CODE_DESCRIPTION: Varchar (16777216) - Standard Industrial Classification (SIC) code description. (Nullable: YES)

- SIC: Varchar (16777216) - Standard Industrial Classification (SIC). Code assigned by the SEC indicating the registrant industry group. (Nullable: YES)

- STATE: Varchar (16777216) - The state or province of the registrant. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)


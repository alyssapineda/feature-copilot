**Table 14: CYBERSYN_SEC_FILINGS.CYBERSYN.SEC_CIK_INDEX** (U.S. Securities and Exchange Commission (SEC) Central Index Key (CIK) Index Data)

This table contains information related to information about companies, including their identifiers, geographic details, SIC codes, industry classifications, and tax-related information.

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. (Nullable: YES)

- STATE: Varchar (16777216) - The state or province of the registrant. (Nullable: YES)

- CIK: Varchar (16777216) - Central Index Key (CIK). Ten digit number assigned by the SEC to each registrant that submits filings. (Nullable: YES)

- SIC: Varchar (16777216) - Standard Industrial Classification (SIC). Code assigned by the SEC indicating the registrant industry group. (Nullable: YES)

- CITY: Varchar (16777216) - The city of the registrant. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - Name of registrant. This corresponds to the name of the legal entity as of the latest filing date. (Nullable: YES)

- SIC_CODE_CATEGORY: Varchar (16777216) - Standard Industrial Classification (SIC) code category. (Nullable: YES)

- STATE_GEO_ID: Varchar (16777216) - A unique identifier of the state where the business is headquartered. Joinable to the GEOGRAPHY_INDEX table (Nullable: YES)

- EIN: Varchar (16777216) - Employee Identification Number assigned by the Internal Revenue Service (IRS) (Nullable: YES)

- SIC_CODE_DESCRIPTION: Varchar (16777216) - Standard Industrial Classification (SIC) code description. (Nullable: YES)

- COUNTRY: Varchar (16777216) - The country of the registrant. (Nullable: YES)

- COUNTRY_GEO_ID: Varchar (16777216) - A unique identifier of the country where the business is headquartered. Joinable to the GEOGRAPHY_INDEX table (Nullable: YES)


**Table 8: CYBERSYN_SEC_FILINGS.CYBERSYN.COMPANY_CHARACTERISTICS** (Company Characteristics Data)

This table contains information related to characteristics or attributes of various companies.

- VALUE: Varchar (16777216) - The value related to the relationship type or characteristics specified. (Nullable: YES)

- RELATIONSHIP_TYPE: Varchar (16777216) - Specifies the kind of relationship or characteristic that is being reported in the VALUE field. (Nullable: YES)

- RELATIONSHIP_END_DATE: Date - The ending of characteristics being valid for a given company. In cases where a characteristic is currently valid, an end date of NULL is assigned. (Nullable: YES)

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - The name of the company. (Nullable: YES)

- RELATIONSHIP_START_DATE: Date - The beginning of characteristics taking effect for a given company. In cases where a characteristic pre-dates the beginning of the data, a start date of NULL is assigned. (Nullable: YES)


**Table 51: SEC_FILINGS.CYBERSYN.COMPANY_CHARACTERISTICS** (COMPANY_CHARACTERISTICS)

Characteristics for nearly 100k companies, including EIN, CIK, LEI, address information, industry descriptions, and more, with start and end date ranges, by Cybersyn's COMPANY_ID. This table serves as a compliment to the company_index table, which is the spine for Cybersyn data that involves company-level identifiers.Provides a long format overview of characteristics associated with a particular COMPANY_ID.This table includes a unique ID for each company (COMPANY_ID) and associated categorical characteristics (EIN, CIK, LEI, address information, industry descriptions, and more). A characteristic may be temporal with start and end dates indicating the range for which the data is valid.

- RELATIONSHIP_START_DATE: Date - The beginning of characteristics taking effect for a given company. In cases where a characteristic pre-dates the beginning of the data, a start date of NULL is assigned. (Nullable: YES)

- RELATIONSHIP_TYPE: Varchar (16777216) - Specifies the kind of relationship or characteristic that is being reported in the VALUE field. (Nullable: YES)

- VALUE: Varchar (16777216) - The value related to the relationship type or characteristics specified. (Nullable: YES)

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - The name of the company. (Nullable: YES)

- RELATIONSHIP_END_DATE: Date - The ending of characteristics being valid for a given company. In cases where a characteristic is currently valid, an end date of NULL is assigned. (Nullable: YES)


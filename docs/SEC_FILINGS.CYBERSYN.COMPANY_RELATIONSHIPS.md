**Table 53: SEC_FILINGS.CYBERSYN.COMPANY_RELATIONSHIPS** (COMPANY_RELATIONSHIPS)

Company subsidiary and parent relationships, joinable to Cybersyn's company_index table.

- RELATED_COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to the related company. Joinable to the COMPANY_INDEX table. (Nullable: YES)

- RELATIONSHIP_END_DATE: Date - The ending of the relationship being valid for the company and the related company. In cases where a relationship is currently valid, an end date of NULL is assigned. (Nullable: YES)

- RELATED_COMPANY_NAME: Varchar (16777216) - The name of the related company. (Nullable: YES)

- ENTITY_LEVEL: Varchar (16777216) - Describes the type or level of the entity for additional convenience. Currently, all entities are corporate entities and are denoted as 'Corporate'. (Nullable: YES)

- COMPANY_ID: Varchar (32) - Unique identifier assigned by Cybersyn to each company. Joinable to the COMPANY_INDEX table. (Nullable: YES)

- RELATIONSHIP_START_DATE: Date - The beginning of a company being associated with the related company. In cases where the start date is unknown, NULL is assigned. (Nullable: YES)

- RELATIONSHIP_TYPE: Varchar (10) - Specifies the kind of relationship between the company and the related company. The value is 'Parent' when the company is the parent of the related company and 'Subsidiary' when the company is a subsidiary of the related company. (Nullable: YES)

- RELATED_ENTITY_LEVEL: Varchar (16777216) - Describes the type or level of the related entity for additional convenience. Currently, all entities are corporate entities and are denoted as 'Corporate'. (Nullable: YES)

- COMPANY_NAME: Varchar (16777216) - The name of the company. (Nullable: YES)


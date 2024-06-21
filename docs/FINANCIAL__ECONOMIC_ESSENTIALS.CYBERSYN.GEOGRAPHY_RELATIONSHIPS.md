**Table 38: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.GEOGRAPHY_RELATIONSHIPS** (GEOGRAPHY_RELATIONSHIPS)

The Geography Relationships table provides details on relationships between geographic entities of differing levels. This table includes relationships of type 'overlaps' and type 'contains'. For example, it provides a GEO_ID for a zip code that overlaps with a city, and it details a GEO_ID for a state that contains a particular census tract.

- GEO_NAME: Varchar (16777216) - Full name of the place (Nullable: YES)

- RELATED_GEO_NAME: Varchar (16777216) - Name of the place related to GEO_NAME. This is a place that overlaps or is contained within the primary geo (e.g., city within a state) (Nullable: YES)

- GEO_ID: Varchar (16777216) - A unique identifier for a place joinable to the GEOGRAPHY_INDEX table (Nullable: YES)

- RELATED_GEO_ID: Varchar (16777216) - A unique identifier for the related place joinable to the GEOGRAPHY_INDEX table (Nullable: YES)

- LEVEL: Varchar (16777216) - Geographic level or hierarchy (e.g., Country, State, County, City, Continent, CountrySubRegion, etc.) (Nullable: YES)

- RELATIONSHIP_TYPE: Varchar (16777216) - Relationship between the two places. Contains means the RELATED_GEO_ID is fully contained within the GEO_ID (e.g., relationship of state to a city) while Overlaps indicates the GEO_ID is a subpart of the RELATED_GEO_ID (e.g., relationship of city to a state) (Nullable: YES)

- RELATED_LEVEL: Varchar (16777216) - Geographic level or hierarchy of the related place (e.g., Country, State, County, City, Continent, CountrySubRegion, etc.) (Nullable: YES)


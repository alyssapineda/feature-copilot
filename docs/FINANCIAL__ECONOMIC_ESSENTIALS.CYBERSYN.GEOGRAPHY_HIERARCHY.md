**Table 35: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.GEOGRAPHY_HIERARCHY** (GEOGRAPHY_HIERARCHY)

The Geography Hierarchy table provides hierarchical relationships between a PARENT_GEO_ID and GEO_ID (e.g., country/USA is parent to geoID/01, which is representative of the state of Alabama).

- PARENT_GEO_ID: Varchar (16777216) - GEO_ID from GEOGRAPHY_INDEX table for the parent geography (Nullable: YES)

- GEO_ID: Varchar (16777216) - GEO_ID from GEOGRAPHY_INDEX table for the child geography (Nullable: YES)


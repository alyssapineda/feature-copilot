**Table 25: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FINANCIAL_CFPB_COMPLAINT** (FINANCIAL_CFPB_COMPLAINT)

Daily-updated consumer complaints about financial products and services, including company responses and complaint details, dating back to December 2011, from the CFPB.The Consumer Financial Protection Bureau (CFPB) publishes the Consumer Complaints Database that provides complaint information for companies by product category, receipt, and company response timeliness by consumer's zip code and state. It serves as a valuable tool for understanding consumer challenges in the financial marketplace and for monitoring how financial institutions address these issues. The data is updated daily and dates back to Dec 1, 2011.Provides a wide format overview of each complaint submitted to the CFPB.The table provides information on each complaint, including the product, issue, associated company, complaint narrative, public response from the company, and complaint submission details.

- ID_ZIP: Varchar (16777216) - a unique identifier of the mailing zip code provided by the consumer (Nullable: YES)

- PRODUCT: Varchar (16777216) - type of product identified by the consumer in the complaint.  Product categories were consolidated by the CFPB in 2017 (Nullable: YES)

- CONSUMER_CONSENT_PROVIDED: Varchar (16777216) - Identifies consumer consent in publishing their complaint narrative (Nullable: YES)

- SUB_PRODUCT: Varchar (16777216) - type of sub-product identified by the consumer in the complaint.  Sub-product categories were consolidated by the CFPB in 2017 (Nullable: YES)

- ISSUE: Varchar (16777216) - type of issue identified by the consumer in the complaint.  The categorical issues available for selection have evolved over time (Nullable: YES)

- COMPANY_RESPONSE_TO_CONSUMER: Varchar (16777216) - Company explanation of how the issue was closed, selected from a list (Nullable: YES)

- ID_STATE: Varchar (16777216) - a unique identifier of the mailing state provided by the consumer (Nullable: YES)

- ZIP_CODE: Varchar (16777216) - mailing zip code provided by the consumer (Nullable: YES)

- COMPANY: Varchar (16777216) - Company identified by the consumer in the complaint. (Nullable: YES)

- TAGS: Varchar (16777216) - Categorical data supporting easier searching of complaints submitted by or on behalf of consumers, includes "Older American" and "Servicemember" (Nullable: YES)

- SUB_ISSUE: Varchar (16777216) - type of sub-issue identified by the consumer in the complaint.  The categorical sub-issues available for selection have evolved over time (Nullable: YES)

- CONSUMER_COMPLAINT_NARRATIVE: Varchar (16777216) - The consumer-submitted description of the complaint, with PII scrubbed by the CFPB.  Consumers must opt-in and can opt out at any time (Nullable: YES)

- DATE_SENT_TO_COMPANY: Date - Date the CFPB sent the complaint to the company (Nullable: YES)

- STATE: Varchar (16777216) - mailing state provided by the consumer (Nullable: YES)

- DATE_RECEIVED: Date - Date the CFPB received the complaint (Nullable: YES)

- SUBMITTED_VIA: Varchar (16777216) - How the complaint was submitted (Nullable: YES)

- COMPANY_PUBLIC_RESPONSE: Varchar (16777216) - The optional, public-facing response to a consumer complaint chosen by the company from a list (Nullable: YES)

- TIMELY_RESPONSE: Date - Indicates whether the company gave a timely response (Nullable: YES)

- CONSUMER_DISPUTED: Varchar (16777216) - Whether the consumer disputed the company response.  After April 24, 2017 the Bureau discontinued this option and this field is marked N/A (Nullable: YES)


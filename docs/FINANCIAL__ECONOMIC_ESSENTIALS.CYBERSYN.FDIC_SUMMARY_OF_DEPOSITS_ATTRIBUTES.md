**Table 16: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FDIC_SUMMARY_OF_DEPOSITS_ATTRIBUTES** (FDIC_SUMMARY_OF_DEPOSITS_ATTRIBUTES)

Deposit data for FDIC-insured bank branches, including deposit amounts, branch locations, and institution details, released annually.The Federal Deposit Insurance Corporation (FDIC) is an independent agency of the US government that insures deposits at banks and thrift institutions, up to an insured limit, and promotes the safety and soundness of these financial institutions by identifying, monitoring, and addressing risks. They monitor financial institutions at 3 levels: (1) holding company, (2) institution, and (3) branch. On an annual basis, they conduct the Summary of Deposits survey that gathers data on the deposits held at each FDIC-insured banks' branches (if the bank has at least one branch).Provides a wide format breakdown of variables included in the fdic_summary_of_deposits_timeseries table.

- FREQUENCY: Varchar (6) - How often the data is aggregated (e.g., Annual). (Nullable: YES)

- VARIABLE_NAME: Varchar (16777216) - Human-readable description of the financial data variables tracked by the FDIC. (Nullable: YES)

- MEASURE: Varchar (16777216) - Quantifiable attribute being recorded (e.g., Domestic Deposits). (Nullable: YES)

- UNIT: Varchar (16777216) - Unit in which the measure is recorded (e.g., USD YTD). (Nullable: YES)

- MEASUREMENT_TYPE: Varchar (16777216) - Classification indicating the level at which the variable is tracked by the FDIC, either at the "Institution" or "Branch" level. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique FDIC identifier for tracked financial data. (Nullable: YES)


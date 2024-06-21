**Table 17: FINANCIAL__ECONOMIC_ESSENTIALS.CYBERSYN.FDIC_SUMMARY_OF_DEPOSITS_TIMESERIES** (FDIC_SUMMARY_OF_DEPOSITS_TIMESERIES)

Deposit data for FDIC-insured bank branches, including deposit amounts, branch locations, and institution details, released annually.The Federal Deposit Insurance Corporation (FDIC) is an independent agency of the US government that insures deposits at banks and thrift institutions, up to an insured limit, and promotes the safety and soundness of these financial institutions by identifying, monitoring, and addressing risks. They monitor financial institutions at 3 levels: (1) holding company, (2) institution, and (3) branch. On an annual basis, they conduct the Summary of Deposits survey that gathers data on the deposits held at each FDIC-insured banks' branches (if the bank has at least one branch).Each row represents a distinct timeseries, date, and value by FDIC institution and branch. Each variable is detailed in the fdic_summary_of_deposits_attributes table.

- VARIABLE_NAME: Varchar (16777216) - Human-readable description of the financial data variables tracked by the FDIC. (Nullable: YES)

- DATE: Date - Date associated with the value. (Nullable: YES)

- UNIT: Varchar (16777216) - Unit in which the measure is recorded (e.g., USD YTD). (Nullable: YES)

- FDIC_INSTITUTION_ID: Varchar (16777216) - Unique FDIC ID of the institution that owns the branch. It is a unique number, sequentially added to the FDIC database for both banks and branches. This ID is updated with every merger or purchase of branches to reflect the most current owner. (Nullable: YES)

- VARIABLE: Varchar (16777216) - Unique FDIC identifier for tracked financial data. (Nullable: YES)

- FDIC_BRANCH_ID: Varchar (16777216) - FDIC's unique number for the bank or savings institution assigned by the FDIC in order to identify and track. The branch ID for the Headquarters branch is the same as the branch ID for the entire bank or savings institution. (Nullable: YES)

- VALUE: Number (38, 0) - Value reported for the variable. (Nullable: YES)


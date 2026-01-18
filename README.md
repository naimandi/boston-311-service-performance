# Boston 311 Service Request Analysis and Visualization

### Purpose 
This project focuses on KPI and metric visualization to evaluate service-level agreement (SLA) compliance for municipal 311 service requests in the City of Boston. The analysis examines overall performance as well as time-based trends, including resolution times, , case volume, and geographic pattern.

### Data 
Source: Boston Open Data Portal – 311 Service Requests
https://data.boston.gov/dataset/311-service-requests

### Steps 
- `download.py`: Downloads yearly Boston 311 CSV files directly from the Boston Open Data portal and stores them locally.
-  `merge.py`: Merges raw yearly CSV files into a single consolidated dataset.
-  `clean.ipynb`: This script reads the merged Boston 311 dataset and performs data quality assessment and cleaning to prepare it for analysis.
-  `eda.ipynb`: Performs exploratory data analysis on the cleaned Boston 311 dataset and prepares pre-aggregated tables for Tableau dashboards. It parses dates, computes SLA compliance, and summarizes time-based trends such as case volume, median resolution times, and SLA compliance over time. It also aggregates overall performance metrics, top departments, top request types, and neighborhood-level SLA data over all years. All results are saved as CSV files ready for Tableau, allowing interactive dashboards without heavy data processing. Python visualizations are used to verify trends and distributions before export.

Tableau Project Links:

## Interactive Dashboards

- [311 Service Requests Dashboard — Overall Performance](https://public.tableau.com/shared/YBT6363G8?:display_count=n&:origin=viz_share_link)  
- [311 Service Requests Dashboard — Yearly Trends ](https://public.tableau.com/shared/6P56PKBSX?:display_count=n&:origin=viz_share_link)

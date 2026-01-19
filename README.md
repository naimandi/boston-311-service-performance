# Boston 311 Service Request Analysis and Visualization

### Purpose 
This project analyzes Boston 311 service request data to track and visualize key aspects of service performance, including case volume trends, resolution times, SLA compliance, overdue cases, department-level performance, and neighborhood-level service outcomes. Interactive dashboards created in Tableau allow exploration of both time-based trends and overall service patterns.

### Data 
Source: Boston Open Data Portal – 311 Service Requests
https://data.boston.gov/dataset/311-service-requests

### Steps 
- `download.py`: Downloads yearly Boston 311 CSV files directly from the Boston Open Data portal and stores them locally.
-  `merge.py`: Merges raw yearly CSV files into a single consolidated dataset.
-  `clean.ipynb`: This script reads the merged Boston 311 dataset and performs data quality assessment and cleaning to prepare it for analysis.
-  `eda.ipynb`: Performs exploratory data analysis on the cleaned Boston 311 dataset and prepares pre-aggregated tables for Tableau dashboards. It parses dates, computes SLA compliance, and summarizes time-based trends such as case volume, median resolution times, and SLA compliance over time. It also aggregates overall performance metrics, top departments, top request types, and neighborhood-level SLA data over all years. All results are saved as CSV files ready for Tableau, allowing interactive dashboards without heavy data processing. Python visualizations are used to verify trends and distributions before export.


## Tableau Dashboards

- [Boston 311 Service Requests Dashboard — Overall Analysis](https://public.tableau.com/shared/RPF8W69CF?:display_count=n&:origin=viz_share_link)  
- [Boston 311 Service Requests Dashboard — Yearly Trends ](https://public.tableau.com/views/Boston311ServiceRequestVisualizations/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

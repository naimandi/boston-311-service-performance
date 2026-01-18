# TODO
## Data Analysis + Visualization Using Python and Tableau

### Purpose 
This project focuses on KPI visualization and analysis to evaluate service-level agreement (SLA) compliance for municipal 311 service requests in the City of Boston. The analysis examines overall performance as well as time-based trends, including resolution times, overdue behavior, case volume, and geographic pattern

### Data 
Source: Boston Open Data Portal – 311 Service Requests
https://data.boston.gov/dataset/311-service-requests

### Steps 
- `download.py`: Downloads yearly Boston 311 CSV files directly from the Boston Open Data portal and stores them locally.
-  `merge.py`: Merges raw yearly CSV files into a single consolidated dataset.
-  `clean.ipynb`: TODO
-  `eda.ipynb`: TODO This script does .. Because Tableau Public has data-size constraints, I pre-aggregated the dataset in Python to produce analysis-ready KPI tables. This also ensured that Tableau was used for visualization and storytelling rather than heavy data processing.
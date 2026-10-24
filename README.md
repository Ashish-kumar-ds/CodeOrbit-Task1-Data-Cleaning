# Task 1 — Data Cleaning in Excel/Python

**Internship:** CodeOrbit Tech — Data Analyst Internship  
**Project:** Customer Dataset Cleaning using Python and Pandas  
**Author:** Ashish Kumar

## Objective
Clean a synthetic customer dataset by handling duplicate rows, missing values, inconsistent text formatting, numeric types, and mixed/invalid dates.

## Technologies
Python 3.10+, Pandas, CSV, Excel.

## Project files
- `data/sample_customer_data.csv` — original dataset with intentional data-quality issues
- `data_cleaning.py` — reproducible cleaning code
- `output/cleaned_customer_data.csv` — cleaned dataset
- `output/cleaning_log.csv` — cleaning steps and counts
- `output/cleaning_summary.txt` — run summary
- `output/cleaned_data_preview.txt` — preview of cleaned records
- `Task1_Data_Cleaning_Workbook.xlsx` and `docs/Task1_Data_Cleaning_Report.pdf` — included in the downloadable project ZIP
- `docs/cleaning_steps.md` — cleaning explanation
- `docs/demo_video_script.md` — recording guide
- `SUBMISSION_CHECKLIST.md` — final submission checklist

## Setup and run
1. Install Python 3.10 or newer.
2. Open a terminal in this repository folder.
3. Run `pip install -r requirements.txt`.
4. Run `python data_cleaning.py`.
5. Review the generated files in `output/`.

## Cleaning approach
1. Remove exact duplicate rows.
2. Trim spaces and standardize names/cities and email addresses.
3. Convert Age and Purchase_Amount to numeric values.
4. Fill missing Age and Purchase_Amount using medians.
5. Fill missing City with `Unknown` and Email with `Not Provided`.
6. Normalize valid dates to `YYYY-MM-DD`; mark invalid dates as `Unknown`.
7. Sort records and validate missing cells.

## Results
- Original rows: 15
- Exact duplicate rows removed: 1
- Final rows: 14
- Remaining missing cells: 0

## Data note
The dataset is synthetic. Median imputation is a simplified teaching choice; confirm cleaning rules with the data owner for real datasets.

## Repository
https://github.com/Ashish-kumar-ds/CodeOrbit-Task1-Data-Cleaning
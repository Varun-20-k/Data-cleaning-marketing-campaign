# Data-cleaning-marketing-campaign
Data cleaning and preprocessing of the Marketing Campaign dataset using Python (Pandas)/Excel.
# 🧹 Data Cleaning and Preprocessing — Marketing Campaign Dataset

## 🎯 Objective
Clean and preprocess a raw dataset containing missing values, duplicates, and inconsistent formats.

## 📊 Dataset
- Source: Customer Personality Analysis / Marketing Campaign Dataset (Kaggle)
- Rows: 2240
- Columns: 29

## 🧰 Tools Used
- Python 3
- Pandas
- Jupyter Notebook

## 🧪 Steps Performed
1. Loaded the dataset using Pandas.
2. Handled missing values — filled 24 missing 'Income' values using the median.
3. Removed duplicates (none found).
4. Standardized text columns (`Education`, `Marital_Status`).
5. Converted `Dt_Customer` to date format (`dd-mm-yyyy`).
6. Renamed columns to lowercase with underscores.
7. Fixed data types for numeric columns.
8. Saved cleaned dataset for further analysis.

## 📈 Results
| Step | Result |
|------|---------|
| Missing values handled | Yes |
| Duplicates removed | 0 |
| Columns renamed | 29 |
| Final rows | 2240 |

## 📄 Deliverables
- `data_cleaning.ipynb`
- `cleaned_marketing_campaign.csv`
- `Data_Cleaning_Report.pdf`

## 👨‍💻 Author
Varun K — Final Year Engineering Student  



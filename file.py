# ----------------------------------------------
# 🧹 DATA CLEANING AND PREPROCESSING SCRIPT
# Dataset: Marketing Campaign
# Author: Varun K (Data Analytics Project)
# ----------------------------------------------

# ✅ Import required libraries
import pandas as pd

# ----------------------------------------------
# 1️⃣ Load Dataset
# ----------------------------------------------
# Replace with your file name if needed
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# View basic info
print("Initial Dataset Info:")
print(df.info(), "\n")

# ----------------------------------------------
# 2️⃣ Check for Missing Values
# ----------------------------------------------
print("Missing values before cleaning:")
print(df.isnull().sum(), "\n")

# Fill missing Income values with the median
df['Income'].fillna(df['Income'].median(), inplace=True)

# ----------------------------------------------
# 3️⃣ Remove Duplicates
# ----------------------------------------------
duplicates_count = df.duplicated().sum()
print(f"Duplicates found: {duplicates_count}")
df.drop_duplicates(inplace=True)

# ----------------------------------------------
# 4️⃣ Standardize Text Values
# ----------------------------------------------
# Clean and format Education and Marital_Status
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()

# ----------------------------------------------
# 5️⃣ Convert Date Columns
# ----------------------------------------------
# Convert Dt_Customer to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

# ----------------------------------------------
# 6️⃣ Rename Columns
# ----------------------------------------------
# Make all column names lowercase and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ----------------------------------------------
# 7️⃣ Fix Data Types
# ----------------------------------------------
# Ensure numerical columns are correctly typed
df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

# ----------------------------------------------
# 8️⃣ Verify Cleaning Results
# ----------------------------------------------
print("Missing values after cleaning:")
print(df.isnull().sum(), "\n")

print("Dataset Summary After Cleaning:")
print(df.info(), "\n")

# ----------------------------------------------
# 9️⃣ Save Cleaned Data
# ----------------------------------------------
cleaned_file = "cleaned_marketing_campaign.csv"
df.to_csv(cleaned_file, index=False)

print(f"✅ Cleaned dataset saved as '{cleaned_file}'")



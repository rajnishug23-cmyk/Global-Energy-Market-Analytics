import pandas as pd
import os

# ==========================================================
# GLOBAL ENERGY MARKET RESEARCH & ANALYTICS
# Step 1: Load and Clean Energy Dataset
# ==========================================================

print("Starting energy data cleaning...")

# ----------------------------------------------------------
# 1. Check whether the dataset exists
# ----------------------------------------------------------

input_file = "owid-energy-data.csv"

if not os.path.exists(input_file):
    print("\nERROR: Dataset not found!")
    print("Please make sure this file exists:")
    print("data/owid-energy-data.csv")
    exit()

# ----------------------------------------------------------
# 2. Load the dataset
# ----------------------------------------------------------

print("Loading energy dataset...")

df = pd.read_csv(input_file)

print("Original shape:", df.shape)

# ----------------------------------------------------------
# 3. Select useful columns
# ----------------------------------------------------------

columns = [
    "country",
    "year",
    "population",
    "gdp",
    "primary_energy_consumption",
    "oil_production",
    "gas_production",
    "coal_production",
    "oil_consumption",
    "gas_consumption",
    "coal_consumption",
    "renewables_consumption",
    "renewables_electricity",
    "solar_electricity",
    "wind_electricity",
    "hydro_electricity",
    "nuclear_electricity"
]

# Keep only columns that actually exist
available_columns = []

for column in columns:
    if column in df.columns:
        available_columns.append(column)

df = df[available_columns]

print("Selected columns:", len(available_columns))

# ----------------------------------------------------------
# 4. Remove duplicate rows
# ----------------------------------------------------------

df = df.drop_duplicates()

print("Duplicates removed.")

# ----------------------------------------------------------
# 5. Convert year to numeric
# ----------------------------------------------------------

df["year"] = pd.to_numeric(
    df["year"],
    errors="coerce"
)

# ----------------------------------------------------------
# 6. Convert numerical columns
# ----------------------------------------------------------

numeric_columns = [
    column
    for column in df.columns
    if column not in ["country", "year"]
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

print("Numerical columns converted.")

# ----------------------------------------------------------
# 7. Remove rows without country or year
# ----------------------------------------------------------

df = df.dropna(
    subset=["country", "year"]
)

# ----------------------------------------------------------
# 8. Sort the dataset
# ----------------------------------------------------------

df = df.sort_values(
    by=["country", "year"]
)

# ----------------------------------------------------------
# 9. Create output folder
# ----------------------------------------------------------

os.makedirs("data", exist_ok=True)

# ----------------------------------------------------------
# 10. Save cleaned dataset
# ----------------------------------------------------------

output_file = "data/cleaned_energy_data.csv"

df.to_csv(
    output_file,
    index=False
)

# ----------------------------------------------------------
# 11. Display results
# ----------------------------------------------------------

print("\n========================================")
print("CLEANING COMPLETED SUCCESSFULLY")
print("========================================")

print("\nOriginal dataset shape:")
print(df.shape)

print("\nCleaned dataset saved at:")
print(output_file)

print("\nFirst 5 rows:")
print(df.head())

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())
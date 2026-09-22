import pandas as pd
import sqlite3
import os

# ==========================================================
# GLOBAL ENERGY MARKET RESEARCH & ANALYTICS
# Step 3: SQL Analysis using SQLite
# ==========================================================

print("Starting SQL analysis...")

# ----------------------------------------------------------
# 1. Load cleaned data
# ----------------------------------------------------------

input_file = "data/cleaned_energy_data.csv"

df = pd.read_csv(input_file)

print("Cleaned dataset loaded.")
print("Rows:", len(df))

# ----------------------------------------------------------
# 2. Create output folder
# ----------------------------------------------------------

os.makedirs("output", exist_ok=True)

# ----------------------------------------------------------
# 3. Create SQLite database
# ----------------------------------------------------------

database_file = "output/energy_market.db"

connection = sqlite3.connect(database_file)

# Load dataframe into SQLite
df.to_sql(
    "energy_data",
    connection,
    if_exists="replace",
    index=False
)

print("Dataset loaded into SQLite database.")

# ----------------------------------------------------------
# 4. Query latest data for selected countries
# ----------------------------------------------------------

query = """
SELECT
    country,
    year,
    primary_energy_consumption,
    oil_production,
    gas_production,
    coal_production
FROM energy_data
WHERE country IN (
    'India',
    'United States',
    'China',
    'Germany',
    'United Kingdom'
)
AND year = (
    SELECT MAX(year)
    FROM energy_data
)
ORDER BY primary_energy_consumption DESC;
"""

result = pd.read_sql_query(
    query,
    connection
)

# ----------------------------------------------------------
# 5. Save SQL result
# ----------------------------------------------------------

output_file = "output/sql_country_analysis.csv"

result.to_csv(
    output_file,
    index=False
)

# ----------------------------------------------------------
# 6. Close database
# ----------------------------------------------------------

connection.close()

# ----------------------------------------------------------
# 7. Display results
# ----------------------------------------------------------

print("\n========================================")
print("SQL ANALYSIS COMPLETED SUCCESSFULLY")
print("========================================")

print("\nLatest country comparison:")

print(result.to_string(index=False))

print("\nSQL result saved at:")
print(output_file)

print("\nSQLite database saved at:")
print(database_file)
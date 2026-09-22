import pandas as pd
import os

# ==========================================================
# GLOBAL ENERGY MARKET RESEARCH & ANALYTICS
# Step 2: Energy Market Analysis
# ==========================================================

print("Starting energy market analysis...")

# ----------------------------------------------------------
# 1. Load cleaned data
# ----------------------------------------------------------

input_file = "data/cleaned_energy_data.csv"

df = pd.read_csv(input_file)

print("Dataset loaded successfully.")
print("Shape:", df.shape)

# ----------------------------------------------------------
# 2. Create output folder
# ----------------------------------------------------------

os.makedirs("output", exist_ok=True)

# ----------------------------------------------------------
# 3. Global Energy Production Analysis
# ----------------------------------------------------------

production_columns = [
    "year",
    "oil_production",
    "gas_production",
    "coal_production"
]

available_production = [
    column for column in production_columns
    if column in df.columns
]

global_data = df[
    df["country"] == "World"
].copy()

if not global_data.empty:

    global_production = global_data[
        available_production
    ].copy()

    global_production = global_production.sort_values(
        "year"
    )

    global_production.to_csv(
        "output/global_energy_production.csv",
        index=False
    )

    print("\nGlobal production analysis completed.")

else:
    print("\nWorld-level data not found.")

# ----------------------------------------------------------
# 4. Selected Country Analysis
# ----------------------------------------------------------

countries = [
    "India",
    "United States",
    "China",
    "Germany",
    "United Kingdom"
]

country_data = df[
    df["country"].isin(countries)
].copy()

country_columns = [
    "country",
    "year",
    "primary_energy_consumption",
    "oil_production",
    "gas_production",
    "coal_production",
    "renewables_consumption",
    "solar_electricity",
    "wind_electricity",
    "hydro_electricity",
    "nuclear_electricity"
]

available_country_columns = [
    column
    for column in country_columns
    if column in country_data.columns
]

country_comparison = country_data[
    available_country_columns
].copy()

country_comparison = country_comparison.sort_values(
    ["country", "year"]
)

country_comparison.to_csv(
    "output/country_energy_comparison.csv",
    index=False
)

print("Country comparison completed.")

# ----------------------------------------------------------
# 5. Renewable Energy Analysis
# ----------------------------------------------------------

renewable_columns = [
    "country",
    "year",
    "renewables_consumption",
    "renewables_electricity",
    "solar_electricity",
    "wind_electricity",
    "hydro_electricity",
    "nuclear_electricity"
]

available_renewable_columns = [
    column
    for column in renewable_columns
    if column in df.columns
]

renewable_data = df[
    df["country"] == "World"
].copy()

if not renewable_data.empty:

    renewable_analysis = renewable_data[
        available_renewable_columns
    ].copy()

    renewable_analysis = renewable_analysis.sort_values(
        "year"
    )

    renewable_analysis.to_csv(
        "output/global_renewable_energy.csv",
        index=False
    )

    print("Renewable energy analysis completed.")

# ----------------------------------------------------------
# 6. Latest Country Data
# ----------------------------------------------------------

latest_year = country_data["year"].max()

latest_country_data = country_data[
    country_data["year"] == latest_year
].copy()

latest_country_data = latest_country_data[
    available_country_columns
]

latest_country_data.to_csv(
    "output/latest_country_energy.csv",
    index=False
)

print("Latest country comparison completed.")

# ----------------------------------------------------------
# 7. Display latest results
# ----------------------------------------------------------

print("\n========================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("========================================")

print("\nLatest year available:", int(latest_year))

print("\nLatest country energy data:")

print(
    latest_country_data[
        [
            column
            for column in [
                "country",
                "primary_energy_consumption",
                "oil_production",
                "gas_production",
                "coal_production"
            ]
            if column in latest_country_data.columns
        ]
    ].to_string(index=False)
)

print("\nFiles created:")

print("1. output/global_energy_production.csv")
print("2. output/country_energy_comparison.csv")
print("3. output/global_renewable_energy.csv")
print("4. output/latest_country_energy.csv")
import pandas as pd 

from config import RAW_DATA_FILE

EXPECTED_COLUMNS ={
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "medin_income",
    "medin_house_value",
    "ocean_proximity",
}

KNOWN_OCEAN_CATEGORIES = ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]

COUNT_COLUMNS = ["total_rooms", "population", "households"]



def validate_data(df):
    problems = []

    if len(df) == 0 : 
        problems.append("The table is empty.")
        return problems

    missing_columns = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing_columns:
        problems.append(f"Missing columns: {missing_columns}")
        return problems


    if not df["latitude"].between(32,42.5).all():
        problems.append("Some latitude values are outside California.")
    if not df["longitude"].between(-125,-114).all():
        problems.append("Some longitude values are outside California.")

    for column in COUNT_COLUMNS:
        if (df[column] <= 0).any():
            problems.append(f"Column {column} has zero or nagative  values.")

    if (df["median_income"] <= 0).any():
        problems.append("median_house_value has zero or neagtive values.")

    if (df["median_house_value"] <= 0).any():
        problems.append("median_house_value has zero or negative values.")

    unknown = set(df["ocean_proximity"].dropna().unique()) - set(KNOWN_OCEAN_CATEGORIES)
    if unknown:
        problems.append(f"Unknown ocean_proximity categories: {sorted(unknown)}")

    too_many_bedrooms = df["total_bedrooms"] > df["totla_rooms"]
    if too_many_bedrooms.any():
        problems.append(f"{too_many_bedrooms.sum()} rows have more bedrooms than rooms.")

    if not df["housing_median_age"].between(1,52).all():
        problems.append("housing_median_age must be between 1 and 52.")

    
    return problems
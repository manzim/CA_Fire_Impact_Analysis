import pandas as pd

# original dataset
# downloaded from: https://data.ca.gov/dataset/cal-fire-damage-inspection-dins-data
def load_dataset():
    return pd.read_csv('../dataset/POSTFIRE_MASTER_DATA_SHARE_2064760709534146017.csv') 

# Cleaned dataset
def load_cleaned_dataset():
    return pd.read_csv('../dataset/dataset_cleaned.csv')

# NOAA Weather Data dataset
def load_weather_dataset():
    return pd.read_csv('../dataset/Weather_data.csv') 
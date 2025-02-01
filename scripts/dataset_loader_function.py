import pandas as pd

def load_dataset():
    return pd.read_csv('../dataset/POSTFIRE_MASTER_DATA_SHARE_2064760709534146017.csv')  # Correct

def load_cleaned_dataset():
    return pd.read_csv('../dataset/dataset_cleaned.csv')
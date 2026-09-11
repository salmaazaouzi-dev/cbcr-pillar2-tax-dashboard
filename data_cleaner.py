import pandas as pd
from data_loader import load_raw_data


def clean_data():
    """Loads raw data, selects relevant columns, and handles missing values."""
    df = load_raw_data()

    # Define relevant columns
    columns_to_keep = [
        "parent_name",
        "TAX_PAID",
        "TAX_ACCRUED",
        "ASSETS",
        "STATED_CAPITAL",
        "EARNINGS",
        "EMPLOYEES",
    ]

    # Keep available columns and fill nulls
    available_cols = [col for col in columns_to_keep if col in df.columns]
    df_cleaned = df[available_cols].copy()
    df_cleaned = df_cleaned.fillna(0)

    print(
        f"--> Data cleaned successfully. Remaining shape: {df_cleaned.shape}"
    )
    return df_cleaned

if __name__ == "__main__":
    df_clean = clean_data()
    # Cette ligne doit être décalée à l'intérieur du bloc :
    df_clean.to_csv("cbcr_cleaned_data.csv", index=False)
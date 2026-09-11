import os
import pandas as pd


def load_raw_data():
    """Finds and loads the raw CbCR CSV dataset."""
    csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]

    if not csv_files:
        raise FileNotFoundError("No raw CSV dataset found in the directory.")

    file_name = csv_files[0]
    print(f"--> Loading raw file: '{file_name}'...")
    df = pd.read_csv(file_name)
    return df


if __name__ == "__main__":
    df = load_raw_data()
    print(f"Data loaded successfully with {len(df)} rows.")
    print(f"Columns: {list(df.columns)}")
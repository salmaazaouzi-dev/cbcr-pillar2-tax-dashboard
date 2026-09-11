import os
import pandas as pd

# Load CSV file
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

if csv_files:
    df = pd.read_csv(csv_files[0])

    # 1. Clean missing values
    df['TAX_PAID'] = df['TAX_PAID'].fillna(0)
    df['EARNINGS'] = df['EARNINGS'].fillna(0)

    # 2. Calculate Effective Tax Rate (ETR %)
    # ETR = (TAX_PAID / EARNINGS) * 100
    # Avoid division by zero when EARNINGS <= 0
    df['EFFECTIVE_TAX_RATE'] = df.apply(
        lambda row: (row['TAX_PAID'] / row['EARNINGS'] * 100) if row['EARNINGS'] > 0 else 0, 
        axis=1
    )

    # 3. Display summary of calculated ETR
    print("--- Effective Tax Rate (ETR) Summary (%) ---")
    print(df['EFFECTIVE_TAX_RATE'].describe().round(2))

    # 4. Save cleaned dataset with calculated indicators
    output_file = "processed_tax_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\nProcessed data saved successfully to '{output_file}'!")

else:
    print("Error: No CSV file found.")
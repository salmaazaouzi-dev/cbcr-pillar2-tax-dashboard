import pandas as pd
from data_cleaner import clean_data


def calculate_metrics():
    """Calculates Effective Tax Rate (ETR %) and basic indicators."""
    # 1. Load cleaned data from our clean_data() module
    df = clean_data()

    # 2. S'assurer que 'parent_name' / 'PARENT_NAME' est bien conservé
    # (Si la casse diffère dans clean_data, on normalise le nom de la colonne)
    for col in df.columns:
        if col.lower() == "parent_name":
            df.rename(columns={col: "PARENT_NAME"}, inplace=True)

    # 3. Calculate Effective Tax Rate (ETR %) safely
    # Formula: ETR = (TAX_PAID / EARNINGS) * 100
    df["EFFECTIVE_TAX_RATE"] = df.apply(
        lambda row: (row["TAX_PAID"] / row["EARNINGS"] * 100)
        if row["EARNINGS"] > 0
        else 0,
        axis=1,
    )

    print("--> Financial metrics calculated successfully.")
    return df


if __name__ == "__main__":
    df_metrics = calculate_metrics()
    print("\n--- Sample Calculated ETR Data ---")
    
    # Affichage de contrôle incluant PARENT_NAME
    preview_cols = [c for c in ["PARENT_NAME", "TAX_PAID", "EARNINGS", "EFFECTIVE_TAX_RATE"] if c in df_metrics.columns]
    print(df_metrics[preview_cols].head())

    # Exporter le fichier complet avec PARENT_NAME et l'ETR calculé
    df_metrics.to_csv("cbcr_metrics.csv", index=False)
    print("--> File 'cbcr_metrics.csv' exported successfully with PARENT_NAME!")
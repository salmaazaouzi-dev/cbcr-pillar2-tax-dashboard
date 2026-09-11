import pandas as pd
from metrics_calculator import calculate_metrics


def generate_summary_stats():
    """Generates summary statistics for key financial metrics and Effective Tax Rates (ETR)."""
    df = calculate_metrics()

    # حساب الإحصائيات الوصفية
    stats = df.describe()

    print("--> Summary statistics generated successfully.")
    return stats


if __name__ == "__main__":
    df_stat = generate_summary_stats()
    print("\n--- Summary Statistics for Financial Metrics and ETR ---")
    print(df_stat[["TAX_PAID", "EARNINGS", "EFFECTIVE_TAX_RATE"]].round(2))

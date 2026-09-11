import streamlit as st
from metrics_calculator import calculate_metrics
from stats_reporter import generate_summary_stats

st.set_page_config(page_title="Fiscal Transparency & ETR Dashboard", layout="wide")
page_title=st.title("Fiscal Transparency & ETR Dashboard")

@st.cache_data
def load_data():
    """Load and process data for the dashboard."""
    df_metrics = calculate_metrics()
    df_stats = generate_summary_stats()
    return df_metrics, df_stats

df_metrics, df_stats = load_data()
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", f"{len(df_metrics):,}")
col2.metric(
    "Average ETR", f"{df_metrics['EFFECTIVE_TAX_RATE'].mean():.2f}%"
)
col3.metric(
    "Median ETR", f"{df_metrics['EFFECTIVE_TAX_RATE'].median():.2f}%"
)

st.markdown("---")

tab1, tab2 = st.tabs(["Data Explorer", "Summary Statistics"])

with tab1:
    st.subheader("Data Explorer")
    st.dataframe(df_metrics, use_container_width=True)

with tab2:
    st.subheader("Summary Statistics")
    st.dataframe(
        df_stats[["TAX_PAID", "EARNINGS", "EFFECTIVE_TAX_RATE"]].round(2),
        use_container_width=True,
    )
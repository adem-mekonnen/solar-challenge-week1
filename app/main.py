import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- Page Configuration ---
# Use st.set_page_config() as the first Streamlit command.
st.set_page_config(
    page_title="Solar Potential Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Data Loading Function with Caching ---
@st.cache_data # Decorator to cache the data, improving performance
def load_data():
    """
    Loads cleaned data for all countries from the 'data/' directory.
    Constructs a robust file path independent of where the script is run.
    Returns a single concatenated DataFrame or None if files are not found.
    """
    countries = ['benin', 'sierra_leone', 'togo']
    all_dfs = []
    
    # Get the directory of the current script (main.py)
    script_dir = os.path.dirname(__file__)
    
    for country in countries:
        # Construct a robust path to the CSV file
        file_path = os.path.join(script_dir, '..', 'data', f'{country}_clean.csv')
        
        try:
            df = pd.read_csv(file_path, parse_dates=['Timestamp'])
            df['country'] = country.replace('_', ' ').title()
            all_dfs.append(df)
        except FileNotFoundError:
            st.error(f"Error: Cleaned data for {country.title()} not found at `{file_path}`. "
                     "Please ensure you have run the EDA for all countries (Task 2).")
            return None

    if all_dfs:
        return pd.concat(all_dfs, ignore_index=True)
    return None

# Load the data
df_all = load_data()

# --- Main Dashboard UI ---

st.title("☀️ Solar Potential Across West Africa")
st.markdown("An interactive dashboard for analyzing solar irradiance and environmental data to identify high-potential regions for solar investment.")

# Only display the dashboard if the data has been successfully loaded
if df_all is not None:
    
    # --- Sidebar for User Inputs ---
    st.sidebar.header("Filter Options")
    
    available_countries = df_all['country'].unique().tolist()
    
    # Widget to select multiple countries
    selected_countries = st.sidebar.multiselect(
        "Select Countries for Comparison:",
        options=available_countries,
        default=available_countries # All countries are selected by default
    )

    # Filter the DataFrame based on user's selection
    df_filtered = df_all[df_all['country'].isin(selected_countries)]

    st.markdown("---")

    # --- Main Content Area ---

    # Display plots only if at least one country is selected
    if not df_filtered.empty:
        
        # Create two columns for a side-by-side layout
        col1, col2 = st.columns(2)

        with col1:
            # 1. Boxplot of GHI (as required)
            st.subheader("Global Horizontal Irradiance (GHI) Distribution")
            fig, ax = plt.subplots()
            sns.boxplot(x='country', y='GHI', data=df_filtered, palette='viridis', ax=ax)
            ax.set_xlabel("Country")
            ax.set_ylabel("GHI (W/m²)")
            ax.tick_params(axis='x', rotation=15)
            st.pyplot(fig)

        with col2:
            # 2. Bar chart of average GHI (Bonus plot)
            st.subheader("Average GHI Ranking")
            avg_ghi = df_filtered.groupby('country')['GHI'].mean().sort_values(ascending=False)
            fig, ax = plt.subplots()
            avg_ghi.plot(kind='bar', ax=ax, color=sns.color_palette('viridis', len(avg_ghi)))
            ax.set_ylabel("Average GHI (W/m²)")
            ax.set_xlabel("Country")
            ax.tick_params(axis='x', rotation=15)
            st.pyplot(fig)

        st.markdown("---")

        # 3. Top Regions Table (Summary Statistics)
        st.subheader("Summary Statistics for Selected Countries")
        summary_metrics = ['GHI', 'DNI', 'DHI', 'Tamb']
        summary_table = df_filtered.groupby('country')[summary_metrics].agg(['mean', 'median', 'std'])
        st.dataframe(summary_table.style.format("{:.2f}"))

        st.markdown("---")
        
        # 4. Time Series Plot
        st.subheader("Daily Average GHI Over Time")
        df_daily_avg = df_filtered.set_index('Timestamp').groupby('country')['GHI'].resample('D').mean().reset_index()
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.lineplot(data=df_daily_avg, x='Timestamp', y='GHI', hue='country', ax=ax)
        ax.set_xlabel("Date")
        ax.set_ylabel("Daily Average GHI (W/m²)")
        st.pyplot(fig)

    else:
        st.warning("Please select at least one country from the sidebar to view the analysis.")

else:
    st.error("Dashboard could not be loaded. Please check the data loading errors above.")
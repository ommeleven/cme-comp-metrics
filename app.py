import streamlit as st
from utils.helper_functions import display_trader_performance, display_trade_log, visualize_overview, df
from about import about_page  # Correctly importing the function

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a Page", ["Dashboard", "About"])

if page == "Dashboard":
    st.title("Trader Performance Dashboard")

    # Dropdown to select a trader
    trader_name = st.selectbox("Select Trader by Name", options=[""] + list(df["Trader Name"].unique()))

    if trader_name:
        # Display trader-specific performance and trade log
        display_trader_performance(trader_name)
        display_trade_log(trader_name)

    # Visualize overview of all traders
    st.markdown("---")
    st.subheader("Overview of All Traders")
    visualize_overview()

elif page == "About":
    # Call the about_page function
    about_page()

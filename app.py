import streamlit as st
from utils.helper_functions import display_trader_performance, display_trade_log, visualize_overview, df

st.title("Trader Performance Dashboard")

# Dropdown to select a trader
trader_name = st.selectbox("Select Trader by Name", options=[""] + list(df["Trader Name"].unique()))

if trader_name:
    display_trader_performance(trader_name)
    display_trade_log(trader_name)

# Visualize overview of all traders
visualize_overview()

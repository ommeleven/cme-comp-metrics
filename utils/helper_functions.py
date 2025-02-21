import matplotlib.pyplot as plt # type: ignore
import pandas as pd
import streamlit as st
import plotly.express as px # type: ignore

# Sample data
data = {
    "Trader Name": ["ArtArtArtArt", "Jordan Belfort", "Dani Nikolov", "Emma D", "Fatima Afolabi", "JEFE"],
    "Symbol": ["CL", "ES", "GC", "MNQ", "RTY", "ES"],
    "Side": ["Buy", "Buy", "Sell", "Buy", "Buy", "Buy"],
    "Filled Qty": [1, 5, 5, 10, 2, 4],
    "Avg Price": [75.82, 6134.75, 2744.3, 21559.65, 2303.9, 6123.25],
    "Close Price": [76.15, 4100, 1910, 2225, 2150, 4100],
    "Net Profit/Loss (USD)": [0.33, -500, -834, -100, 0.15, -200],
    "Total Duration (hrs)": [2, 3, 2, 4, 2.5, 3],
    "Max Drawdown (USD)": [-20, -50, -100, -30, -15, -40],
    "Avg Profit per Trade (USD)": [0.33, -100, -167, -10, 0.075, -50],
    "Avg Holding Time (hrs)": [1, 0.5, 0.6, 0.4, 0.3, 0.8]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

def display_trader_performance(trader_name):
    trader_data = df[df["Trader Name"] == trader_name]
    if trader_data.empty:
        st.write("Trader not found.")
        return

    st.subheader(f"Performance of {trader_name}")
    st.write(trader_data)

    # Metrics Visualization
    fig, ax = plt.subplots(2, 2, figsize=(10, 8))

    # Profit/Loss bar chart
    ax[0, 0].bar(trader_data['Symbol'], trader_data['Net Profit/Loss (USD)'], color='blue')
    ax[0, 0].set_title("Net Profit/Loss (USD)")
    ax[0, 0].set_xlabel("Symbol")
    ax[0, 0].set_ylabel("Net Profit/Loss (USD)")

    # Total Duration bar chart
    ax[0, 1].bar(trader_data['Symbol'], trader_data['Total Duration (hrs)'], color='green')
    ax[0, 1].set_title("Total Duration (hrs)")
    ax[0, 1].set_xlabel("Symbol")
    ax[0, 1].set_ylabel("Duration (hrs)")

    # Max Drawdown bar chart
    ax[1, 0].bar(trader_data['Symbol'], trader_data['Max Drawdown (USD)'], color='red')
    ax[1, 0].set_title("Max Drawdown (USD)")
    ax[1, 0].set_xlabel("Symbol")
    ax[1, 0].set_ylabel("Max Drawdown (USD)")

    # Avg Profit per Trade bar chart
    ax[1, 1].bar(trader_data['Symbol'], trader_data['Avg Profit per Trade (USD)'], color='purple')
    ax[1, 1].set_title("Avg Profit per Trade (USD)")
    ax[1, 1].set_xlabel("Symbol")
    ax[1, 1].set_ylabel("Avg Profit per Trade (USD)")

    plt.tight_layout()
    st.pyplot(fig)


def display_trade_log(trader_name):
    trader_data = df[df["Trader Name"] == trader_name]
    if trader_data.empty:
        st.write("Trader not found.")
        return

    st.subheader(f"Trade Log for {trader_name}")
    st.write(trader_data[['Trader Name', 'Symbol', 'Side', 'Filled Qty', 'Avg Price', 'Close Price', 'Net Profit/Loss (USD)']])

def visualize_overview():
    st.subheader("Overview of All Traders' Performance")
    fig = px.bar(df, x='Trader Name', y='Net Profit/Loss (USD)', color='Trader Name', title="Overall Performance of Traders")
    st.plotly_chart(fig)

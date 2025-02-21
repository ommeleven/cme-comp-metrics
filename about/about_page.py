import streamlit as st

def about_page():
    st.title("About the Trader Performance Metrics")

    st.write("""
    This dashboard evaluates trader performance using a variety of metrics that help understand trading behaviors, efficiency, and profitability. 
    Below are descriptions of key metrics displayed in this app:
    """)

    metrics = [
        {
            "Metric": "Total Trades",
            "Formula": "COUNT(Trades)",
            "Description": "The total number of trades executed by the trader.",
            "Inputs Needed": "A list of all trades made by the trader. Count the total number of trades."
        },
        {
            "Metric": "Net Profit",
            "Formula": "SUM(Profit/Loss)",
            "Description": "The total profit or loss from all trades combined.",
            "Inputs Needed": "A list of profit/loss for each individual trade. Add up all the profits and losses from each trade."
        },
        {
            "Metric": "Max Drawdown",
            "Formula": "MAX(Equity Curve Drawdown)",
            "Description": "The largest peak-to-trough decline in the trader’s equity curve.",
            "Inputs Needed": "A series of data points for the trader’s equity after each trade. Calculate peak-to-trough declines."
        },
        {
            "Metric": "Avg Profit per Trade",
            "Formula": "Net Profit / Total Trades",
            "Description": "The average profit per trade executed by the trader.",
            "Inputs Needed": "Net Profit: The total profit/loss from all trades. Total Trades: The total number of trades."
        },
        {
            "Metric": "Total Duration (hrs)",
            "Formula": "SUM(Trade Duration in hours)",
            "Description": "The total time spent on all trades, in hours.",
            "Inputs Needed": "A list of all trade durations in hours. Add up the durations of all trades."
        },
        {
            "Metric": "Trade Frequency",
            "Formula": "Total Trades / Trading Days",
            "Description": "The frequency of trades executed by the trader, typically per day.",
            "Inputs Needed": "Total Trades: The total number of trades. Trading Days: The number of trading days."
        },
        {
            "Metric": "Avg Holding Time",
            "Formula": "AVG(Trade Holding Time)",
            "Description": "The average duration of time that trades are held from entry to exit.",
            "Inputs Needed": "A list of holding times for each individual trade (i.e., time between opening and closing of each trade)."
        },
        {
            "Metric": "Market Adaptability",
            "Formula": "Calculate Adaptability Score",
            "Description": "Measures how well the trader adapts to changing market conditions.",
            "Inputs Needed": "Market conditions, such as volatility, price movements, and the trader’s response to them."
        },
        {
            "Metric": "ARS",
            "Formula": "(((Profit per Trade) * Avg Profit) / Total Drawdown) * Market Exposure",
            "Description": "A weighted score reflecting profitability relative to drawdown, adjusted by market exposure.",
            "Inputs Needed": "Profit per Trade, Avg Profit, Total Drawdown, Market Exposure."
        },
        {
            "Metric": "PER",
            "Formula": "Relative Performance vs Market",
            "Description": "Measures the trader’s performance compared to the market's performance over time.",
            "Inputs Needed": "Historical market data and the trader’s performance data."
        },
        {
            "Metric": "TMI",
            "Formula": "Trailing Market Index",
            "Description": "A trailing index that tracks the market’s performance.",
            "Inputs Needed": "Market data over time to compare the trader's performance to market performance."
        },
        {
            "Metric": "RSQ",
            "Formula": "R-Squared between trades and market movements",
            "Description": "Measures the correlation between the trader’s trades and the broader market movements.",
            "Inputs Needed": "Historical data of both the trader’s trades and the market’s price movements over the same period."
        },
        {
            "Metric": "VAI",
            "Formula": "Volatility Adjusted Income",
            "Description": "A measure of profitability adjusted for market volatility.",
            "Inputs Needed": "Profit: Total profit/loss. Volatility: Market volatility over the period."
        },
        {
            "Metric": "EPI",
            "Formula": "Exponential Profit Index",
            "Description": "A weighted profit index that gives more weight to recent profits.",
            "Inputs Needed": "Recent Profits: Profits in the most recent trades. All Profits: Total profits over time."
        },
        {
            "Metric": "MAC",
            "Formula": "Market Adaptation Coefficient",
            "Description": "A coefficient that measures how well a trader adapts to market changes, incorporating volatility.",
            "Inputs Needed": "Market conditions, price volatility, and the trader’s responsiveness to changes."
        }
    ]

    # Display metrics in expandable sections
    for metric in metrics:
        with st.expander(metric["Metric"]):
            st.markdown(f"**Formula:**  \n`{metric['Formula']}`")
            st.markdown(f"**Description:**  \n{metric['Description']}")
            st.markdown(f"**Inputs Needed:**  \n{metric['Inputs Needed']}")
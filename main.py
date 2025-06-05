# main.py
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from analysis import indicators  
import pandas as pd

st.title("📈 Financial Dashboard")


tickers = st.text_input("Enter ticker(s), separated by comma", "AAPL,TSLA")


tickers = [t.strip().upper() for t in tickers.split(",") if t.strip()]

start_date = st.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2024-12-31"))

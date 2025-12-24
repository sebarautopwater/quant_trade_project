import yfinance as yf
import pandas as pd

def load_data(symbol, start):
    df = yf.download(symbol, start=start)
    df = df[["Close"]].copy()
    df["returns"] = df["Close"].pct_change()
    return df
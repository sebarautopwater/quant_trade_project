def trend_signal(df, short_window=50, long_window=200):
    df = df.copy()

    df["ma_short"] = df["Close"].rolling(short_window).mean()
    df["ma_long"] = df["Close"].rolling(long_window).mean()

    df["signal"] = 0
    df.loc[df["ma_short"] > df["ma_long"], "signal"] = 1
    df.loc[df["ma_short"] < df["ma_long"], "signal"] = -1

    return df
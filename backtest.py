def backtest(df):
    df = df.copy()

    df["position"] = (
        df["signal"] * df["position_size"]
    ).shift(1)

    df["strategy_returns"] = df["position"] * df["returns"]
    df["cum_strategy"] = (1 + df["strategy_returns"]).cumprod()
    df["cum_market"] = (1 + df["returns"]).cumprod()

    return df
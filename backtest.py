def backtest(df, cost_per_trade=0.0005):
    df = df.copy()

    df["position"] = (
        df["signal"] * df["position_size"]
    ).shift(1)

    df["position_change"] = df["position"].diff().abs()

    df["gross_returns"] = df["position"] * df["returns"]
    df["transaction_costs"] = cost_per_trade * df["position_change"]

    df["strategy_returns"] = (
        df["gross_returns"] - df["transaction_costs"]
    )

    df["cum_strategy"] = (1 + df["strategy_returns"]).cumprod()
    df["cum_market"] = (1 + df["returns"]).cumprod()

    return df

import numpy as np

def volatility_targeting(
    df,
    vol_window=20,
    target_vol=0.10,
    max_leverage=3
):
    df = df.copy()

    df["vol"] = df["returns"].rolling(vol_window).std()
    daily_target_vol = target_vol / np.sqrt(252)

    df["position_size"] = daily_target_vol / df["vol"]
    df["position_size"] = df["position_size"].clip(0, max_leverage)

    return df
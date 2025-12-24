from data import load_data
from signals import trend_signal
from risk import volatility_targeting
from backtest import backtest
from metrics import sharpe_ratio, max_drawdown

import matplotlib.pyplot as plt

def main():
    df = load_data("SPY", start="2015-01-01")
    df = trend_signal(df)
    df = volatility_targeting(df)
    df = backtest(df)

    strat_sharpe = sharpe_ratio(df["strategy_returns"].dropna())
    strat_dd = max_drawdown(df["cum_strategy"])

    print(f"Sharpe Ratio: {strat_sharpe:.2f}")
    print(f"Max Drawdown: {strat_dd:.2%}")

    plt.figure(figsize=(12, 6))
    plt.plot(df["cum_strategy"], label="Strategy")
    plt.plot(df["cum_market"], label="Market")
    plt.legend()
    plt.title("Volatility-Targeted Trend Strategy")
    plt.show()

if __name__ == "__main__":
    main()
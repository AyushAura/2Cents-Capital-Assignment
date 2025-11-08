class Alpha4MultiAsset:
    """
    Alpha 4: Multi-Asset Regime Switching (Risk-On / Risk-Off).
    Uses a benchmark index (e.g., Nifty 50) to determine market regime
    and rotate between high-beta and defensive asset baskets.
    """
    def __init__(self, benchmark_id: str):
        self.benchmark_id = benchmark_id
        self.ma_period = 50
        self.benchmark_prices = []

    def on_daily_bar(self, bar):
        if bar.instrument_id == self.benchmark_id:
             self.benchmark_prices.append(float(bar.close))
             
        if len(self.benchmark_prices) > self.ma_period:
            ma = sum(self.benchmark_prices[-self.ma_period:]) / self.ma_period
            current_price = self.benchmark_prices[-1]
            
            if current_price > ma:
                return "RISK_ON"
            else:
                return "RISK_OFF"
        return "NEUTRAL"
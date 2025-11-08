class Alpha2Breakout:
    """
    Alpha 2: Volatility Breakout (Momentum).
    Uses Donchian Channels to identify price breakouts from a defined range.
    """
    def __init__(self, instrument_id: str, lookback: int = 20):
        self.instrument_id = instrument_id
        self.lookback = lookback
        self.highs = []
        self.lows = []

    def on_bar(self, bar):
        if bar.instrument_id != self.instrument_id:
            return 0
            
        self.highs.append(float(bar.high))
        self.lows.append(float(bar.low))
        
        if len(self.highs) <= self.lookback:
            return 0

        # Calculate previous bar's channel
        upper_channel = max(self.highs[-self.lookback-1:-1])
        lower_channel = min(self.lows[-self.lookback-1:-1])
        current_price = float(bar.close)

        if current_price > upper_channel:
            return 1  # Long Breakout
        elif current_price < lower_channel:
            return -1 # Short Breakout
        return 0
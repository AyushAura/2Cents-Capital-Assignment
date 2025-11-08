class Alpha3MTF:
    """
    Alpha 3: Multi-Timeframe Trend Following.
    Uses a 1-hour EMA as a trend filter and 1-minute EMAs for entry signals.
    """
    def __init__(self, instrument_id: str):
        self.instrument_id = instrument_id
        self.lt_ema_period = 100 # 1-hour
        self.st_fast_period = 9  # 1-minute
        self.st_slow_period = 21 # 1-minute
        
        # Mock state for EMAs
        self.lt_trend = 0 # 1 for Bull, -1 for Bear
        self.st_fast_ema = 0.0
        self.st_slow_ema = 0.0

    def on_1h_bar(self, bar):
        """Called when a 1-hour bar is closed"""
        # Update LT trend filter logic here
        pass

    def on_1m_bar(self, bar):
        """Called on every 1-minute bar for entry signals"""
        # 1. Check LT trend filter
        if self.lt_trend == 0: return 0
        
        # 2. Update ST EMAs
        # ...
        
        # 3. Check for crossover aligned with LT trend
        # if self.lt_trend == 1 and crossover(fast, slow): return 1
        return 0
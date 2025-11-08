class Alpha5OrderBook:
    """
    Alpha 5: High-Frequency Order Book Imbalance (Microstructure).
    Generates signals based on the Order Book Imbalance (OBI) metric.
    *** FAILED REPLICATION in Phase IV due to latency ***
    """
    def __init__(self, instrument_id: str, threshold: float = 0.7):
        self.instrument_id = instrument_id
        self.threshold = threshold

    def on_l2_update(self, book_snapshot):
        """
        Called on every L2 order book update.
        """
        bid_vol = sum([level.quantity for level in book_snapshot.bids[:5]])
        ask_vol = sum([level.quantity for level in book_snapshot.asks[:5]])
        
        total_vol = bid_vol + ask_vol
        if total_vol == 0: return 0
        
        obi = bid_vol / total_vol
        
        if obi > self.threshold:
            return 1 # Strong buying pressure
        elif obi < (1.0 - self.threshold):
            return -1 # Strong selling pressure
            
        return 0
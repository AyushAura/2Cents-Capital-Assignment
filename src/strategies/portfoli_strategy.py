from nautilus_trader.core.actor import Actor
from nautilus_trader.core.message import Event
from nautilus_trader.model.data import Bar, QuoteTick, OrderBook
from nautilus_trader.model.events import OrderFilled
from nautilus_trader.strategy import Strategy

# Import our alpha models
from src.alphas.alpha_1_pairs import Alpha1Pairs
from src.alphas.alpha_2_breakout import Alpha2Breakout
from src.alphas.alpha_3_mtf import Alpha3MTF
from src.alphas.alpha_4_multi_asset import Alpha4MultiAsset
from src.alphas.alpha_5_orderbook import Alpha5OrderBook

class PortfolioStrategy(Strategy):
    """
    The central strategy actor that manages all 5 alphas, aggregates their
    signals, and manages portfolio-level risk and execution.
    """
    def __init__(self, config):
        super().__init__(config)
        
        # Initialize all 5 alphas with their specific parameters
        self.alpha_1 = Alpha1Pairs(asset_a="BTCUSDT.BINANCE", asset_b="ETHUSDT.BINANCE")
        self.alpha_2 = Alpha2Breakout(instrument_id="EURUSD.IBKR", lookback=20)
        self.alpha_3 = Alpha3MTF(instrument_id="GC.IBKR") # Gold Futures
        self.alpha_4 = Alpha4MultiAsset(benchmark_id="NIFTY50.ZERODHA")
        self.alpha_5 = Alpha5OrderBook(instrument_id="AAPL.IBKR")
        
        self.log.info("PortfolioStrategy initialized with 5 alphas.")

    async def on_bar(self, bar: Bar):
        """
        Event handler for Bar data (1-minute, 1-hour, daily).
        Dispatches data to the relevant bar-based alphas (1-4).
        """
        # 1. Update Alphas
        sig1 = self.alpha_1.on_bar(bar)
        sig2 = self.alpha_2.on_bar(bar)
        # ... dispatch to others based on instrument_id ...
        
        # 2. Aggregate & Execute
        # self.execute_portfolio_rebalance()
        pass

    async def on_order_book(self, book: OrderBook):
        """
        Event handler for L2 Order Book data.
        Dispatches data specifically to Alpha 5 (HFT).
        """
        sig5 = self.alpha_5.on_l2_update(book)
        if sig5 != 0:
            self.log.info(f"Alpha 5 HFT Signal: {sig5}")
            # self.execute_hft_order(sig5)
        pass
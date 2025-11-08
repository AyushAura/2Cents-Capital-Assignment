from nautilus_trader.adapters.binance.clients import BinanceDataClient, BinanceExecutionClient

# Nautilus has built-in Binance clients, so we often just configure them.
# This file serves as a placeholder to show where custom logic would go
# if we needed to override the default behavior.

class CustomBinanceDataClient(BinanceDataClient):
    """
    Extended Binance client to handle custom data streams if necessary.
    """
    pass
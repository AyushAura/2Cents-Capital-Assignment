import asyncio
import configparser
from nautilus_trader.config import TradingNodeConfig
from nautilus_trader.core.message import Event  # Correct v1.x import
from nautilus_trader.core.actor import Actor      # Correct v1.x import
from nautilus_trader.core.node import TradingNode
from nautilus_trader.adapters.ib.clients import IBKRDataClient
from nautilus_trader.adapters.ib.clients import IBKRExecutionClient
from nautilus_trader.model.enums import LogLevel

# This is a simple "Actor" that will just listen for events
# and print them. This helps us see if we are connected.
class EventPrinter(Actor):
    def __init__(self):
        # We pass self.id as the actor_id to the base constructor
        super().__init__(id=self.id, loop=None)
        self.log = self.init_logging(self.id, LogLevel.INFO)

    async def on_event(self, event: Event):
        # We are looking for an AccountState message, which proves
        # we are connected and receiving data from the broker.
        self.log.info(f"Received event: {event.__class__.__name__}")
        if event.__class__.__name__ == "AccountState":
            self.log.info(f"Successfully received account data: {event}")

    # on_message is part of the base Actor, we just don't use it here.
    async def on_message(self, message):
        pass # Not used in this test

async def main():
    """
    Main function to configure and run the connection test.
    """
    print("--- Starting IBKR Connection Test ---")

    # 1. Load API keys from our config file
    config = configparser.ConfigParser()
    config.read('config/api_keys.ini')

    ibkr_config = config['ibkr_paper']
    host = ibkr_config['host']
    port = ibkr_config['port']
    client_id = ibkr_config['client_id']

    print(f"Attempting to connect to IBKR TWS at {host}:{port} with ClientID {client_id}...")
    print("Ensure TWS is running and 'Enable ActiveX' is checked.")

    # 2. Configure the main TradingNode
    node_config = TradingNodeConfig(
        actor_id="IBKR.Connection.Test",
        log_level=LogLevel.INFO,
    )
    node = TradingNode(config=node_config)

    # 3. Configure the IBKR Data Client
    # Use a different client_id for data
    data_client = IBKRDataClient(
        client_id=int(client_id) + 1,
        host=host,
        port=int(port),
    )

    # 4. Configure the IBKR Execution Client
    exec_client = IBKRExecutionClient(
        client_id=int(client_id),
        host=host,
        port=int(port),
    )

    # 5. Add the clients to the node
    node.add_client(data_client)
    node.add_client(exec_client)

    # 6. Add our simple event printer to see what's happening
    printer = EventPrinter()
    node.add_actor(printer)

    try:
        # 7. Start the node
        await node.start()
        print("Node started successfully. Listening for events...")
        print("Check TWS, you should see the ClientID connection.")
        print("Waiting for 15 seconds to receive account data...")

        # We'll run for 15 seconds to see if we get account updates.
        # If you see "Received event: AccountState", it's a 100% success!
        await asyncio.sleep(15)

        print("--- Test Complete ---")

    except Exception as e:
        print(f"Error encountered: {e}")
    finally:
        # 8. Cleanly stop the node
        await node.stop()
        print("Node stopped.")

if __name__ == "__main__":
    asyncio.run(main())



import MetaTrader5EasyT as easyt
import time

# Connect to MT5 platform
easyt.connect()

# Login to your account
account =101577647  # replace with your account number
password = '1234$Victoria' # replace with your account password
server = 'Exness-MT5Trial9'  # replace with your broker's server name

authorized = easyt.login(account, password, server)
if authorized:
    print("Connected to account:", account)
else:
    print("Failed to connect:", easyt.last_error())
    easyt.disconnect()
    exit()

# Define the symbol and timeframe
symbol = 'EURUSD'
timeframe = easyt.TIMEFRAME_M1

while True:
    # Check for existing sell orders
    orders = easyt.orders_get(symbol=symbol)
    sell_orders = [order for order in orders if order.type == easyt.ORDER_TYPE_SELL]

    if not sell_orders:
        # Request the last 100 candlesticks
        candles = easyt.copy_rates_from_pos(symbol, timeframe, 0, 100)

        # Place a buy order
        lot_size = 0.01
        price = easyt.symbol_info_tick(symbol).ask
        slippage = 3
        stop_loss = price - 0.005
        take_profit = price + 0.01

        request = {
            'action': easyt.TRADE_ACTION_DEAL,
            'symbol': symbol,
            'volume': lot_size,
            'type': easyt.ORDER_TYPE_BUY,
            'price': price,
            'sl': stop_loss,
            'tp': take_profit,
            'deviation': slippage
        }
        result = easyt.order_send(request)

        if result.retcode != easyt.TRADE_RETCODE_DONE:
            print(f"Order failed: {result.comment}")
        else:
            print("Buy order placed successfully")

    # Sleep for 3 minutes
    time.sleep(180)

# Disconnect from the MT5 platform
easyt.disconnect()

 



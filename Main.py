from metaapi_cloud_sdk import MetaApi
import talib
import numpy as np

# Initialize MetaApi client

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YjI0NTQ0ZWYzMWI0NzQ4NWMxNzQ1NmUzNzdmYTlhZiIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7Im1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7Im1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsibWV0aG9kcyI6WyJyaXNrLW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsibWV0aG9kcyI6WyJtdC1tYW5hZ2VyLWFwaTpyZXN0OmRlYWxpbmc6KjoqIiwibXQtbWFuYWdlci1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfV0sInRva2VuSWQiOiIyMDIxMDIxMyIsImltcGVyc29uYXRlZCI6ZmFsc2UsInJlYWxVc2VySWQiOiI2YjI0NTQ0ZWYzMWI0NzQ4NWMxNzQ1NmUzNzdmYTlhZiIsImlhdCI6MTY4MzU1NTQzOX0.TyozxNppuzbijkcibZg1mw-fGdxfdVV_7oUO8F01iC-SVd9ueUqvYKJ4dyM2pJVn4jT0slQc-KR0Y2yvKVfG4BDPFCiZ0q3kPrU-JccZn9Ej4ZuD7nyS-iBXOcOX8UTDTC61WXvx0F2dJ4D2hW7-tFOalKJNkImdO2CI9fJboPS3bqchigNStji9d5F2QHx_gnrUEPi2GNpXwbuQ06haJtbxR9wjB_BJ4k-UxxWQyDE1ljlf27T_bbCdhTAo5YZyE36hfgf9GF6ak4WniSnQVpnv98WwE7a8zmpJW0WMa6fWTTQ_msdKCz0xIoT6-CC74LlpAQrVjOUMmsOYW-0dGJV5I8IQbaiDJLqZbEFbllfS8uBzYGXKqfTgu-bc8Z7BAmcT6-Hyd9biLI_uI43poE3fh-9UqpZ7_keAnk-xdORwuFLped0WbSDQdQCkTOQ9ToSpFDq47j2MF_ieDuNw0MOW9nDnm-z-BdUA8ONpb10gl9mnr6kuLEEQsdD8eqOVVtk0Vp4vEVfvje-czro_mBEjdjPUsTAHBBqPwX6EJ6ZyUuJd5jc4WpiumHXWwTpb9bsxLD1kgD2Kj3XuXd-ncWDnl25nR_gdbkr8MQ_8ot3LZqNWB2hTggXW2O1Usp1dKo-H0prhp3EPWLbn9go2NAkNWPRQIlAJ0JKxVtbHNzA'
#account_id = '7d8ab04c-bc18-4535-bbc4-660c30e4d4ab'
account_id='c11f5cfa-ff5c-40b7-9028-a87616f3a767'

api = MetaApi(token)

# Define trading parameters
symbol = 'XAUUSD'
volume = 0.01
risk_percentage = 4
atr_periods = 14
atr_multiplier = 2
trailing_stop_distance = 50

# Define indicator parameters
rsi_periods = 14
macd_periods = (12, 26, 9)
bbands_periods = 20
bbands_deviation = 2
ema_periods = (50, 200)

# Define trade variables
trade_type = None
trailing_stop = None
position_opened = False

async def main():
    # Connect to the MetaTrader account
    try:
        await api.connect()
        account = await api.metatrader_account_api.get_account(account_id)
    except Exception as e:
        print(f"Error connecting to MetaTrader account: {e}")
        return
    
    while True:
        # Get the latest candle data
        try:
            candles = await api.metatrader_candles_api.get_candles(account_id, symbol, '30s', 1000)
        except Exception as e:
            print(f"Error retrieving candle data: {e}")
            continue
        
        # Extract the close prices from the candle data
        close = np.array([candle.close for candle in candles])
        
        # Calculate the indicators
        rsi = talib.RSI(close, rsi_periods)
        macd, macdsignal, macdhist = talib.MACD(close, macd_periods[0], macd_periods[1], macd_periods[2])
        upperband, middleband, lowerband = talib.BBANDS(close, bbands_periods, bbands_deviation, bbands_deviation, 0)
        ema_short = talib.EMA(close, ema_periods[0])
        ema_long = talib.EMA(close, ema_periods[1])
        atr = talib.ATR(candles.high, candles.low, candles.close, atr_periods)
        
        # Determine the position of each indicator
        rsi_position = 'overbought' if rsi[-1] > 70 else 'oversold' if rsi[-1] < 30 else 'neutral'
        macd_position = 'above' if macd[-1] > macdsignal[-1] else 'below'
        bbands_position = 'above' if close[-1] > upperband[-1] else 'below' if close[-1] < lowerband[-1] else 'inside'
        ema_position = 'bullish' if ema_short[-1] > ema_long[-1] else 'bearish'
        
        # Determine if the market is trending or ranging
        is_trending = ema_position == 'bullish' and macd_position == 'above' and bbands_position == 'above'
        is_ranging = ema_position == 'bearish' and macd_position == 'below' and bbands_position == 'below'
        
        # Check if all indicators are showing the same position and place a trade if they are
        if (rsi_position == macd_position == bbands_position == ema_position) and (is_trending or is_ranging):
            if (rsi_position == 'overbought' and ema_position == 'bearish') or (rsi_position == 'oversold' and ema_position == 'bullish'):
                trade_type = 'sell'
            elif (rsi_position == 'oversold' and ema_position == 'bearish') or (rsi_position == 'overbought' and ema_position == 'bullish'):
                trade_type = 'buy'
            
            # Check if more than 9 out of 12 indicators are in agreement
            indicators = [rsi_position, macd_position, bbands_position, ema_position]
            if indicators.count(trade_type) >= 9:
                # Calculate the trade size based on the current balance and risk percentage
                try:
                    balance = await api.metatrader_account_api.get_balance(account_id)
                    trade_size = (balance * risk_percentage) / 100
                    trade_size = round(trade_size / float(account.symbol_info[symbol].lotSize), 2) * float(account.symbol_info[symbol].lotSize)
                except Exception as e:
                    print(f"Error retrieving account balance: {e}")
                    continue
                
                # Calculate the current trailing stop distance
                if trade_type == 'buy':
                    trailing_stop = close[-1] - (atr[-1] * atr_multiplier)
                elif trade_type == 'sell':
                    trailing_stop = close[-1] + (atr[-1] * atr_multiplier)
                
                # Place the trade
                try:
                    position = await api.metatrader_trades_api.create_market_order(account_id, {
                        'symbol': symbol,
                        'type': trade_type,
                        'volume': volume,
                        'trailingStop': trailing_stop,
                        'comment': 'Trading bot'
                    })
                    print(f"Placed {trade_type} trade for {symbol} at {close[-1]}. Trade size: {trade_size}.")
                    position_opened = True
                except Exception as e:
                    print(f"Error placing {trade_type} trade for {symbol}: {e}")
        else:
            if position_opened:
                # Close the position if the market condition changes
                try:
                    await api.metatrader_trades_api.close_position(account_id, position.id)
                    print(f"Closed {trade_type} position for {symbol} at {close[-1]}.")
                    position_opened = False
                except Exception as e:
                    print(f"Error closing {trade_type} position for {symbol}: {e}")

# Run the main program
asyncio.run(main())

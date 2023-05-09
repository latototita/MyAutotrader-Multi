


toke = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YjI0NTQ0ZWYzMWI0NzQ4NWMxNzQ1NmUzNzdmYTlhZiIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7Im1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7Im1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsibWV0aG9kcyI6WyJyaXNrLW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsibWV0aG9kcyI6WyJtdC1tYW5hZ2VyLWFwaTpyZXN0OmRlYWxpbmc6KjoqIiwibXQtbWFuYWdlci1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfV0sInRva2VuSWQiOiIyMDIxMDIxMyIsImltcGVyc29uYXRlZCI6ZmFsc2UsInJlYWxVc2VySWQiOiI2YjI0NTQ0ZWYzMWI0NzQ4NWMxNzQ1NmUzNzdmYTlhZiIsImlhdCI6MTY4MzU1NTQzOX0.TyozxNppuzbijkcibZg1mw-fGdxfdVV_7oUO8F01iC-SVd9ueUqvYKJ4dyM2pJVn4jT0slQc-KR0Y2yvKVfG4BDPFCiZ0q3kPrU-JccZn9Ej4ZuD7nyS-iBXOcOX8UTDTC61WXvx0F2dJ4D2hW7-tFOalKJNkImdO2CI9fJboPS3bqchigNStji9d5F2QHx_gnrUEPi2GNpXwbuQ06haJtbxR9wjB_BJ4k-UxxWQyDE1ljlf27T_bbCdhTAo5YZyE36hfgf9GF6ak4WniSnQVpnv98WwE7a8zmpJW0WMa6fWTTQ_msdKCz0xIoT6-CC74LlpAQrVjOUMmsOYW-0dGJV5I8IQbaiDJLqZbEFbllfS8uBzYGXKqfTgu-bc8Z7BAmcT6-Hyd9biLI_uI43poE3fh-9UqpZ7_keAnk-xdORwuFLped0WbSDQdQCkTOQ9ToSpFDq47j2MF_ieDuNw0MOW9nDnm-z-BdUA8ONpb10gl9mnr6kuLEEQsdD8eqOVVtk0Vp4vEVfvje-czro_mBEjdjPUsTAHBBqPwX6EJ6ZyUuJd5jc4WpiumHXWwTpb9bsxLD1kgD2Kj3XuXd-ncWDnl25nR_gdbkr8MQ_8ot3LZqNWB2hTggXW2O1Usp1dKo-H0prhp3EPWLbn9go2NAkNWPRQIlAJ0JKxVtbHNzA'
#account_id = '7d8ab04c-bc18-4535-bbc4-660c30e4d4ab'
account_id='c11f5cfa-ff5c-40b7-9028-a87616f3a767'

import backtrader as bt
import numpy as np
import time
from metaapi_cloud_sdk import MetaApi

class MyStrategy(bt.Strategy):
    params = (
        ('atr_periods', 14),
        ('atr_multiplier', 2),
        ('trailing_stop_distance', 50),
        ('rsi_periods', 14),
        ('macd_periods', (12, 26, 9)),
        ('bbands_periods', 20),
        ('bbands_deviation', 2),
        ('ema_periods', (50, 200)),
        ('risk_percentage', 4),
        ('volume', 0.01),
        ('symbol', 'XAUUSD'),
        ('account_id', 'c11f5cfa-ff5c-40b7-9028-a87616f3a767')
    )

    def __init__(self):
        self.trailing_stop = None
        self.position_opened = False
        self.trade_type = None

        # Initialize MetaApi client
        self.api = MetaApi(token)

        # Connect to the MetaTrader account
        self.api.connect()
        self.account = self.api.metatrader_account_api.get_account(self.params.account_id)

    def next(self):
        # Get the latest candle data
        try:
            candles = self.api.metatrader_candles_api.get_candles(self.params.account_id, self.params.symbol, '1M', 1000)
        except Exception as e:
            print(f"Error retrieving candle data: {e}")
            return

        # Extract the close prices from the candle data
        close = np.array([candle.close for candle in candles])

        # Calculate the indicators
        rsi = bt.talib.RSI(close, timeperiod=self.params.rsi_periods)
        macd, macdsignal, macdhist = bt.talib.MACD(close, *self.params.macd_periods)
        upperband, middleband, lowerband = bt.talib.BBANDS(close, timeperiod=self.params.bbands_periods,
                                                           nbdevup=self.params.bbands_deviation,
                                                           nbdevdn=self.params.bbands_deviation, matype=0)
        ema_short = bt.talib.EMA(close, timeperiod=self.params.ema_periods[0])
        ema_long = bt.talib.EMA(close, timeperiod=self.params.ema_periods[1])
        atr = bt.talib.ATR(candles.high, candles.low, candles.close, timeperiod=self.params.atr_periods)

        # Determine the position of each indicator
        rsi_position = 'overbought' if rsi[-1] > 70 else 'oversold' if rsi[-1] < 30 else 'neutral'
        macd_position = 'above' if macd[-1] > macdsignal[-1] else 'below'
        bbands_position = 'above' if close[-1] > upperband[-1] else 'below' if close[-1] < lowerband[-1] else 'inside'
        ema_position = 'bullish' if ema_short[-1] > ema_long[-1] else 'bearish'

        # Determine if the market is trending or ranging
        is_trending = ema_position == 'bullish' and macd_position == 'above' and bbands_position == 'above'
        is_ranging = ema_position == 'bearish' and macd_position == 'below' and bbands_position == 'below'

        # Check if all indicators are showing
        # Check if all indicators are showing the same position and place a trade if they are
        if is_trending and not self.position_opened:
            # Open a long position
            self.position_opened = True
            self.trade_type = 'long'

            # Calculate the stop loss and take profit levels
            stop_loss = close[-1] - self.params.trailing_stop_distance * atr[-1]
            take_profit = close[-1] + self.params.trailing_stop_distance * atr[-1]

            # Place a market order with MetaApi
            try:
                order_id = self.api.metatrader_trades_api.create_market_buy_order(self.params.account_id,
                                                                                  self.params.symbol,
                                                                                  self.params.volume)
                print("Success - Trending")
            except Exception as e:
                print(f"Error placing market buy order: {e}")
                return

            # Update the stop loss and take profit levels for the opened position
            try:
                self.api.metatrader_trades_api.update_trade(self.params.account_id, order_id,
                                                            stop_loss=stop_loss, take_profit=take_profit)
                print("Success - Update Trending")
            except Exception as e:
                print(f"Error updating trade: {e}")
                return

        elif is_ranging and not self.position_opened:
            # Open a short position
            self.position_opened = True
            self.trade_type = 'short'

            # Calculate the stop loss and take profit levels
            stop_loss = close[-1] + self.params.trailing_stop_distance * atr[-1]
            take_profit = close[-1] - self.params.trailing_stop_distance * atr[-1]

            # Place a market order with MetaApi
            try:
                order_id = self.api.metatrader_trades_api.create_market_sell_order(self.params.account_id, self.params.symbol, self.params.volume)
                print("Success - Ranging")
            except Exception as e:
                print(f"Error placing market sell order: {e}")
                return

            # Update the stop loss and take profit levels for the opened position
            try:
                self.api.metatrader_trades_api.update_trade(self.params.account_id, order_id,
                                                            stop_loss=stop_loss, take_profit=take_profit)
                print("Success - Update Ranging")
            except Exception as e:
                print(f"Error updating trade: {e}")
                return

        print("No suitable market conditions")

        # Check if the trailing stop should be updated
        if self.position_opened and self.trade_type == 'long':
            # Calculate the updated stop loss level
            stop_loss = close[-1] - self.params.trailing_stop_distance * atr[-1]

            # Update the stop loss level for the opened position
            try:
                self.api.metatrader_trades_api.update_trade(self.params.account_id, order_id,
                                                            stop_loss=stop_loss)
                print("Success - Update Trailing Stop")
            except Exception as e:
                print(f"Error updating trade: {e}")
                return

        elif self.position_opened and self.trade_type == 'short':
            # Calculate the updated stop loss level
            stop_loss = close[-1] + self.params.trailing_stop_distance * atr[-1]

            # Update the stop loss level for the opened position
            try:
                self.api.metatrader_trades_api.update_trade(self.params.account_id, order_id,
                                                            stop_loss=stop_loss)
                print("Success - Update Trailing Stop")
            except Exception as e:
                print(f"Error updating trade: {e}")
                return

import time
from datetime import datetime, timedelta
import backtrader as bt
import numpy as np
from metaapi_cloud_sdk import MetaApi


if __name__ == '__main__':
    # Create an instance of the strategy
    strategy = MyStrategy()

    # Create a cerebro instance
    cerebro = bt.Cerebro()

    # Add the strategy to cerebro
    cerebro.addstrategy(strategy)

    # Set the data parameters (you may need to adjust these according to your data)
    data_params = {
        'name': 'mydata',
        'timeframe': bt.TimeFrame.Minutes,
        'compression': 1,
    }

    # Create a data feed
    data = bt.feeds.YourDataFeed(**data_params)  # Replace YourDataFeed with your actual data feed class

    # Add the data feed to cerebro
    cerebro.adddata(data)

    # Run the strategy every 3 minutes
    cerebro.run(**{
        'runonce': False,
        'exactbars': 1,
        'fromdate': datetime.now() - timedelta(minutes=3),
        'todate': datetime.now(),
        'live': False
    })

    while True:
        cerebro.run(**{
            'runonce': False,
            'exactbars': 1,
            'fromdate': datetime.now() - timedelta(minutes=3),
            'todate': datetime.now(),
            'live': False
        })
        time.sleep(180)  # Wait for 3 minutes before running again

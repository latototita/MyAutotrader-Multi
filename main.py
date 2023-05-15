import asyncio
import numpy as np
import os
import pandas as pd
import pandas_ta as ta
from metaapi_cloud_sdk import MetaApi
from metaapi_cloud_sdk.clients.metaApi.tradeException import TradeException
from datetime import datetime, timedelta

# Initialize MetaApi client

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YjI0NTQ0ZWYzMWI0NzQ4NWMxNzQ1NmUzNzdmYTlhZiIsInBlcm1pc3Npb25zIjpbXSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjZiMjQ1NDRlZjMxYjQ3NDg1YzE3NDU2ZTM3N2ZhOWFmIiwiaWF0IjoxNjgzOTcwNDk4fQ.XzOt-R6egTLGb0fpmbxzDrLHqqlSbqdskeX3OSbx585bi_jG9BhSp-PtEyZ4kqJBafXcGmGRa8IMYQ6BMtDRmoiUd6InEjioBhPlKa6wrylTruPK6_YYq3LsZGd-GctHqW5-_pv3UtKyYriHO-P61dE-zpH6AAAO-NeAru-GKvOQeNwhwSVW_Q8Ov6Q6dljt0q9psxZYOU2jZiR1N3d0d_pQpvKLCgXFk71TL93GyEj-7csQ5Z0py0ChVioeWY7Cf-MlzEJdnSFgcHeFaKfny680C-5srBJwCO4EBVSEEqJao71fhnnK7UsW_QVMUoamVEBvbxD2Wr0F2pHcdIkVUoMrJeNiWdCTvdEONsg9xMFREqGdvlx66khNhvOpVvK_obsSEwMUS7Qvk3-3yh5F7PaT0qsQW4WdZVRaTLbayA7ChbYqCGvp4EAA4mxYTSxWjihDFCWHy6QWmHVzDw5JzhUxus-bWtOTiVVGUjg5e5uPNSHYUzN2D0Pl4p6QxnGISQCmRTuNtbEEm_9yLF_5xuRAdQez1VS0rYP0x3YauLmLIdhpmNKjNNfi13uAiwJVmjIj__9VDALqiGje25WFWr9BLQCUZdemGHe4q9bc2IcAjSZIo6auI6aVqkGwm7UpkHat_FMTxynZnhDNkrGebjgvuW4_1nbmWVUGZ4y2mTc'
accountId = os.getenv('ACCOUNT_ID') or '7d8ab04c-bc18-4535-bbc4-660c30e4d4ab'


# Define trading parameters
symbol = 'XAUUSDm'
volume = 0.01
risk_percentage = 4
atr_periods = 14
atr_multiplier = 2

# Define indicator parameters
rsi_periods = 14
sma_periods = 50
ema_periods = 200
macd_periods = (12, 26, 9)
bbands_periods = 20
bbands_deviation = 2



async def main():
    # Connect to the MetaTrader account
    api = MetaApi(token)
    try:
        account = await api.metatrader_account_api.get_account(accountId)
        account_balance = account['balance']
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
            print('Deploying account')
            await account.deploy()

        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_rpc_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        while True:
            open_trades=await connection.get_orders()
            if open_trades:
                pass
            else:
                # Get the latest candle data
                print('api synchronized successfully')
                try:
                    candles = await account.get_historical_candles(symbol=symbol,timeframe='30s',start_time=None,limit=1000)
                    print('Gotten the latest candle data Successfully')
                except Exception as e:
                    print(f"Error retrieving candle data: {e}")
                    continue
                data = pd.DataFrame(candles)
                data['time'] = pd.to_datetime(data['time'], unit='ms')
                data.set_index('time', inplace=True)

                atr_period = 14  # Replace with your desired ATR period
                data['atr'] = ta.atr(data['high'], data['low'], data['close'], length=atr_period)

                # Determine the current ATR value
                current_atr = data['atr'].iloc[-1]

                # Calculate the ATR-based threshold for buy and sell signals
                threshold = current_atr * 0.5

                # Determine if a buy or sell order should be placed
                if data['close'].iloc[-1] > data['open'].iloc[-1] + threshold:
                    ATR = 'Buy'
                elif data['close'].iloc[-1] < data['open'].iloc[-1] - threshold:
                    ATR = 'Sell'
                else:
                    ATR = 'None'
                data = pd.DataFrame(candles)
                data['time'] = pd.to_datetime(data['time'], unit='ms')
                data.set_index('time', inplace=True)

                # Calculate Volume indicators
                data['obv'] = ta.obv(data['close'], data['volume'])
                data['vwap'] = ta.vwap(data['high'], data['low'], data['close'], data['volume'])
                data['adl'] = ta.adl(data['high'], data['low'], data['close'], data['volume'])
                data['cmf'] = ta.cmf(data['high'], data['low'], data['close'], data['volume'])

                # Determine if a buy or sell order should be placed
                if data['obv'].iloc[-1] > data['obv'].shift(1).iloc[-1] and data['vwap'].iloc[-1] > data['vwap'].shift(1).iloc[-1] and data['adl'].iloc[-1] > data['adl'].shift(1).iloc[-1] and data['cmf'].iloc[-1] > data['cmf'].shift(1).iloc[-1]:
                    set_1 = 'Buy'
                elif data['obv'].iloc[-1] < data['obv'].shift(1).iloc[-1] and data['vwap'].iloc[-1] < data['vwap'].shift(1).iloc[-1] and data['adl'].iloc[-1] < data['adl'].shift(1).iloc[-1] and data['cmf'].iloc[-1] < data['cmf'].shift(1).iloc[-1]:
                    set_1 = 'Sell'
                else:
                    set_1 = 'No Order'
                data = pd.DataFrame(candles)
                data['time'] = pd.to_datetime(data['time'], unit='ms')
                data.set_index('time', inplace=True)

                # Apply the Oscillator indicators
                data['willr'] = ta.willr(data['high'], data['low'], data['close'])
                data['adx'] = ta.adx(data['high'], data['low'], data['close'], length=14)
                data['cci'] = ta.cci(data['high'], data['low'], data['close'], length=20)

                # Set buy and sell conditions based on the indicators
                data['buy_signal'] = (
                    (data['willr'] < -80) &  # Example condition for Williams %R (oversold)
                    (data['adx'] > 25) &  # Example condition for ADX (trend strength)
                    (data['cci'] < -100)  # Example condition for CCI (oversold)
                )

                data['sell_signal'] = (
                    (data['willr'] > -20) &  # Example condition for Williams %R (overbought)
                    (data['adx'] > 25) &  # Example condition for ADX (trend strength)
                    (data['cci'] > 100)  # Example condition for CCI (overbought)
                )

                # Assess whether to place a buy or sell order
                if data['buy_signal'].any():
                    order_type_2 = 'Buy'
                elif data['sell_signal'].any():
                    order_type_2 = 'Sell'
                else:
                    order_type_2 = 'No Order'


                # Calculate Volatility Indicators
                data['atr'] = ta.atr(data['high'], data['low'], data['close'], length=14)
                data['bb_upper'], data['bb_middle'], data['bb_lower'] = ta.bbands(data['close'], length=20)
                data['dc_upper'], data['dc_lower'] = ta.donchian(data['close'], upper_length=20, lower_length=20)
                data['kc_upper'], data['kc_middle'], data['kc_lower'] = ta.kc(data['high'], data['low'], data['close'], length=20)
                data['vix'] = ta.vortex_indicator(data['high'], data['low'], data['close'], length=14)

                # Determine Buy and Sell Signals
                data['buy_signalz'] = (data['close'] > data['bb_upper']) & (data['close'].shift(1) <= data['bb_upper'].shift(1)) \
                                    & (data['vix'] > 1)
                data['sell_signalz'] = (data['close'] < data['bb_lower']) & (data['close'].shift(1) >= data['bb_lower'].shift(1)) \
                                    & (data['vix'] > 1)

                # Initialize variables for buy and sell orders
                buy_order = False
                sell_order = False

                # Loop through the data to determine buy and sell orders
                for i in range(1, len(data)):
                    if data['buy_signalz'][i-1] and data['buy_signalz'][i] and data['buy_signalz'][i+1]:
                        buy_orderzz = True
                        # Place your buy order logic here

                    if data['sell_signalz'][i-1] and data['sell_signalz'][i] and data['sell_signalz'][i+1]:
                        sell_orderzz = True
                        # Place your sell order logic here

                # Extract the close prices from the candle data
                close = np.array([candle.close for candle in candles])
                
                # Create pandas DataFrame with close prices
                df = pd.DataFrame(close, columns=['close'])
                
                # Calculate the indicators using pandas_ta
                df['rsi'] = ta.rsi(df['close'], rsi_periods)
                df['sma'] = ta.sma(df['close'], sma_periods)
                df['ema'] = ta.ema(df['close'], ema_periods)
                macd_data = ta.macd(df['close'], *macd_periods)
                df['macd'] = macd_data['MACD']
                df['macdsignal'] = macd_data['MACDh']
                df['macdhist'] = macd_data['MACDs']
                df['upperband'], df['middleband'], df['lowerband'] = ta.bbands(df['close'], bbands_periods, bbands_deviation)
                ichimoku_data = ta.ichimoku(df['close'])
                df['tenkan_sen'] = ichimoku_data['tenkan_sen']
                df['kijun_sen'] = ichimoku_data['kijun_sen']
                df['senkou_span_a'] = ichimoku_data['senkou_span_a']
                df['senkou_span_b'] = ichimoku_data['senkou_span_b']
                df['chikou_span'] = ichimoku_data['chikou_span']
                df['atr'] = ta.atr(candles.high, candles.low, candles.close, atr_periods)
                
                # Determine the position of each indicator
                df['rsi_position'] = np.where(df['rsi'] > 70, 'overbought', np.where(df['rsi'] < 30, 'oversold', 'neutral'))
                df['sma_position'] = np.where(df['close'] > df['sma'], 'above', 'below')
                df['ema_position'] =np.where(df['close'] > df['ema'], 'bullish', 'bearish')
                df['macd_position'] = np.where(df['macd'] > df['macdsignal'], 'above', 'below')
                df['bbands_position'] = np.where(df['close'] > df['upperband'], 'above', np.where(df['close'] < df['lowerband'], 'below', 'inside'))
                df['ichimoku_position'] = np.where((df['close'] > df['senkou_span_a']) & (df['close'] > df['senkou_span_b']), 'above', np.where((df['close'] < df['senkou_span_a']) & (df['close'] < df['senkou_span_b']), 'below', 'inside'))
                df['atr_position'] = np.where(df['close'] > df['atr'], 'above', 'below')
                df['fib_retracement_position'] = np.where(df['close'] > df['fib_levels'], 'above', 'below')
                df['trendline_position'] = np.where(df['close'] > df['trendlines'], 'above', 'below')
                df['macd_crossover_position'] = np.where(df['macd_crossover'] > 0, 'above', 'below')
                df['stochastic_crossover_position'] = np.where(df['stochastic_crossover'] > 0, 'above', 'below')
                # Determine if the market is trending or ranging
                is_buy= (buy_orderzz==True)and(order_type_2=='Buy')and(set_1 =='Buy')and(ATR=='Buy')and(df['sma_position']=='above')and(df['rsi_position']=='overbought')and(df['ichimoku_positions']=='above')and(df['macd_position']=='above')and(df['fib_retracement_position']=='above')and(df['ema_position']=='bullish')and(df['macd_crossover_position']=='above')and(df['bbands_position']=='above')and(df['stochastic_crossover_position']=='above')and(df['trendline_position']=='above')
                is_sell = (sell_orderzz==True)and(order_type_2 == 'Sell')and(set_1=='Sell')and(ATR == 'Sell')and(df['sma_position']=='below')and(df['rsi_position']=='oversold')and(df['ichimoku_positions']=='below')and(df['macd_position']=='below')and(df['fib_retracement_position']=='below')and(df['ema_position']=='bearish')and(df['macd_crossover_position']=='below')and(df['bbands_position']=='below')and(df['stochastic_crossover_position']=='below')and(df['trendline_position']=='below')
                # Retrieve current price information
                prices = await connection.get_symbol_price(symbol)
                current_price = prices['ask']
                if is_buy:
                    # Calculate prices at pips above and below the current price
                    take_profit = current_price + (20 * 0.0001)  # Assuming 5 decimal places
                    stop_loss = current_price - (10 * 0.0001)
                    try:
                        # calculate margin required for trade
                        first_margin= await connection.calculate_margin({
                            'symbol': symbol,
                            'type': 'ORDER_TYPE_BUY',
                            'volume': 0.01,
                            'openPrice':  current_price
                        })
                        '''
                        second_margin= await connection.calculate_margin({
                            'symbol': symbol,
                            'type': 'ORDER_TYPE_BUY',
                            'volume': 0.02,
                            'openPrice':  current_price
                        })'''
                        if first_margin<((4/100)*account_balance):
                            result = await connection.create_market_buy_order(
                                symbol,
                                volume,
                                stop_loss,
                                take_profit,
                                {'trailingStopLoss': {
                                        'distance': {
                                            'distance': 10,
                                            'units': 'RELATIVE_PIPS'
                                        }
                                    }
                                })
                        else:
                            pass
                        print('Trade successful, result code is ' + result['stringCode'])
                    except Exception as err:
                        print('Trade failed with error:')
                        print(api.format_error(err))

                elif is_sell:
                    # Calculate prices at pips above and below the current price
                    stop_loss = current_price + (10 * 0.0001)  # Assuming 5 decimal places
                    take_profit = current_price - (20 * 0.0001)
                    try:
                        # calculate margin required for trade
                        first_margin= await connection.calculate_margin({
                            'symbol': symbol,
                            'type': 'ORDER_TYPE_SELL',
                            'volume': 0.01,
                            'openPrice':  current_price,
                        })
                        '''
                        second_margin= await connection.calculate_margin({
                            'symbol': symbol,
                            'type': 'ORDER_TYPE_SELL',
                            'volume': 0.02,
                            'openPrice':  current_price
                        })'''
                        
                        if first_margin<((4/100)*account_balance):
                            result = await connection.create_market_sell_order(
                                symbol,
                                0.01,
                                stop_loss,
                                take_profit,
                                {'trailingStopLoss': {
                                        'distance': {
                                            'distance': 10,
                                            'units': 'RELATIVE_PIPS'
                                        }
                                    }
                                })
                        else:
                            pass
                    except Exception as err:
                        print('Trade failed with error:')
                        print(api.format_error(err))
            await asyncio.sleep(120)
    except Exception as e:
        print(f"Error connecting to MetaTrader account: {e}")
        return

asyncio.run(main())

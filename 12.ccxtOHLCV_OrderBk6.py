# -*- coding: utf-8 -*-
import time
import pytz
from csv import writer
import asyncio
import os
import sys
import datetime
import ccxt.async_support as ccxt  # noqa: E402

from csv import writer
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import os
import pytz
import datetime

today_date_UTC = str(datetime.datetime.now(tz=pytz.timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")).split()[0]
print(today_date_UTC)
today_date_UTC_long = str(datetime.datetime.now(tz=pytz.timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")).split()
print(today_date_UTC_long)
exchange = '12. Exchange ALL_INFO (Timezone UTC)'
platform = 'binance'
pair = 'BTC-USD'
csv = '.csv'
fname_main_dir = 'C:/Users/malco/Desktop/Automation'#googlecloud
fname1 = fname_main_dir + '/' + '{}'.format(exchange)  # exchange folder
fname2 = fname1 + '/' + '{}'.format(platform)  # Creates platform folder eg. Binance
fname3 = fname2 + '/' + '{}'.format(pair)  # Creates pair folder eg. BTC-USD
fname4 = fname3 + '/' + '{}'.format(today_date_UTC)  # Creates date folder eg. 2020-06-18
fname5 = fname4 + '/' + '{}'.format(platform + '_' + today_date_UTC + '_' + pair + csv)  # Creates final folder: Binance-BTC-USD-2020-06-18.csv


def make1_dir_exchange():  # Creates "Exchange" Folder
    if not os.path.exists(fname1):
        os.makedirs(fname1)
        print('dir made')
    else:
        print('path exists:', fname1)


def make2_dir_platform():  # Creates platform folder eg. Binance
    if not os.path.exists(fname2):
        os.makedirs(fname2)
        print('dir made')
    else:
        print('path exists:', fname2)


def make3_dir_pair():  # Creates pair folder eg. BTC-USD
    if not os.path.exists(fname3):
        os.makedirs(fname3)
        print('dir made')
    else:
        print('path exists:', fname3)


def make4_dir_pair():  # Creates date folder eg. 2020-06-18
    if not os.path.exists(fname4):
        os.makedirs(fname4)
        print('dir made')
    else:
        print('path exists:', fname4)


def make5_dir_pair():  # Creates final folder: Binance-BTC-USD-2020-06-18.csv
    if not os.path.exists(fname5):
        with open(fname5, 'a+', newline='') as csv0:
            csvwriter0 = writer(csv0)
            csvwriter0.writerow([
'symbol',
'timestamp',
'datetime',
'high',
'low',
'Bids',
'BidVol',
'Asks',
'AskVol',
'vwap',
'open',
'close',
'last',
'previousClose',
'change',
'percentage',
'baseVolume',
'quoteVolume',

'priceChange',
'priceChangePercent',
'weightedAvgPrice',
'prevClosePrice',
'lastPrice',
'lastQty',
'askPrice',
'askQty',
'openPrice',
'highPrice',
'lowPrice',
'volume',
'quoteVolume',
'openTime',
'closeTime',
'firstId',
'lastId',
'count'])
            csv0.close()
            print('Creating CSV file and respective Col names')
    else:
        print('CSV File Exists:', fname5)


make1_dir_exchange()
make2_dir_platform()
make3_dir_pair()
make4_dir_pair()
make5_dir_pair()

import pandas as pd

exchange_ = 'binance'



async def main(symbol):
    # you can set enableRateLimit = True to enable the built-in rate limiter
    # this way you request rate will never hit the limit of an exchange
    # the library will throttle your requests to avoid that
    # exchange = ccxt.binance({#ACTUAL
    exchange = ccxt.binance({

        'enableRateLimit': True,  # this option enables the built-in rate limiter
        'rateLimit': 1,  # once every 3 seconds, 20 times per minute – will work #check
        # 'verbose': True

    })
    count = 0
    print('fileName of CSV is:', fname5)

    while True:
        if count == 0:
            # while count<5:
            tic = time.time()
            print('______________________________count {}_______________________________________'.format(count))
            print('--------------------------------------------------------------')
            datetime_unix = exchange.milliseconds()  # changed
            datetime_read = datetime.datetime.utcfromtimestamp(int(datetime_unix) / 1000)  # 2020-06-19 04:11:24.165000
            datetime_read_2 = datetime_read.strftime('%H:%M:%S.%f')  # 04:11:24.165000

            ticker = await exchange.fetch_ticker(symbol)  # 0actual

            toc = time.time()
            tocketty = toc - tic
            print('time taken is:', tocketty)


            count += 1
        else:
            # while count<5:
            tic = time.time()
            print('______________________________count {}_______________________________________'.format(count))
            print('--------------------------------------------------------------')
            datetime_unix = exchange.milliseconds()  # changed
            datetime_read = datetime.datetime.utcfromtimestamp(int(datetime_unix) / 1000) #2020-06-19 04:11:24.165000
            datetime_read_2 = datetime_read.strftime('%H:%M:%S.%f') #04:11:24.165000


            # this can be any call really
            ticker = await exchange.fetch_ticker(symbol)  # 0actual

            print('ticker:', ticker) #ccxt1
            # print(ticker['bids'][99], ticker['asks'][99]) #ccxt5
            print('bid ask:', ticker['bid'], ticker['ask'])  # ccxt5
            print('bid ask:', ticker['bid'], ticker['ask'])  # ccxt5
            # print('tickertest:', ticker['ticker'])

            # working
            symbols_ = ticker['symbol']
            timestamp = ticker['timestamp']
            datetime_exchng = ticker['datetime']
            high = ticker['high']
            low = ticker['low']
            bid = ticker['bid']
            bidVolume = ticker['bidVolume']
            ask = ticker['ask']
            askVolume = ticker['askVolume']
            vwap = ticker['vwap']
            opened = ticker['open']#cannot
            close = ticker['close']
            last = ticker['last']
            previousClose = ticker['previousClose']
            change = ticker['change']
            percentage = ticker['percentage']
            baseVolume = ticker['baseVolume']
            quoteVolume = ticker['quoteVolume']

            info = ticker['info']  # 'info': {...........}
            #
            priceChange = info['priceChange']  # cannot
            priceChangePercent = info['priceChangePercent']
            weightedAvgPrice = info['weightedAvgPrice']
            prevClosePrice = info['prevClosePrice']
            lastPrice = info['lastPrice']
            lastQty = info['lastQty']
            askPrice = info['askPrice']
            askQty = info['askQty']
            openPrice = info['openPrice']
            highPrice = info['highPrice']
            lowPrice = info['lowPrice']
            volume = info['volume']
            quoteVolume = info['quoteVolume']
            openTime = info['openTime']
            closeTime = info['closeTime']
            firstId = info['firstId']
            lastId = info['lastId']
            count_info = info['count']

            bid1 = ticker['bid']
            ask1 = ticker['ask']
            bid1_vol = ticker['bid']
            ask1_vol = ticker['ask']

            print(datetime_read_2, bid1, bid1_vol, ask1, ask1_vol)
            toc = time.time()
            toe = toc - tic
            tocketty = tocketty + toe
            avg_tocky = tocketty / count
            print('                 Average time taken:', avg_tocky)
            print('                 TOTAL Time Run (Since Inception):', tocketty)
            # print('                 Time Unable to print:', unable_print)
            print('time taken is:', toe)


            with open(fname5, 'a+', newline='') as csv:
                csvwriter = writer(csv)
                csvwriter.writerow(
[symbols_,
 timestamp,
datetime_exchng,
high,
low,
bid,
bidVolume,
ask,
askVolume,
vwap,
opened,
close,
last,
previousClose,
change,
percentage,
baseVolume,
quoteVolume,

priceChange,
priceChangePercent,
weightedAvgPrice,
prevClosePrice,
lastPrice,
lastQty,
askPrice,
askQty,
openPrice,
highPrice,
lowPrice,
volume,
quoteVolume,
openTime,
closeTime,
firstId,
lastId,
count_info])
            count += 1
        # for i in ticker:
        #     print(i)
# asyncio.get_event_loop().run_until_complete(main('BTC/USDT'))#ACTUAL


count_all_all = 0
while_true_count1 = 0
unable_print = 0
for i in range(0, 1000000000000):
    print('________________________________________Master Section Count{}_____________________________'.format(i))
    while True:
        try:
            while_true_count1 += 1
            print('attempting')
            if count_all_all == 0:
                tic = time.time()
                asyncio.get_event_loop().run_until_complete(main('BTC/USDT'))  # ACTUAL
                toc = time.time()
                tocketty = toc - tic
                count_all_all += 1
            else:
                tic = time.time()
                asyncio.get_event_loop().run_until_complete(main('BTC/USDT'))  # ACTUAL
                print('section2_____________________________________{}_______________________'.format(count_all_all))

                toc = time.time()
                toe = toc - tic
                print('                 Time Taken to run (Current) program:', toe)
                tocketty = tocketty + toe
                avg_tocky = tocketty / while_true_count1
                print('                 Average time taken:', avg_tocky)
                print('                 TOTAL Time Run (Since Inception):', tocketty)
                print('                 Time Unable to print:', unable_print)

                count_all_all += 1
        except:
            unable_print += 1
            continue
        break

# asyncio.get_event_loop().run_until_complete(main('BTC/USDT'))
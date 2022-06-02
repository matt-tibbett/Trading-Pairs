#!/usr/bin/python3

import requests
import json

exchangeList = [
    { 
    'name': 'Binance', 
    'url': 'https://api.binance.com/api/v3/exchangeInfo',
    'symbolColumn': ['symbols'] 
    },
    { 
    'name': 'Bybit', 
    'url': 'https://api-testnet.bybit.com/v2/public/tickers', 
    'symbolColumn': ['result']
    },
    { 
    'name': 'Kucoin', 
    'url': 'https://api.kucoin.com/api/v1/market/allTickers', 
    'symbolColumn': ['data', 'ticker']
    }
]

exchange = exchangeList[2]

r = requests.get(exchange['url'])
data_json = r.json()

binsymbols = []

for x in data_json[(exchange['symbolColumn'])]:
    if x["symbol"].endswith("USDT"):
        binsymbols.append(x["symbol"][:-4])

print(f"There are {len(binsymbols)} USDT pairs on {exchange['name']}")

binsymbols.sort()

for sym in binsymbols:
    print(sym)

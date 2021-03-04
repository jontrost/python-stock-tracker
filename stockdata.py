import urllib.request as request
import json

def get_stock_price(stock):
    source = request.urlopen(f"https://financialmodelingprep.com/api/v3/quote/{stock}?apikey=ea998f3c010a894ff2f028237e4bd572").read()
    data = json.loads(source)
    if not data:
        return 0
    else: 
        return data[0]['price']

while True:
    ticker_symbol = input("Enter a stock ticker symbol to receive price data: ").upper()
    price = get_stock_price(ticker_symbol)
    if price == 0:
        print(f"The stock ticker symbol '{ticker_symbol}' is invalid")
    else:
        print(f"{ticker_symbol} price = {price}")
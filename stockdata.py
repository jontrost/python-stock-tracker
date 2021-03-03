import urllib.request as request
import json

def get_stock_price(stock):
    source = request.urlopen(f"https://financialmodelingprep.com/api/v3/quote/{stock}?apikey=ea998f3c010a894ff2f028237e4bd572").read()
    data = json.loads(source)
    price = data[0]['price']
    return price

price = get_stock_price("GME")
print(f"GME price = {price}")
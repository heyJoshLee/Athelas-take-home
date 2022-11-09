import requests
import csv
from api_key import API_KEY

base_url = 'https://finnhub.io/api/v1/quote'
stocks_to_query = ['AAPL', 'AMZN', 'NFLX', 'META', 'GOOGL']

latest_prices = []

for symbol in stocks_to_query:
  URL = base_url + '?symbol=' + symbol + '&token=' + API_KEY
  r = requests.get(URL)
  res = r.json()
  latest_prices.append({
    'ticker': symbol,
    'data': res
  })

most_volatile_stock = ''

for i in range(len(latest_prices)):
  stock = latest_prices[i]
  if i == 0:
    most_volatile_stock = stock
  else:
    if abs(stock['data']['dp']) > abs(most_volatile_stock['data']['dp']):
      most_volatile_stock = stock


with open('output.csv', 'w') as f:
  writer = csv.writer(f)
  headers = ['stock_symbol', 'percentage_change', 'current_price', 'last_close_price']
  writer.writerow(headers)
  writer.writerow([
    most_volatile_stock['ticker'],
    most_volatile_stock['data']['dp'],
    most_volatile_stock['data']['c'],
    most_volatile_stock['data']['pc']
  ])
  
  f.close

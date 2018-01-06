import pandas_datareader as pdr
from datetime import datetime
import json

SYMBOLS = ['XIC.TO', 'VUS.TO', 'VSB.TO', 'ZEF.TO', 'VEF.TO', 'VEE.TO', 'VRE.TO', 'XEN.TO', 'DSI', 'CLF.TO', 'ESGD', 'ESGE', 'REET']

for symbol in SYMBOLS:
  data = pdr.get_data_yahoo(symbols=symbol, start=datetime(2012,1,1), end=datetime.today())
  # print data['Date'] + ', ' + data['Adj Close']
  # print

  # for date, num in zip(list(data.index),list(data['Adj Close'])):
  #   print date + "," + num

  # print data.to_json(orient="index", date_format='iso')
  # print data.reset_index()

  data = data.reset_index().to_json(None, orient='records', date_format='iso')
  data = json.dumps(data, indent=4, separators=(',', ': '))
  print data

  break
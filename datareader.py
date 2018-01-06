'''
Script made to import data from yahoo finance
Exports CSV files from 2012/1/1 to datetime.today()
'''
from datetime import datetime

import csv
import pandas_datareader as pdr

SHORTS = ['XIC', 'VUS', 'VSB', 'ZEF', 'VEE',
          'VEF', 'VRE', 'XEN', 'DSI', 'CLF',
          'ESGD', 'ESGE', 'REET']
SYMBOLS = ['XIC.TO', 'VUS.TO', 'VSB.TO', 'ZEF.TO', 'VEE.TO',
           'VEF.TO', 'VRE.TO', 'XEN.TO', 'DSI', 'CLF.TO',
           'ESGD', 'ESGE', 'REET']

for i, symbol in enumerate(SYMBOLS):
    print 'Starting on ' + SHORTS[i]
    data = pdr.get_data_yahoo(symbols=symbol, start=datetime(2012, 1, 1), end=datetime.today())
    filename = 'export/' + SHORTS[i] + '-ALL-reduced.csv'
    with open(filename, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for index, row in data.iterrows():
            time = index.strftime('%Y-%m-%d')
            adj_close = row['Adj Close']
            csvwriter.writerow([time, adj_close])
        csvfile.close()

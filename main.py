import pandas as pd
import os

assert 'data' in os.listdir()


files = os.listdir('data')
edstat = {'country_series': 0,
          'data': 1,
          'footnote': 2,
          'country': 3,
          'series': 4,
          'excel': 5}

for key in edstat:
    if files[edstat[key]][-3:] == 'csv':
        edstat[key] = pd.read_csv('data/' + files[edstat[key]])
    elif files[edstat[key]][-3:] == 'lsx':
        edstat[key] = pd.read_excel('data/' + files[edstat[key]])


import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime

t = []
r = datetime.today().weekday()
print(r)


today = datetime.today().strftime("%Y-%m-%d")
print(today)

yf.pdr_override()

samsung = pdr.get_data_yahoo('005930.KS', start=today, end=today)

print('--------------------------------------------')
print(samsung)
print('--------------------------------------------')
print(samsung.index)
print('--------------------------------------------')
print(samsung.columns)

plt.plot(samsung.index, samsung.Close, 'b', label='Samsung Electronics')
# plt.show()

samsung_tests = samsung

print('--------------------------------------------')
print(samsung_tests)
print('--------------------------------------------')

dataTest = 'dataTest'

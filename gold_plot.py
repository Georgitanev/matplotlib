# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 08:43:39 2020

@author: G
dataset source:https://datahub.io/core/gold-prices#python
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib.pyplot import figure
import matplotlib.dates as mdates
plt.xkcd()

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)

file_source = 'D:\\git\\24_09_2019_download_repos\\matplotlib\\gold-prices_zip\\archive\\annual.csv'
data = pd.read_csv(file_source)

df = data[50:]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m').dt.strftime('%Y-%m')

plt.gcf().autofmt_xdate()
fig, ax = plt.subplots(figsize=(20, 10))
plt.title('Gold price')
plt.xlabel('Dates Y-m')
plt.ylabel('Gold price')
plt.legend(['Gold price'])

plt.plot_date(df['Date'], df['Price'], color='b', linestyle='-', label='All Devs')
plt.show()


fig.savefig('Gold_price_month.png')

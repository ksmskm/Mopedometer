import sqlite3
import random
import time
import datetime

import numpy as np
import matplotlib as mpl
# 'Agg' backend doesn't require a Display
mpl.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('test.db')
curs = conn.cursor()
graphArray = []

for row in curs.execute("SELECT * FROM temps"):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(', ')

    #Program gets 'None' when thermocouple is detached
    if splitInfo[1] != 'None':
        graphArrayAppend = splitInfo[0] + ',' + splitInfo[1]
    else:
        graphArrayAppend = splitInfo[0] + ',' + str(random.randint(0, 100))
    graphArray.append(graphArrayAppend)

datestamp, value = np.loadtxt(graphArray,delimiter=',', 
        unpack=True, converters={ 0: mdates.strpdate2num('%Y-%m-%d %H:%M:%S')})

fig = plt.figure()

rect = fig.patch

ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)
fig.savefig('temp.png')

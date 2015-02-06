import sqlite3
import time
import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('test.db')
curs = conn.cursor()
graphArray = []

for row in curs.execute("SELECT * FROM temps"):
#    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
 #   splitInfo = startingInfo.split(',')
  #  for col in range(len(splitInfo)):
#	print splitInfo[col] + '_'
    print 'row'

#    graphArrayAppend = splitInfo[0] + ',' + splitInfo[1]
#    graphArray.append(graphArrayAppend)

#timestamp, value = np.loadtxt(graphArray,delimiter = ',', unpack = True, converters = { 0: mdates.strpdate2num(' %H:%M:%S')})

#fig = plt.figure()

#rect = fig.patch

#ax1 = fig.add_subplot(1,1,1, axisbg='white')
#plt.plot_date(x = timestamp, y = value, fmt='b-', label = 'value', linewidth=2)
#plt.show()

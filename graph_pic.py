#!/usr/bin/env python

# serves a .png file of a graph from 'test.db' file
#
# this is a temporary solution to demonstrate
# the integration of db, graphing and server tools & is being accessed
# via apache in a cgi-bin/ folder

import cgitb
cgitb.enable()

import sqlite3
import time
import sys
import datetime

import os
import tempfile
# write matplotlib files to writable directory
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()

import numpy as np
import matplotlib as mpl
# 'Agg' backend doesn't require a Display
mpl.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('/home/pi/Mopedometer/test.db')
curs = conn.cursor()
graphArray = []

for row in curs.execute("SELECT * FROM temps"):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(', ')

    #Program gets 'None' when thermocouple is detached
    if splitInfo[1] != 'None':
        graphArrayAppend = splitInfo[0] + ',' + splitInfo[1]
    else:
        graphArrayAppend = splitInfo[0] + ',' + str(0)
    graphArray.append(graphArrayAppend)

datestamp, value = np.loadtxt(graphArray,delimiter=',', 
        unpack=True, converters={ 0: mdates.strpdate2num('%Y-%m-%d %H:%M:%S')})

fig = plt.figure()

rect = fig.patch

ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)

# save the plot as a png and output directly to webserver
print "Content-Type: image/png\n"
fig.savefig( sys.stdout, format='png' )

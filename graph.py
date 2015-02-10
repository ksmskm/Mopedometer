#!/usr/bin/env python

import cgitb
cgitb.enable()

import sqlite3
import os
import tempfile
# write matplotlib files to writable directory
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()

import matplotlib as mpl
# 'Agg' backend doesn't require a Display
mpl.use('Agg')

conn = sqlite3.connect('test.db')
curs = conn.cursor()

print "\nEntire database contents:\n"
for row in curs.execute("SELECT * FROM temps"):
    print row
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')

conn.close()

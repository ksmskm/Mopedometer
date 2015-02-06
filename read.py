#!/usr/bin/env python
# Let printing work the same in Python 2 and 3
from __future__ import print_function

import sqlite3

conn = sqlite3.connect('test.db')

curs = conn.cursor()

print("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM temps"):
    print(row)

conn.close()

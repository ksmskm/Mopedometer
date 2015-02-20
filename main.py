#!/usr/bin/env python

#no byte code for convenience/experimentation
import sys
sys.dont_write_bytecode = True

import time
import sqlite3
import interface
import thermocouple

lcd_plate   = interface.lcd_plate()   
egt_sensor  = thermocouple.egt_sensor()
setPoint    = 1100
dbfilename  = '/home/pi/Mopedometer/test.db'

while True:
    if lcd_plate.up_pressed():  

        # Prep db & display
        conn = sqlite3.connect(dbfilename)
        curs = conn.cursor()
        lcd_plate.prepDisplay()

        # Log & Display Exhaust Gas Temps.            
        runLogging = True                             
        while runLogging:
            temp = egt_sensor.readTempF()

            # Query SQL DB 'temps'
            sqlString = "INSERT INTO temps values(datetime('now'), (?))"
            curs.execute(sqlString, (temp,))
            conn.commit()

            lcd_plate.displayEGT(temp)

            # alert if temp goes over a set point.
            if temp >= setPoint:
                lcd_plate.flash(10, .05) 
            else:
                lcd_plate.refresh(.5)

            # DOWN button to stop logging.
            if lcd_plate.down_pressed():
                conn.close()
                lcd_plate.displayOFF()
                runLogging = False

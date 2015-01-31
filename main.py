import os
import time
import math
import sqlite3
import MAX31855
import Adafruit_GPIO.SPI as SPI
import Adafruit_CharLCD as LCD

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Overheat threshold point
setPoint = 1000

# Prep database 
conn = sqlite3.connect('test.db')
curs = conn.cursor()

# Prep LCD
# Char LCD plate button names.
SELECT                  = 0
RIGHT                   = 1
DOWN                    = 2
UP                      = 3
LEFT                    = 4

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

while True:
    if lcd.is_pressed(UP):
        # Log & Display Exhaust Gas Temps. DOWN button to SHUTDOWN.
        lcd.message('EGT: ')
        while not lcd.is_pressed(DOWN):
            temp = c_to_f(sensor.readTempC())

            # rudimentary protection against input noise
            if not temp < 0:

                curs.execute("INSERT INTO temps values(time('now'), (?))", (temp,))
                conn.commit()

                lcd.set_cursor(4, 0)
                lcd.message('{:12.0f}'.format(temp))

                if temp >= setPoint:
                    for i in range(10):
                         lcd.set_color(1.0, 0.0, 0.0)
                         time.sleep(0.02)
                         lcd.set_color(0.0, 0.0, 0.0)
                else:
                    lcd.set_color(1.0, 1.0, 1.0)
                    time.sleep(0.2)

        conn.close()
        lcd.clear()
        lcd.set_backlight(False)
        os.system("sudo shutdown -h now")

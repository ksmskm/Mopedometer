import os
import time
import math
import sqlite3
import MAX31855
import Adafruit_GPIO.SPI as SPI
import Adafruit_CharLCD as LCD

# Raspberry Pi hardware SPI configuration (from Adafruit MAX31855).
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Overheat point (A relatively static value in application)
setPoint = 80

# Char LCD plate button names.
SELECT                  = 0
RIGHT                   = 1
DOWN                    = 2
UP                      = 3
LEFT                    = 4

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

def main():
    while True:
        if lcd.is_pressed(UP):
            runLogging = True                       
            maxTemp = float("-inf")

            # Prep database 
            conn = sqlite3.connect('test.db')
            curs = conn.cursor()

            # prep display
            lcd.message('EGT: ')
            lcd.set_cursor(0, 1)
            lcd.message('MAX: ')

            # Log & Display Exhaust Gas Temps.            
            while runLogging:
                temp = c_to_f(sensor.readTempC())

                sqlString = "INSERT INTO temps values(time('now'), (?))"
                curs.execute(sqlString, (temp,))
                conn.commit()

                # display clean data & not noise.
                if not math.isnan(temp) and temp >= 0:
                    lcd.set_cursor(4, 0)
                    lcd.message('{:12.0f}'.format(temp))

                # update/display max temperature
                if temp > maxTemp:
                    maxTemp = temp
                    lcd.set_cursor(0, 1)
                    lcd.message('{:12.0f}'.format(maxTemp))

                # alert if temp goes over a set point.
                if temp >= setPoint:
                    flashLCD(10, .02) 
                else:
                    lcd.set_color(1.0, 1.0, 1.0)
                    time.sleep(0.2)

                # DOWN button to stop logging.
                if lcd.is_pressed(DOWN):
                    conn.close()
                    lcd.clear()
                    lcd.set_backlight(False)
                    runLogging = False

# Convert celsius to fahrenheit.
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def flashLCD(times, duration):
    for i in range(times):
        lcd.set_color(1.0, 0.0, 0.0)
        time.sleep(duration)
        lcd.set_color(0.0, 0.0, 0.0)

if __name__ == "__main__":
    main()

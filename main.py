import Adafruit_CharLCD as LCD
import time
import math
import Adafruit_GPIO.SPI as SPI
import MAX31855

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#Overheat threshold point
setPoint = 80

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()
lcd.message('EGT: ')

# Loop printing measurements every second.
while True:
        temp = c_to_f(sensor.readTempC())

        if not math.isnan(temp) or temp < 0:

                lcd.set_cursor(4, 0)
                lcd.message('{:12.0f}'.format(temp))

                if temp >= setPoint:
			for i in range(5):
				 lcd.set_color(1.0, 0.0, 0.0)
				 time.sleep(0.02)
                       		 lcd.set_color(0.0, 0.0, 0.0)
		else:
                	lcd.set_color(1.0, 1.0, 1.0)
			time.sleep(0.5)

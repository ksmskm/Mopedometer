# Provides an interface to a exhaust gas temperature thermocouple
# based on the MAX31855 library from Adafruit. It runs through
# the RPi's hardware SPI.

# byte code for convenience/experimentation
import sys
sys.dont_write_bytecode = True

import MAX31855
import Adafruit_GPIO.SPI as SPI

# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
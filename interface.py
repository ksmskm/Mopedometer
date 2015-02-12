# byte code for convenience/experimentation
import sys
sys.dont_write_bytecode = True

import time
import math
import Adafruit_CharLCD as LCD

class lcd_plate(LCD.Adafruit_CharLCDPlate):

    def __init__(self):
        super(lcd_plate, self).__init__()

    def prepDisplay(self):
        self.set_backlight(True)
        self.message('EGT: ')
        self.set_cursor(0, 1)
        self.message('CYL: ')

    def flash(self, times, duration):
        for i in range(times):
            self.set_color(1.0, 0.0, 0.0)
            time.sleep(duration)
            self.set_color(0.0, 0.0, 0.0)

    def up_pressed(self):
        return self.is_pressed(UP)

    def down_pressed(self):                           
        return self.is_pressed(DOWN)

    def right_pressed(self):
        return self.is_pressed(RIGHT)
    
    def left_pressed(self):
        return self.is_pressed(LEFT)

    def select_pressed(self):
        return self.is_pressed(SELECT)

    def displayEGT(self, temp):
        # display clean data & not noise.
        if not math.isnan(temp) and temp >= 0:
            self.set_cursor(4, 0)
            self.message('{:12.0f}'.format(temp))

    def displayOFF(self):
        self.clear()
        self.set_backlight(False)

    def refresh(self, duration):
        self.set_color(1.0, 1.0, 1.0)
        time.sleep(duration)

# byte code for convenience/experimentation
import sys
sys.dont_write_bytecode = True

import time
import Adafruit_CharLCD as LCD

class lcd_plate(LCD.Adafruit_CharLCDPlate):

    def __init__(self):
        super()

    def prepDisplay():
        set_backlight(True)
        message('EGT: ')
        set_cursor(0, 1)
        message('CYL: ')

    def flash(times, duration):
        for i in range(times):
            set_color(1.0, 0.0, 0.0)
            time.sleep(duration)
            set_color(0.0, 0.0, 0.0)

    def up_pressed():
        return is_pressed(UP)

    def down_pressed():                           
        return is_pressed(DOWN)

    def right_pressed():
        return is_pressed(RIGHT)
    
    def left_pressed():
        return is_pressed(LEFT)

    def select_pressed():
        return is_pressed(SELECT)

    def displayEGT(temp):
        # display clean data & not noise.
        if not math.isnan(temp) and temp >= 0:
            lcd.set_cursor(4, 0)
            lcd.message('{:12.0f}'.format(temp))

    def displayOFF():
        lcd.clear()
        lcd.set_backlight(False)

    def refresh(duration):
        set_color(1.0, 1.0, 1.0)
        time.sleep(duration)
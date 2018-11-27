# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import time
import pytm1638
import RPi.GPIO as GPIO

class TM1638_Button:
    def __init__(self, dio, clk, stb):
        self.stb = stb
        self.display = pytm1638.TM1638(dio, clk, stb)
        display.enable(1)

    def wait_for_input(self, cb, exit):
        while True:
            keys = 0
            GPIO.output(self.stb, False)
            self.send_byte(0x42)
            for i in range(4):
                keys |= self.receive() << i
            GPIO.output(self.stb, True)
            time.sleep(0.1)

            if exit or keys > 0:
                break

        cb(keys)
        return keys

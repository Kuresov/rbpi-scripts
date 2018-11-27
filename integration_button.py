# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import pytm1638

DIO = 17		# GPIO/BCM 17
CLK = 11		# GPIO/BCM 11
STB = 22		# GPIO/BCM 22
angle = 0
display = pytm1638.TM1638(DIO, CLK, STB)

display.enable(1)

def button_press():
    global angle
    angle = 0

    while True:
        pressed = display.get_buttons()
        if pressed == 1:
        angle = 90
        display.set_led(0,1)
        elif pressed == 2:
        angle = 180
        display.set_led(1, 1)
        elif pressed == 4:
        angle = 270
        display.set_led(2, 1)
        elif pressed == 8:
        angle = 360
        display.set_led(3, 1)

        if angle > 0:
            break
	   
	return angle

# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import time
import spidev
import RPi.GPIO as GPIO
import integration_ir
import integration_stepper
import integration_display
import integration_button

def main():
    print("CP320 - Final Project")
    print("Prepared by: Alex & Pillip")
    print("Using Stepper Motor, Infrared Sensor, and TM1638 LED/7-Segment Display with Buttons\n")
    try:
        while True:
            ir_val = integration_ir.infrared_On()                
            integration_display.display_svn_segment(ir_val)

            if ir_val >= 2.0
                integration_stepper.stepper_On(45)
            
            btn_val = integration_button.button_press()
            if btn_val > 0:
                integration_stepper.stepper_On(btn_val)

            time.sleep(0.2)
    except KeyboardInterrupt:
        integration_stepper.stepper_Neutral()
        GPIO.cleanup()
        spi.close()
        pass

main()

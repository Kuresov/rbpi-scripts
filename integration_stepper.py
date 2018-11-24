# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
STEPPER_PINS = [13,16,26,21]
SLEEP_TIME = 0.01
MULTIPLIER = 5.833

stepper_sequence = [
	[GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
	[GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
	[GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
	[GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
]

GPIO.setup(STEPPER_PINS, GPIO.OUT)
total = 0

def stepper_On(val):
	global total
	total += int(val)

	# Ensure that we don't rotate several revolutions to return to neutral
	if total >= 360:
		total -= 360

	iter_given = get_steps(val)
	rotate_stepper(iter_given)

def stepper_Neutral():
	# 'total' will be the degrees from neutral we are currently
  # at. Thus, the neutral angle will be 360 - the current total.
	iter_neutral = get_steps(360 - total)
	rotate_stepper(iter_neutral)

def rotate_stepper(steps):
	while steps > 0:
		for row in stepper_sequence:
			GPIO.output(STEPPER_PINS, row)
			time.sleep(SLEEP_TIME)
		steps -= 1

def get_steps(val):
	# Convert the degree-value to the number of steps required for that angle
	return (int(val) * multiplier) / 4

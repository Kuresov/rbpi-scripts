#!/usr/bin/python
# Terry Sturtevant, May 10, 2017
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
stepper_pins=[13,16,26,21]

GPIO.setup(stepper_pins,GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])

steps_for_360 = 2100
multiplier = 5.833

total = 0

try:
	while True:
		val = raw_input("value 0..360, q=quit:")

		if val == 'q':
			break
		else:
			total += int(val)
			iter = (int(val) * multiplier) / 4
			print("iter %d", iter)

			while iter > 0:
				for row in stepper_sequence:
					GPIO.output(stepper_pins,row)
					time.sleep(0.02)
				iter -= 1

except KeyboardInterrupt:
	pass

iter_neutral = (int(360 - total) * multiplier) / 4
#print("iter_neutral %d", iter_neutral)

while iter_neutral > 0:
	for row in stepper_sequence:
		GPIO.output(stepper_pins,row)
		time.sleep(0.01)
	iter_neutral -= 1

GPIO.cleanup()

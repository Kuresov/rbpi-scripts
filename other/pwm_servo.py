import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)
p.start(6)

try:
    while True:
        val = raw_input("value 0..180, q=quit:")

        if val == 'q':
                break
        else:
		#value = float(val) / 17.1

		value = ((1 + (float(val) / 90)) / 20) * 100
		print(value)

		if value < 2.2:
			value = 2.2
		if value > 10.5:
			value = 10.5

		p.ChangeDutyCycle(value)

except KeyboardInterrupt:
	pass

p.ChangeDutyCycle(6)
time.sleep(1)
p.stop()
GPIO.cleanup()

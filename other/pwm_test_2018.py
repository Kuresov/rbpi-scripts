import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 60)  # channel=18 frequency=60Hz
p.start(50)
time.sleep(2)
try:
    while True:
            print("100")
            p.ChangeDutyCycle(100)
            time.sleep(2)
            print("99")
            p.ChangeDutyCycle(99)
            time.sleep(2)
            print("80")
            p.ChangeDutyCycle(80)
            time.sleep(2)
            print("50")
            p.ChangeDutyCycle(50)
            time.sleep(2)
            print("20")
            p.ChangeDutyCycle(20)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()

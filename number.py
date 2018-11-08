import time
import pytm1638

DIO = 17		# GPIO/BCM 17
CLK = 21		# GPIO/BCM 11
STB = 22		# GPIO/BCM 22

display = pytm1638.TM1638(DIO, CLK, STB)

display.enable(1)

try:
	while True:
		# Display number 1
		display.send_char(0, 6)

		display.set_led(0, 1)
		time.sleep(0.5)
		display.set_led(0,0)  
		time.sleep(1)

		# Display number 2
		display.send_char(1, 91)

		display.set_led(1, 1)
		time.sleep(0.5)
		display.set_led(1,0)  
		time.sleep(1)

		# Display number 3
		display.send_char(2, 79)

		display.set_led(2, 1)
		time.sleep(0.5)
		display.set_led(2,0)  
		time.sleep(1)

		# Display number 4
		display.send_char(3, 102)

		display.set_led(3, 1)
		time.sleep(0.5)
		display.set_led(3,0)  
		time.sleep(1)

		# Display number 5
		display.send_char(4, 109)

		display.set_led(4, 1)
		time.sleep(0.5)
		display.set_led(4,0)  
		time.sleep(1)

		# Display number 6
		display.send_char(5, 125)

		display.set_led(5, 1)
		time.sleep(0.5)
		display.set_led(5,0)  
		time.sleep(1)

		# Display number 7
		display.send_char(6, 7)

		display.set_led(6, 1)
		time.sleep(0.5)
		display.set_led(6,0)  
		time.sleep(1)

		# Display number 8
		display.send_char(7, 127)

		display.set_led(7, 1)
		time.sleep(0.5)
		display.set_led(7,0)  
		time.sleep(1)

		# Display number 9
		display.send_char(8, 103)

		display.set_led(8, 1)
		time.sleep(0.5)
		display.set_led(8,0)  
		time.sleep(1)

except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()

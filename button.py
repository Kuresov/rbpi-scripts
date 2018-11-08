import time
import pytm1638

DIO = 17		# GPIO/BCM 17
CLK = 21		# GPIO/BCM 11
STB = 22		# GPIO/BCM 22

display = pytm1638.TM1638(DIO, CLK, STB)

display.enable(1)

try:
	while True:
    		pressed = display.get_buttons()

		if pressed == 1:
			display.set_led(0,1)
		elif pressed == 2:
                	display.set_led(1, 1)
		elif pressed == 4:
			display.set_led(2, 1)
		elif pressed == 8:
			display.set_led(3, 1)
		elif pressed == 16:
			display.set_led(4,1)
		elif pressed == 32:
			display.set_led(5,1)
		elif pressed == 64:
			display.set_led(6,1)
		elif pressed == 128:
			display.set_led(7,1)
		else:
			done = raw_input('Want to quit? (Y/N): ')
			if (done == 'y' or done == 'Y'):
				for i in range(0,8):
					display.set_led(i,0)
				break
			else:
				print("Continuing")
		print(pressed)
    		time.sleep(3)

except KeyboardInterrupt:
	pass

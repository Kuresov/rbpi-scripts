from time import sleep
import pytm1638

DIO = 17		# GPIO/BCM 17
CLK = 11		# GPIO/BCM 11
STB = 22		# GPIO/BCM 22

display = pytm1638.TM1638(DIO, CLK, STB)

display.enable(1)

def lightup(pos):
    display.set_led(pos-1,1)
    sleep(0.1)
    display.set_led(pos-1,0)
    return None

def led_sequence(lst, lvl):
        speed_level = [1.5, 1.5, 1.0, 1.0, 0.75, 0.75, 0.5, 0.5, 0.25, 0.25]

	for pos in lst:
            print(pos)
	    display.set_led(pos-1, 1)
	    sleep(speed_level[lvl])
	    display.set_led(pos-1, 0)
	    sleep(speed_level[lvl])
	    
	return None

def display_rdy():
        display.send_char(0, 128)
        display.send_char(1, 128) 
        display.send_char(2, 128)   
        display.send_char(3, 128)   
        display.send_char(4, 128)  
        display.send_char(5, 128)   
        display.send_char(6, 128)  
        display.send_char(7, 128)
        return None

def winner():
    display.send_char(0, 63)
    display.send_char(1, 92) 
    display.send_char(2, 84)
    display.send_char(3, 121)
    return None

def loser():
    display.send_char(0, 56)
    display.send_char(1, 63) 
    display.send_char(2, 109)
    display.send_char(3, 121)
    return None


def display_go():
	num_byte = [63, 6, 91, 79, 102, 109, 125, 7, 127, 103]		# Values for: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

	display.send_char(0, 111)   # Display Segment 1
	display.send_char(1, 99)   # Display Segment 2
        sleep(2)	
        return None
    
def display_score(lvl):
	num_byte = [63, 6, 91, 79, 102, 109, 125, 7, 127, 103]		# Values for: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

	display.send_char(0, 63)   # Display Segment 1
	display.send_char(1, 84)   # Display Segment 2

	# Display Segment 5
	display.send_char(4, 56)
	# Display Segment 6
	display.send_char(5, 156)
	# Display Segment 8
	display.send_char(6, num_byte[lvl])

	return None
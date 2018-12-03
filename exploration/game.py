import exploration_button
import explor_game
from time import sleep
from random import randint

DIO = 17
CLK = 11
STB = 22
BUTTON_list = []
START_LEVEL = 0
FINAL_LEVEL = 10

def handle_buttons(button_num):
        BUTTON_list.append(button_num)
        explor_game.lightup(button_num)
        sleep(0.2)
	return None

def main():
	print("CP320 - Exploration Project - Sequence Memorization Game")
	print("Made by: Alex Kirsopp & Pillip Lee")
	global completed
  global level
  
	try:
		while START_LEVEL != FINAL_LEVEL:
			explor_game.display_score(START_LEVEL)
			completed = False
			print("Welcome to Level: ", START_LEVEL)
			LED_list = []
			global BUTTON_list
			BUTTON_list = []
                        sleep(3)
			for x in range(START_LEVEL+1):
  			n = randint(1,8)
				LED_list.append(n)
			explor_game.led_sequence(LED_list, START_LEVEL)
			explor_game.display_go()
			while True:
				buttons = exploration_button.TM1638_Button(DIO, CLK, STB)
				print("Waiting for button press...")				

				buttons.wait_for_input(handle_buttons)
				if len(BUTTON_list) == (START_LEVEL+1):
          break
        else:
          continue

			if LED_list == BUTTON_list: 	# Check if LED and Button sequences match.
				completed = True
				START_LEVEL += 1
			else:
        completed = False
        explor_game.loser()
				print("Game Over.")
				break
			    
		if completed == True:
      explor_game.winner()
      print("Game Completed! Congratulations!!")
                          
	except KeyboardInterrupt:
		pass

main()

import exploration_button.py

def handle_buttons(button_num):
    print("Button Handler -> Button pressed: ", button_num)


def main():
	print("CP320 - Exploration Project")
	print("Prepared by: Alex Kirsopp & Pillip Lee")

    try:
        while True:
            buttons = exploration_button.TM1638_Button()
            exploration_button.wait_for_input(handle_buttons, False)

    except KeyboardInterrupt:
        pass

main()

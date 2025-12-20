# All this code is NOT PRODUCTION STANDARD, but self documenting for LEARNING LEVEL.

from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, Controller as BoardController, Listener as BoardListener
from time import sleep as wait_for

TIMES_BUTTON_IS_PRESSED_DURING_MOUSE_TEST = 1
SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS = 1 
MOVEMENT_BY_PIXELS_IN_MTEST = 700

DURATION_OF_TEST_KEY_PRESS_IN_SECONDS = 3
INDIVIDUAL_TEST_KEY_PRESSED = 'a'

def individual_tests_for_Mouse():
    mouse_object = Controller()

    # Should get the mouse's current position
    wait_for(SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS)
    print(mouse_object.position) # Gets the mouse's current position after 1 second.

    # Should move mouse to top left corner
    X_COORD, Y_COORD = 0, 0
    wait_for(SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS)
    mouse_object.position = (X_COORD, Y_COORD)

    # Should move mouse to a bit right and below from top left corner by 5 pixels
    wait_for(SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS)
    mouse_object.move(MOVEMENT_BY_PIXELS_IN_MOUSE_TEST, MOVEMENT_BY_PIXELS_IN_MOUSE_TEST)

    # Click once
    wait_for(SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS)
    mouse_object.click(Button.x1, TIMES_BUTTON_IS_PRESSED_DURING_TEST)    # X1 is BACKWARD SIDE BUTTON

    wait_for(SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS)
    mouse_object.click(Button.x2, TIMES_BUTTON_IS_PRESSED_DURING_TEST)    # X2 is FORWARDS SIDE BUTTON

def individual_tests_for_Keyboard():
    board_object = BoardController()

    # Press and release the key tested for 3 second.
    wait_for(SET_TIME_DELAY_IN_SECONDS_BETWEEN_TESTS)
    board_object.press(INDIVIDUAL_TEST_KEY_PRESSED)
    wait_for(DURATION_OF_TEST_KEY_PRESS_IN_SECONDS)
    board_object.release(INDIVIDUAL_TEST_KEY_PRESSED)
    # IMP-NOTE: IT STILL ONLY PRESSES THE KEY ONCE, EVEN IF YOU ARE WAITING WITH THE KEY DOWN FOR A LONGER TIME. 

# individual_tests_for_Mouse()      # Uncomment to test simple MOUSE_KEY functioning
# individual_tests_for_Keyboard()   # Uncomment to test simple KEY_BOARD functioning

individual_tests_for_Keyboard()
quit()  # Dirty exit for testing purposes.


# ===================== MOUSE FUNCTIONS FOR LISTENER TESTING =====================
# Detects the very first mouse button press and STOPS.
def detect_the_button_clicked_once(x, y, button, pressed):
    if pressed:
        print("Clicked at: ("+str(x)+","+str(y)+"). Button pressed = ", button)
        listener.stop()

# Detects mouse clicks until the LEFT Mouse button is pressed.
def detect_the_buttons_clicked_until_left_is_pressed(x, y, button, pressed):
    if button != Button.left:
        print("Clicked at: ("+str(x)+","+str(y)+"). Button pressed = ", button)
    else:
        listener.stop()

# ================================================================================


# Below, you can replace the assigned mouse function with whichever one you want to try.
test_the_assigned_mouse_function = detect_the_buttons_clicked_until_left_is_pressed

with Listener(on_click=test_the_assigned_mouse_function) as listener:
    listener.join()

# with BoardListener()a

import threading
import keyboard
import time


#store the toggle state
toggle = False

#variables for interval and keyb
interval = 6.5
keyb = 'space'

#function to start the space pressing thread
def start_space_thread():
    space_thread = threading.Thread(target=press_space)
    space_thread.daemon = True
    space_thread.start()

# space pressing function
def press_space():
    global toggle
    while True:
        if toggle:
            keyboard.press(keyb)
            keyboard.release(keyb)
        time.sleep(interval)

def set_toggle_state(value):
    global toggle
    toggle = value

def set_interval(value):
    global interval
    try:
        interval = float(value)
    except ValueError:
        pass

def set_keyb(value):
    global keyb
    keyb = value


if __name__ == "__main__":
    start_space_thread() 

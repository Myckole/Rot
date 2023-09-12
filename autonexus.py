import time
from pynput import mouse, keyboard
import pyautogui
import threading

target_color_hex = ["#e3e3e3","#e3e3e1","#545454", "#e1e1e1", "#dddddd", "#e2e2e2", "#d6d6d6", "#cecece", "c3c3c3"]

target_x = 0
r_pressed = False

def start_autonex_thread():
    nexus_thread = threading.Thread(target=autonex_script)
    nexus_thread.daemon = True
    nexus_thread.start()

def set_auto_state(value):
    global auto
    auto = value

# check the pixel color at the specified coordinates
def check_pixel_color(x, y):
    try:
        pixel_color = pyautogui.pixel(x, y)
        r, g, b = pixel_color
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return hex_color.lower()  
    except OSError as e:
        print(f"Error accessing pixel color: {e}")
        return None

def set_hp(value):
    global target_x
    percent = float(value)  
    target_x = int(1570 + ((1910 - 1570) * (percent/100)))


kb_controller = keyboard.Controller()

# press the "r" key
def press_r():
    kb_controller.press("r")
    kb_controller.release("r")

def autonex_script():
    global r_pressed  

    target_y = 484

    current_color = check_pixel_color(target_x, target_y)

    with mouse.Listener(on_move=lambda x, y: None) as listener:
        while True:
            if auto:
                new_color = check_pixel_color(target_x, target_y)

                if new_color in target_color_hex and current_color not in target_color_hex:
                    if not r_pressed:
                        press_r()
                        r_pressed = True
                        print("Below HP threshold, 'r' key pressed.")
                else:
                    r_pressed = False

                current_color = new_color
                print("Current HEX color at ({}, {}): {}".format(target_x, target_y, current_color))
            time.sleep(0.05)  
            
# initialize r_pressed as False
r_pressed = False

if __name__ == "__main__":

    start_autonex_thread()

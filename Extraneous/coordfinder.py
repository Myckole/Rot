import signal
from pynput import mouse
import pyautogui

def get_coords(x, y):
    pixel_color = pyautogui.pixel(x, y)
    r, g, b = pixel_color
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    print("Position: ({}, {})".format(x, y))
    print("RGB Color: ({}, {}, {})".format(r, g, b))
    print("HEX Color: {}".format(hex_color))

def signal_handler(signal, frame):
    print("Exiting")
    listener.stop()

signal.signal(signal.SIGINT, signal_handler)

with mouse.Listener(on_move=get_coords) as listener:
    listener.join()

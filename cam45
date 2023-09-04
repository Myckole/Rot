import keyboard
import time

# 45 deg turn takes 0.375, 0.25, and ---- s for slow, norm, and fast cam spd's respectfully
key_l = 'q'
key_r = 'e'
speed = 0.25

# The speed for the fast setting is inaccuarate
def set_speed(value):
    global speed
    if value == 'slow':
        speed = 0.375
    elif value == 'normal':
        speed = 0.25
    elif value == 'fast':
        speed = 5/3
    else:
        print('what?')

def turn_l():
    keyboard.press(key_l)
    time.sleep(speed)
    keyboard.release(key_l)

def turn_r():
    keyboard.press(key_r)
    time.sleep(speed)
    keyboard.release(key_r)

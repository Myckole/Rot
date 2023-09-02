import PySimpleGUI as sg
import threading
import keyboard
import time

sg.theme('DarkTanBlue')
toggle = False
interval = 6.5
keyb = 'space'

def press_space():
    global toggle
    while True:
        if toggle:
            keyboard.press(keyb)
            keyboard.release(keyb)
        time.sleep(interval)

space_thread = threading.Thread(target=press_space)
space_thread.daemon = True
space_thread.start()

#This is an assortment of keybinds
options = ['Escape', 'Space', 'BackSpace', 'Tab', 'Linefeed', 'Clear', 'Return', 'Pause', 'Scroll_Lock', 'Sys_Req', 'Delete', 'Home', 'Left', 'Up', 'Right', 'Down', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

layout = [
    [sg.Checkbox('Toggle/(ctrl+shift)', key='-TOGGLE-')],
    [sg.Combo(options, key='-KEY-', default_value='space',size=[10,5], readonly=True)],
    [sg.Text('Interval (s)'), sg.InputText(str(interval), key='-INTERVAL-', size=(5,5))],
    [sg.Button('Exit')]
]

window = sg.Window('clicker', layout, keep_on_top=True)

def toggle_checkbox():
    window['-TOGGLE-'](not window['-TOGGLE-'].Get())


keyboard.add_hotkey('ctrl+shift', toggle_checkbox)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    toggle = values['-TOGGLE-']

    try:
        interval = float(values['-INTERVAL-'])
    except ValueError:
        pass
    keyb = values['-KEY-']
window.close()
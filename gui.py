import PySimpleGUI as sg
import toggle
import keyboard
import confusecntrl
import cam45
import slowcntrl

sg.theme('DarkTanBlue')

# This is an assortment of keybinds
options = ['Escape', 'Space', 'BackSpace', 'Tab', 'Linefeed',
           'Clear', 'Return', 'Pause', 'Scroll_Lock', 'Sys_Req',
           'Delete', 'Home', 'Left', 'Up', 'Right', 'Down', 'b',
           'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']

speeds = ['20','30','40','50']

break_count = 0
def lay_break():
    global break_count
    break_count += 1
    return [sg.HorizontalSeparator(key = ('break', break_count))]

lay_45cam = [sg.Text('Cam spd:'), sg.Combo(['slow', 'normal', 'fast'], key = '-CAMSPEED-', readonly=True, default_value='normal')], [sg.Text("'[' and ']' keybinds")]
#lay_auto_nexus = [sg.Checkbox('Auto Nexus', key='-AUTONEXUS-')]
lay_slow_move = [sg.Checkbox('Slow Move/(shift+`)', key='-SLOWMOVE-')]
lay_confuse_control = [sg.Checkbox('Confuse Controls/(ctrl+`)', key='-CONFUSECNTRL-')]
lay_toggle = [[sg.Checkbox('Toggle/(ctrl+shift)', key='-TOGGLE-')], [sg.Combo(options, key='-KEY-', default_value='space', size=[10, 5], readonly=True)],
              [sg.Text('Interval (s)'), sg.InputText('6.5', key='-INTERVAL-', size=(5, 5))]]

compile = [lay_toggle, lay_confuse_control, lay_45cam, lay_slow_move]
layout = []

for i in compile:
    layout.append(i)
    layout.append(lay_break())
layout = layout[:-1]

window = sg.Window('clicker', layout, keep_on_top=True)

def toggle_checkbox():
    window['-TOGGLE-'](not window['-TOGGLE-'].Get())

def confuse_checkbox():
    window['-CONFUSECNTRL-'](not window['-CONFUSECNTRL-'].Get())

def slow_checkbox():
    window['-SLOWMOVE-'](not window['-SLOWMOVE-'].Get())

def turn_l():
    cam45.turn_l()

def turn_r():
    cam45.turn_r()

keyboard.add_hotkey('shift+`', slow_checkbox)
keyboard.add_hotkey('ctrl+shift', toggle_checkbox)
keyboard.add_hotkey('ctrl+`', confuse_checkbox)
keyboard.add_hotkey('[', turn_l)
keyboard.add_hotkey(']', turn_r)

def get_gui_input():
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        toggle.set_toggle_state(values['-TOGGLE-'])
        toggle.set_interval(values['-INTERVAL-'])
        toggle.set_keyb(values['-KEY-'])
        confusecntrl.set_cntrl_state(values['-CONFUSECNTRL-'])
        cam45.set_speed(values['-CAMSPEED-'])
        slowcntrl.set_slow_state(values['-SLOWMOVE-'])

    window.close()

if __name__ == "__main__":
    toggle.start_space_thread()  

    get_gui_input()

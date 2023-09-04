import subprocess
import keyboard  
import threading


ahk_script_path = './confuse.ahk'

# track the AHK script's state
ahk_script_running = False
ahk_process = None  # Initialize ahk_process

# hotkey to toggle the AHK script
toggle_hotkey = 'ctrl + `'

def set_cntrl_state(value):
    global ahk_script_running
    ahk_script_running = value

def start_confuse_thread():
    confuse_thread = threading.Thread(target=toggle_ahk_script)
    confuse_thread.daemon = True
    confuse_thread.start()
# Function to toggle the AHK script
def toggle_ahk_script():
    global ahk_script_running, ahk_process  
    
    if ahk_script_running == True:
        ahk_script_running = False

    else:
        # Start the AHK script
        ahk_process = subprocess.Popen(['AutoHotkey.exe', ahk_script_path])
        ahk_script_running = True

# Register the hotkey to toggle the AHK script
keyboard.add_hotkey(toggle_hotkey, toggle_ahk_script)


# Keep the script running

if __name__ == "__main__":
    start_confuse_thread() 


    
    

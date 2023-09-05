import subprocess
import threading

ahk_script_path = './confuse.ahk'

# track the AHK script's state
ahk_script_running = False
ahk_process = None  # Initialize ahk_process

# hotkey to toggle the AHK script
toggle_hotkey = 'ctrl + `'

# checks if the checkbox is changed
def set_cntrl_state(value):
    global ahk_script_running
    if value != ahk_script_running:
        ahk_script_running = value
        toggle_ahk_script()

def start_confuse_thread():
    confuse_thread = threading.Thread(target=toggle_ahk_script)
    confuse_thread.daemon = True
    confuse_thread.start()

# Function to toggle the AHK script
def toggle_ahk_script():
    global ahk_script_running, ahk_process  
    
    if ahk_script_running == True:
        ahk_process = subprocess.Popen(['AutoHotKey.exe', ahk_script_path])

    elif ahk_script_running == False:
        try:
            ahk_process.terminate()
        except:
            pass

# Keep the script running

if __name__ == "__main__":
    start_confuse_thread() 


    

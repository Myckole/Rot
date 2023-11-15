import subprocess 
import threading

sc_dir = './ahk'
w_path = './w.ahk'
a_path = './a.ahk'
s_path = './s.ahk'
d_path = './d.ahk'

# track the slow script's state
slow_script_running = False
slow_process = None  # Initialize slow_process

# hotkey to toggle the slow script
toggle_hotkey = 'shift + `'

# checks if checkbox is changed
def set_slow_state(value):
    global slow_script_running
    if value != slow_script_running:
        slow_script_running = value
        toggle_slow_script()
    

def start_slow_thread():
    slow_thread = threading.Thread(target=toggle_slow_script)
    slow_thread.daemon = True
    slow_thread.start()
# Function to toggle the slow script
def toggle_slow_script():
    global slow_script_running, slow_process1, slow_process2, slow_process3, slow_process4  
    if slow_script_running == True:

        slow_process1 = subprocess.Popen(['AutoHotkey.exe', w_path], cwd=sc_dir)
        slow_process2 = subprocess.Popen(['AutoHotkey.exe', a_path], cwd=sc_dir)
        slow_process3 = subprocess.Popen(['AutoHotkey.exe', s_path], cwd=sc_dir)
        slow_process4 = subprocess.Popen(['AutoHotkey.exe', d_path], cwd=sc_dir)

    elif slow_script_running == False:
        try:
            slow_process1.terminate()
            slow_process2.terminate()
            slow_process3.terminate()
            slow_process4.terminate()
        except:
            pass

# Keep the script running

if __name__ == "__main__":
    start_slow_thread() 

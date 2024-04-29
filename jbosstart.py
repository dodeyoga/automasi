import subprocess
import pyautogui
import time
import ctypes

def jboss_batch_script(script_path):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script_path, None, None, 1)
        print("Batch script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch script: {e}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Script execution interrupted by user.")

def jboss_button():
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(120)

#jboss_script_path = r'E:\Temenos\BSGPROD\jBossBSGPROD.bat'
#jboss_batch_script(jboss_script_path)
#jboss_button()
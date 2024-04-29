import subprocess
import pyautogui
import time
import ctypes
import pygetwindow as gw

def trun_start(script_path):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script_path, None, None, 1)
        print("Batch script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch script: {e}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Script execution interrupted by user.")

def trun_actions():
        time.sleep(10)
        pyautogui.typewrite('FAJARSH')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('P@Ssw0rd12')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('SGP')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('TS, I TSM')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('6')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('START')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'u')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'u')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)

def trunstart_close(program_name):
    try:
        window = gw.getWindowsWithTitle(rf'"{program_name}"')[0]
        window.close()
        print(f"Closed {program_name} window.")
    except IndexError:
        print(f"Error: {program_name} window not found.")

#start_script_path = r'E:\Temenos\BSGPROD\tRun.bat'
#trun_start(start_script_path)
#trun_actions()
#time.sleep(5)
#trunstart_close('tafj.properties')
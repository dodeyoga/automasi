import pygetwindow as gw
import pyautogui
import time

def activate_window(window_name):
    window = gw.getWindowsWithTitle(window_name)
    if len(window) > 0:
        window[0].activate()
        return window[0]
    else:
        print(f"Window with name '{window_name}' not found.")
        return None

def perform_actions_on_window(window):
    if window is not None:
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(80)
        pyautogui.press('Y')
        time.sleep(5)
        pyautogui.press('enter')
        print("Close Session JBos Success")

#window_name = "Administrator:  JBoss BSGPROD"
#activated_window = activate_window(window_name)
#perform_actions_on_window(activated_window)
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

window_name = "tafj.properties"
activated_window = activate_window(window_name)
#perform_actions_on_window(activated_window)
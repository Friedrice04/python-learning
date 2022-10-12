import time
import pyautogui
i=0
while i < 10000:
    time.sleep(.3)
    pyautogui.press('right')
    i+=1
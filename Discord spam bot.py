import pyautogui
import time
pyautogui.FAILSAFE = True
time.sleep(5)

f = open("""The Bee Movie""", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
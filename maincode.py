import pyautogui; import time
script = open('NAME OF FILE', 'r')
time.sleep(5)
for line in script:
    pyautogui.write(line)
    pyautogui.press('enter')
    time.sleep(1)

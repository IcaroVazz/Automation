import pyautogui
import time


#abrindo o chrome e indo para o wpp

time.sleep(4)

pyautogui.click(888,693)
pyautogui.click(712,221)
pyautogui.click(940,180,clicks=3)
pyautogui.hotkey("ctrl", "c")
#pyautogui.press("Down")
 
pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("https://web.whatsapp.com/")
pyautogui.press("enter")
time.sleep(7)

pyautogui.click(813,502)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.click(1206,583)
pyautogui.click(1050,499)
pyautogui.click(930,19)
pyautogui.write("https://bit.ly/447mUgA")
pyautogui.press("enter")
pyautogui.hotkey("ctrl" , "a")
pyautogui.hotkey("ctrl" , "c")
pyautogui.hotkey("ctrl" , "tab")
pyautogui.click(1136,651)
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")

for i in range (97):
    pyautogui.click(888,693)
    pyautogui.press("esc")
    pyautogui.press("Down")
    pyautogui.click(940,180,clicks=3)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(786,699)
    pyautogui.click(813,502)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    pyautogui.click(1206,583)
    pyautogui.click(1050,499)
    pyautogui.hotkey("ctrl" , "tab")
    pyautogui.hotkey("ctrl" , "c")
    pyautogui.hotkey("ctrl" , "tab")
    pyautogui.hotkey("ctrl" , "v")
    pyautogui.press("enter")

    time.sleep(2)












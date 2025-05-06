import pyautogui

x, y = pyautogui.position()  # Obtém a posição atual do mouse
print(f"Posição do mouse: ({x}, {y})")
pyautogui.sleep(10)
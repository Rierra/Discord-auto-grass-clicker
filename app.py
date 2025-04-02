import pyautogui
import keyboard
import time

# Wait 3 seconds so you can switch to the game window
time.sleep(3)

# Get the game window position
x, y = pyautogui.locateCenterOnScreen('grass_button.png', confidence=0.8)

print(f"Clicking at: {x}, {y}. Press 'q' to stop.")

# Clicking loop with ultra-fast clicks
while not keyboard.is_pressed('q'):
    pyautogui.click(x, y, clicks=2, interval=0.0005)  # Double click per loo



print("Script stopped!")
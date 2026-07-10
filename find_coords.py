import pyautogui
import time

print("Move your mouse to the target spot now.")
time.sleep(4)  # Gives you 4 seconds to hover your mouse over the game button

# Prints the precise numbers you need for the next script
print(f"\nYour coordinates are: {pyautogui.position()}")

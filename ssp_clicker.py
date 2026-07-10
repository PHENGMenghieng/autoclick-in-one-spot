import pyautogui
import time
import random
import keyboard

# ─── CONFIGURATION ───
# REPLACE THESE NUMBERS WITH WHAT FIND_COORDS.PY GIVES YOU:
# Your coordinates are: Point(x=1008, y=537)
X_COORD = 1008       
Y_COORD = 537       

print("Program starting in 5 seconds.")
print("Switch to your game window NOW.")
print("Hold the 'q' key down to STOP the clicker.")
time.sleep(5)

print("Clicker is running indefinitely.")
while True:
    # Check for emergency stop
    if keyboard.is_pressed('q'):
        print("\n Stopped by user successfully.")
        break

    # Force cursor to the exact spot and click
    pyautogui.click(x=X_COORD, y=Y_COORD)

    # Micro-randomized speed (0.2s to 0.3s)
    random_subtraction = random.uniform(0.00001, 0.10000)
    delay = 0.3 - random_subtraction
    
    time.sleep(delay)

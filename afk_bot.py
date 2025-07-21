# Simple AFK Gaming Bot in Python
# This script simulates mouse movements to prevent the computer from going idle.
# ----------------------------------------------------------------------------------------------------------------------------------
# Note: Ensure you have the 'pyautogui' library installed. You can install it using pip:
# pip install pyautogui
# --------------------------------------------------------------------------------------------------------------------------------
# Major Disclaimer:
# This script is intended for educational purposes and to help keep your computer active during long periods of inactivity.
# DO NOT use this in any malicious activity or to violate the terms of service of any games or applications.
# Use this script responsibly and ethically.
# --------------------------------------------------------------------------------------------------------------------------------
# Import necessary libraries
import pyautogui as pag
import random
import time

# Screen dimensions
screen_w, screen_h = pag.size()

# Option A: Fixed pixel margin
# margin_x = 100  
# margin_y = 100

# Option B: Percentage margin (uncomment to use)
margin_x = int(screen_w * 0.05)  # 5% of width
margin_y = int(screen_h * 0.05)  # 5% of height

# Ensure the mouse does not move too close to the edges of the screen
# This prevents accidental clicks on the taskbar or other UI elements.
# Adjust the margins as needed to fit your screen size and preferences.
min_x, max_x = margin_x, screen_w - margin_x
min_y, max_y = margin_y, screen_h - margin_y

# Initialize the move count
move_count = 0
print("🤖 AFK Bot is running. Press Ctrl+C to stop.")

try:
    while True:
        # Randomly move the mouse to a new position within the screen bounds
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        # x = random.randint(0, pag.size().width)
        # y = random.randint(0, pag.size().height)

        speed = random.uniform(0.3, 0.8)            # Random speed for mouse movement       (Realistic movement)
        pag.moveTo(x, y, speed)                     # Move the mouse to the new position

        move_count += 1                             # Increment the move count
        if move_count % 10 == 0:                    # Print status every 10 moves
            pag.press('shift')                      # Press the Shift key to simulate activity
            print("⚡ Shift pressed!")
        
        print(f"🖱️ Move #{move_count}: ({x}, {y})")

        sleep_time = random.uniform(1.5, 3.0)          # Random sleep time between moves
        time.sleep(sleep_time)
except KeyboardInterrupt:
    # Handle the Ctrl+C interrupt gracefully
    print("\n🤖 AFK Bot stopped. User pressed Ctrl+C. Exiting gracefully. Goodbye!")

# Handle any other exceptions that may occur
except Exception as e:
    print(f"⚠️ An error occurred: {e}. Exiting the bot.")

# End of the AFK Bot script
# --------------------------------------------------------------------------------------------------------------------------------
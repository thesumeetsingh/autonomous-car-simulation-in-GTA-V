import pyautogui
import time

def press_key(key, duration=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def move_car(lane_offset, vehicle_in_front):
    if vehicle_in_front:
        press_key("s")  # Slow down

    elif lane_offset < -50:
        press_key("a")  # Steer left

    elif lane_offset > 50:
        press_key("d")  # Steer right

    else:
        press_key("w")  # Move forward

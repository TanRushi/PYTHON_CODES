import pyautogui
import datetime

def screen_capture():
    now = datetime.datetime.now()
    image = pyautogui.screenshot()
    image.save(f"screenshot_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png")

screen_capture()
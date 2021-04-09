#! /bin/env python
from time import sleep
import pyautogui

sleep(3)
screenshot = pyautogui.screenshot()
screenshot.save('screen.png')

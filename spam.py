import time
import pyautogui as pya
from pynput.keyboard import Key, Controller

keyboard = Controller()

class Cordinate:
    emptyMessage = (356, 796)


def clicktoChat():
    pya.click(Cordinate.emptyMessage)


def typetoChat():
    pya.typewrite('!Hacked!')


def sendtoChat():
    keyboard.press(Key.enter)


i = 0
start_time = time.time()
while i < 1000:
    clicktoChat()
    typetoChat()
    time.sleep(0.013)
    sendtoChat()
    i += 1
    if i == 12:
        print("--- %s seconds ---" % (time.time() - start_time))

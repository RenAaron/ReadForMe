from pynput.mouse import Button, Controller
import keyboard
import time
import pyautogui
import pytesseract as pt
from PIL import Image
import win32gui
import win32api
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
coords = []
dc = win32gui.GetDC(0)
red = win32api.RGB(0, 119, 255)

mouse = Controller()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://readloud.net/english/american/30-child-s-boy-voice-justin.html")

#```````````````````````````````````````````````


def speak(text):
    search = driver.find_element("name", "but1")
    search.clear()
    search.send_keys(text)
    driver.find_element("name", "but").click()

hlOn = False

def highlightBox():
    for i in range(mouse.position[0]):
        win32gui.SetPixel(dc, i, coords[0][1], red)

    for i in range(mouse.position[1]):
        win32gui.SetPixel(dc, coords[0][0], i, red)

while 1:
    if(hlOn):
        highlightBox()
    if ((keyboard.is_pressed('`'))):
        if((len(coords) < 1)):
            coords.append(mouse.position)
            print(coords)
            hlOn = True
            time.sleep(1)

        else:
            hlOn = False
            coords.append(mouse.position)
            screenshot = pyautogui.screenshot(
            region=(coords[0][0], coords[0][1], coords[1][0] - coords[0][0], coords[1][1] - coords[0][1]))
            screenshot.save(r'img.png')
            img = Image.open(r'img.png')
            text = pt.image_to_string(img)
            print("Result: " + text)
            speak(text)
            coords.clear()
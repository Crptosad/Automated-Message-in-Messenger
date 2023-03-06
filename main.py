#automating message in messenger

import pyautogui as auto
import webbrowser
import schedule
from time import sleep

web = "link"

time = "20:50"

def automate():
    webbrowser.open(web)
    sleep(15)
    auto.click(440,712) #location of text box
    auto.typewrite("Good evening!!")
    auto.press('enter')
    sleep(5)
    auto.typewrite("magjowa kana!!!!")
    auto.press ('enter')

schedule.every().day.at(time).do(automate)

while True:
    schedule.run_pending()
    sleep(1)
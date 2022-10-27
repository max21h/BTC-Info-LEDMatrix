# py -2 btcInfo.py

# Web Scraping Prerequisites
import requests
# LED Matrix Prerequisites
import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
# JSON
import json
# SYS
import sys
#datetime
import datetime

disp = []
second = 0
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)
if len(sys.argv) > 1:
    device.contrast(int(sys.argv[1])) #set brightness

while(1):
    a = -1
    url = ""
    
    try:
        if(second != datetime.datetime.now().second):
            second = datetime.datetime.now().second
            disp = []
            if len(sys.argv) > 2:
                ##Read JSON from URL
                url = sys.argv[2]
                page = requests.get(url)
                y = page.json()

                if len(sys.argv) > 3: 
                    a = int(sys.argv[3])

                for key in y.keys():
                    disp.append("{}: {} ".format(key, y[key]))
            else:
                #Get BTCUSDT Price from Binance
                url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
                data = requests.get(url)  
                data = data.json()
                disp.append(f"{data['symbol']} {round(float(data['price']), 2)}")

            if url == "":
                disp.append("No URL given")
    except:
        disp = []
        disp.append("An exception occurred")

    disp = list(filter(lambda a:a != 0, disp)) #For some reason every odd element of the list 'disp' is '0'. This removes all occurences of '0' from the list 'disp'

    if(a >= 0):
        show_message(device, disp[a], fill="white", font=proportional(TINY_FONT),scroll_delay = 0.04) #Change the value of 'scroll_delay' to change the Scrolling Speed
    else:
        for i in range(len(disp)):
            show_message(device, disp[i], fill="white", font=proportional(TINY_FONT),scroll_delay = 0.04) #Change the value of 'scroll_delay' to change the Scrolling Speed

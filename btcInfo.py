# py -2 bcdisplay.py

# Web Scraping Prerequisites
import requests
# LED Matrix Prerequisites
import re
import time
import argparse
#from luma.led_matrix.device import max7219
#from luma.core.interface.serial import spi, noop
#from luma.core.render import canvas
#from luma.core.virtual import viewport
#from luma.core.legacy import text, show_message
#from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
#Json
import json
#Sys
import sys

while(1):

    disp = []
    a = -1

    if len(sys.argv) > 1:
        result = True
    else:
        result = False

    if result == False:
        disp.append("No URL given")
    else:
        page = requests.get(sys.argv[1])
        y = page.json()

        if len(sys.argv) > 2: 
            a = int(sys.argv[2])

        for key in y.keys():
            #if isinstance(y[key], dict) == False:
                disp.append("{}: {} ".format(key, y[key]))

    disp = list(filter(lambda a:a != 0, disp)) #For some reason every odd element of the list 'disp' is '0'. This removes all occurences of '0' from the list 'disp'
    #Remove 'list' in Python2.7

    #serial = spi(port=0, device=0, gpio=noop())
    #device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)
    #device.contrast(int(sys.argv[3])) #set brightness

    #Console Output
    #for i in range(len(disp)):
    #print(disp[a])

    if(a >= 0):
       print(disp[a])
    else:
       for i in range(len(disp)):
            print(disp[i])

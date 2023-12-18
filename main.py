#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import time
import traceback
import datetime
from PIL import Image,ImageDraw,ImageFont

import lib.initEPD7in5 as epd7in5b_V2
from lib.API_nook import villager_bday, pp, fromJSONgetName, getThumbnail, api_key, getNumOfBdays, getAPI_data
from lib.imgConvertor import addBorder, rmTransparency, printBlackBMP, rmOldImgs, convertIMG

#OS PATH to image directory
dir_img = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')

#OS PATH to font directory
dir_font = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts')


newIconSize = (250, 250)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5b_V2 Demo")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()


    font48 = ImageFont.truetype(os.path.join(dir_font, 'FinkHeavy.ttf'), 48)
    font72 = ImageFont.truetype(os.path.join(dir_font, 'FinkHeavy.ttf'), 72)

    #logging.info("Displaying day, month and date with thumbnail")


#################################### A P I #####################################################

# This is secret and you must get your own API key from the Nookipedia devs
    api_key = os.environ["SECRET_NOOKIPEDIA_API_KEY"]

# This will get the directory path of img/
    dir_img = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')
# This will list all the items in the img/ (AKA it will list all the files)
    listdir_images = os.listdir(dir_img)

# Gets the current date and time
    date = datetime.datetime.now()
# Month
    currMonth = date.strftime("%B")
# Date
    currDate = date.strftime("%-d")


# Starts the API session
    villager_bday = villager_bday(api_key)

# This calls the getCurrCharAll func in villager_bday class
# It will give the character who's birthday it is today
    parse_json_data = villager_bday.getCurrCharAll(currMonth, currDate, 'true')

# Example of a day (2 characters)

# This will give me the data I want for a given day
#parse_json_data = villager_bday.getCurrCharAll('December', '5', 'true')
# This prints the data to screen, or pass it to a text file to read easily
    pp(parse_json_data)

# This will return a list of names for a day
    names = []
    names = fromJSONgetName(parse_json_data)
    print(names)

# This will obtain the new image file.
    getThumbnail(parse_json_data)


############################## CONVERTING IMG TO BMP ##############################################


# Allow 3 seconds to download image(s)
    time.sleep(3)

    
    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            icon_file_path = os.path.join(dir_img, item)
            break   
    print(item)

# Sets the blank canvas file's path to be opened
    empty_canvas_file = os.path.join(dir_img, 'NULL_COLOUR.png')

# Opens the the blank canvas as background
    background = Image.open(empty_canvas_file)
    icon_open = Image.open(icon_file_path)     # Opens a iteration for RED of icon from API

# Resize and convert the obj for BLK to the correct dimensions
    icon_BLK = icon_open.resize(newIconSize)
    icon_BLK = icon_BLK.convert("RGBA")

# This gets the RGBA data from the actual image and put its in the obj
    img_blk_data = icon_BLK.getdata()


# This sets the outfile location, name and type
    outFile_BLK = os.path.join(dir_img, 'black_thumbnail.bmp')



    printBlackBMP(rmTransparency(addBorder(img_blk_data)), icon_BLK, background, outFile_BLK)



# This will remove the first file it sees with 'img_'
    rmOldImgs(dir_img)    



####################################### PRINTING TO DISPLAY ###################
    
    background_w_thumbnail_blk = Image.open(os.path.join(dir_img, 'black_thumbnail.bmp'))
    canvas_red = Image.open(os.path.join(dir_img, 'NULL_COLOUR.bmp'))

# Canvases w/ thumbnail and blank
    draw_blk = ImageDraw.Draw(background_w_thumbnail_blk)
    draw_red = ImageDraw.Draw(canvas_red)

# Day and Date
    draw_blk.text((10, 90), date.strftime("%B %-d"), font=font48, fill=0)
    draw_red.text((10, 10), date.strftime("%A"), font = font72, fill = 0)

# Middle bar (vertical line)
    draw_blk.rectangle([(380,0),(400,480)], fill="black", outline=None, width=1)

# Calendar bar (tpo right corner all red)
    draw_red.rectangle([(400,0),(800,100)], fill="black", outline=None, width=1)
    draw_red.text((500,50), "CALENDAR", font=font48, fill="white")


# Output to EPD
    epd.display(epd.getbuffer(background_w_thumbnail_blk), epd.getbuffer(canvas_red))


    time.sleep(5)
   



# This will clear after the script is run
    #logging.info("Clear...")
    #epd.init()
    #epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()


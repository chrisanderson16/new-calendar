#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import lib.initEPD7in5 as epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

#import lib.API_nook as nookAPI
from lib.API_nook import villager_bday, pp, fromJSONgetName, getThumbnail, api_key, getNumOfBdays, getAPI_data
#import lib.imgConvertor as convertor 
from lib.imgConvertor import addBorder, rmTransparency, printBlackBMP, rmOldImgs, convertIMG

#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')
#fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
fontdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts')
#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
#if os.path.exists(libdir):
#    sys.path.append(libdir)


# This will get the directory path of img/
dir_img = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
# This will get the directory path of lib/
dir_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

newIconSize = (250, 250)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

import datetime


date = datetime.datetime.now()

logging.basicConfig(level=logging.DEBUG)

##########################################################################################################################################
##########################################################################################################################################
######
######      "need to do with this code" list:
######              - This will be my main.py
######              - I will call the color_test.py to convert x-number of .png files to be converted, the file_n_color_convert.py
######                should purely change the files to:
######                           red_[char name].bmp
######                         black_[char name].bmp
######              - 
######              - 
######              - 
##########################################################################################################################################
########################################################################################################################################## 



try:
    logging.info("epd7in5b_V2 Demo")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()


    font48 = ImageFont.truetype(os.path.join(fontdir, 'FinkHeavy.ttf'), 48)
    font72 = ImageFont.truetype(os.path.join(fontdir, 'FinkHeavy.ttf'), 72)

    logging.info("Displaying day, month and date with thumbnail")

    getAPI_data()

    

    convertIMG()

    time.sleep(4)

    background_w_thumbnail_blk = Image.open(os.path.join(picdir, 'black_thumbnail.bmp'))
    canvas_red = Image.open(os.path.join(picdir, 'NULL_COLOUR.bmp'))

    draw_blk = ImageDraw.Draw(background_w_thumbnail_blk)
    draw_red = ImageDraw.Draw(canvas_red)

    draw_blk.text((10, 90), date.strftime("%B %-d"), font=font48, fill=0)
    draw_red.text((10, 10), date.strftime("%A"), font = font72, fill = 0)

    #background_w_thumbnail_blk.save(os.path.join(picdir, 'final.bmp'))
    
    #img = Image.open(os.path.join(picdir, 'final.bmp'))
    #draw_img = ImageDraw.Draw(img)

    #epd.display(epd.getbuffer(img), epd.getbuffer(background_w_thumbnail_red))
    epd.display(epd.getbuffer(background_w_thumbnail_blk), epd.getbuffer(canvas_red))


    time.sleep(5)





#    logging.info("Clear...")
#    epd.init()
#    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()


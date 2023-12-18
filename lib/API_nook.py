#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests
from requests import Session
from pprint import pprint as pp
import datetime
import shutil
import numpy as np
import os
#from glob import glob
import re
import logging

import time

dir_img = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

api_key = os.environ["SECRET_NOOKIPEDIA_API_KEY"]


class villager_bday:
    def __init__(self, token):
            self.apiurl = 'https://api.nookipedia.com'
            self.headers = {
                'X-API-KEY' : token,
                'AcceptVersion' : '1.0.0'
            }
            self.session = Session()
            self.session.headers.update(self.headers)
            
    def getCurrCharAll(self, month, date, icon_bool):
          url = self.apiurl + '/villagers'
          parameters = {'birthmonth': month,
                        'birthday': date,
                        'nhdetails': icon_bool}
          response = self.session.get(url, params=parameters)
          data = response.text
          parse_json = json.loads(data)
          return parse_json



# Determines how many bdays are on a given day
def getNumOfBdays(data):
    return np.size(data)



# This will print the names of the character(s) who's bday it is a given day
def fromJSONgetName(data):
     iteration = getNumOfBdays(data)
     names = []

     if(iteration >= 1):
         for i in range(0,iteration):
             names.append(data[i]['name'])
             i = i+1
         return names
     else:
         logging.info("Error getting # of birthdays/r/n")

     

# This will download the character(s) who's bday it is a given day
def getThumbnail(json_data):
    names = []
    names = fromJSONgetName(json_data)

    # This will delete all the "old" files in img/
    for item in dir_img:
         if item.startswith('img_'):
              os.remove(os.path.join(dir_img, item))

    iteration = getNumOfBdays(json_data)

    if(iteration >= 1):
         for i in range(0,iteration):
            char_thumbnail_url = json_data[i]['nh_details']['icon_url']
            response2 = requests.get(char_thumbnail_url, stream=True)
            with open(os.path.join(dir_img, 'img_'+names[i]+'.png'), 'wb') as out_file:
                shutil.copyfileobj(response2.raw, out_file)
            del response2
            i = i+1
    else:
        logging.info("Error getting # of birthdays/r/n")





def getAPI_data():


# Gets the current date and time
    date = datetime.datetime.now()
# Month
    currMonth = date.strftime("%B")
# Date
    currDate = date.strftime("%-d")


# Starts the API session
    villagers = villager_bday(api_key)

# This calls the getCurrCharAll func in villager_bday class
# It will give the character who's birthday it is today
    parse_json_data = villagers.getCurrCharAll(currMonth, currDate, 'true')

# Example of a day (2 characters)

# This will give me the data I want for a given day
#parse_json_data = villager_bday.getCurrCharAll('December', '8', 'true')
# This prints the data to screen, or pass it to a text file to read easily
    pp(parse_json_data)

# This will return a list of names for a day
    names = []
    names = fromJSONgetName(parse_json_data)
    print(names)

# This will obtain the new image file.
    getThumbnail(parse_json_data)
    time.sleep(5)
    print("waiting 5 seconds")





if __name__ == '__main__':

# This is secret and you must get your own API key from the Nookipedia devs
    api_key = os.environ["SECRET_NOOKIPEDIA_API_KEY"]

# This will get the directory path of img/
    dir_img = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
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
#    parse_json_data = villager_bday.getCurrCharAll(currMonth, currDate, 'true')

# Example of a day (2 characters)

# This will give me the data I want for a given day
    parse_json_data = villager_bday.getCurrCharAll('December', '8', 'true')
# This prints the data to screen, or pass it to a text file to read easily
    pp(parse_json_data)

# This will return a list of names for a day
    names = []
    names = fromJSONgetName(parse_json_data)
    print(names)

# This will obtain the new image file.
    getThumbnail(parse_json_data)


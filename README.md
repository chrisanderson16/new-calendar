## Animal Crossing ePaper Display Calendar
This is a self project that I am making for my girlfriend. Much of the pre-existing code is free to use from Waveshare for their ePaper displays they sell. It is open-source and free to use without a license. <br />
## Current progress
At the moment, this simply is a collection of different scripts. As I am currently still a computer engineering student, I haven't yet had the time to put it all together.<br />

## Main library test scripts
# API_Handler.py , driverConfig.py , initEPD7in5.py , myCustomEPD.py
These scripts are working libraries that just require the clean up to actually work as completed libraries, otherwise they are "done"<br />

## Working test scripts
The main working scripts utilize the Nookipedia API to obtain the birthdates of different animal crossing characters, their names, and their thumbnail pictures. 
This is done with the **API_nookipedia.py**. The **color_test.py** takes the .png files from the wiki, and will then convert them into the black and red contrasts (This is b/c the display does b/w/r).
The **main.py** ties these together by using the current date from the **API_nookipedia_test.py** to display it onto the connected ePaper display. <br />

## All Current Script functions
**API_Handler.py**
This is a library script that simple allows for retrieval of birthdays, images and name from the nookipedia API wiki.<br /><br />
**API_nookipedia_test.py**
This is a test script that will actually collect the information from the API, rather than just providing the defintions and classes to do so. <br /><br />
**API_nookipedia.py**
This is the exact same as *API_Handler.py*<br /><br />
**color_test.py**
This is the most polished of the scripts with comments. It runs the *API_nookipedia_test.py* script and then will take the .png file from the API. It then resizes the image to be visible on the EPD. It also will split the black and red images apart. It then saves the files. <br /><br />
**driverConfig.py**
This is untouched code from Waveshare that is licensed to be used however and wherever without restraints.<br /><br />
**initEPD7in5.py**
This is untouched code from Waveshare that is licensed to be used however and wherever without restraints.<br /><br />
**main.py**
Current main python script that uses the *driverConfig.py*, *initEPD7in5.py*, *color_test.py*, and *API_nookipedia_test.py*. When running this is will go through the initialization steps, to clear any image "burned" onto the EPD. It will then use the API to get an image, then uses *color_test.py* to split the image into red and black, finally displaying it onto the EPD. <br /><br />
**myCustomEPD-02.py**
This currently acts as a test to see how text is displayed on the screen.<br /><br />
**myCustomEPD.py**
Mainly an experiment to upload the .bmp files directly to the EPD without adjusting anything. Simply, it uploads a given image without doing anything else. <br /><br />
**myPNG-to-BMP.py**
Propriatery script. Needs to be removed at some point. Used to learn how converting png to bmp worked. <br /><br />
**osPathTesting.py**
A simple test to understand how *os.path.join* and other os functions and classes worked. <br /><br />
**png-to-bmp.py**
Essentially a more clear cut version of *color_test.py*, however, it needs to be updated. <br /><br />
**text.txt**
Used to pipe the printouts to be examined when needed. Later on needs to be integrated as an actual log system rather than just > text.txt.<br /> <br />

**text-n-img-EPD.py**
This script is being used to test how to "draw" on images. <br/><br/>

Main.py -> color_test.py -> API_nookipedia_test.py <br/>
   ^-- driverConfig.py <- initEPD7in5.py
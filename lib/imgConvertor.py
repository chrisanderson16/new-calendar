from PIL import Image, ImageDraw, ImageFilter
import os
import time



# These are useful definitions
newIconSize = (250, 250)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)



# Here we will create a function to run the API_nookipedia_test.py
def runAPI(file_path):
    try:
        os.system(f'python3 {os.path.join(file_path)}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.\r\n")



# This will create a border around the image
def addBorder(data):
    newData = []                # Temp data storage to hold image obj
    prevAlphaVAL = 0            # Check previous opacity

    for item in data:
        if(prevAlphaVAL != item[3]):
            newData.append(BLACK)
        else:
            newData.append(item)
        prevAlphaVAL = item[3]
    return newData


# This will removed the transparency and replace it with a solid white
def rmTransparency(data):
    newData = []
    for item in data:
        if item[3] == 0:
            newData.append((255, 255, 255, 255))
        else:
            newData.append(item)
    return newData

# Print Black BMP
def printBlackBMP(data, icon_BLK, background, outFile_BLK):

    newData = []
    
    for item in data:
        #if (item[0] < 100 and item[1] < 100 and item[2] < 100):
        #    newData.append(BLACK)
        #elif (item[0] < 128 and item[1] > 30 and item[2] > 30):
            newData.append(item)
        #else:
        #    newData.append(WHITE)

    icon_BLK.putdata(newData)

    B_Image = background.copy()
    B_Image.paste(icon_BLK, (20, 230))
    B_Image.save(outFile_BLK, quality=95)


def rmOldImgs(dir_img):
    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            os.remove(os.path.join(dir_img, item))
            break

def char_thumbnail(numOfBDays, dir_img):
    
    i = 0
    
    icon_file_path = []

    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            icon_file_path[i] = os.path.join(dir_img, item)
            i += 1
                
    print(icon_file_path)


    return icon_file_path


def convertIMG(dir_img):
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



    printBlackBMP(rmTransparency(addBorder(img_blk_data)))




# This will remove the first file it sees with 'img_'
    #rmOldImgs()    


if __name__ == '__main__':


# This will get the directory path of img/
    dir_img = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
# This will get the directory path of lib/
    dir_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')


# This function call will run the python script, therefore, if we want for main, we can use this for all
    runAPI('API_nook.py')


# Allow 3 seconds to download image(s)
    #time.sleep(3)

# Sets icon_file's path to be opened
    # This will open the first file it sees with 'img_'
    #for item in os.listdir(dir_img):
    #    if item.startswith('img_'):
    #        icon_file_path = os.path.join(dir_img, item)
    #        break   
    #print(item)

# Sets the blank canvas file's path to be opened
    #empty_canvas_file = os.path.join(dir_img, 'NULL_COLOUR.png')

# Opens the the blank canvas as background
    #background = Image.open(empty_canvas_file)
    #icon_open = Image.open(icon_file_path)     # Opens a iteration for RED of icon from API

# Resize and convert the obj for BLK to the correct dimensions
    #icon_BLK = icon_open.resize(newIconSize)
    #icon_BLK = icon_BLK.convert("RGBA")

# This gets the RGBA data from the actual image and put its in the obj
    #img_blk_data = icon_BLK.getdata()


# This sets the outfile location, name and type
    #outFile_BLK = os.path.join(dir_img, 'black_thumbnail.bmp')



    #b = printBlackBMP(rmTransparency(addBorder(img_blk_data)))

    char_thumbnail(2, dir_img)


# This will remove the first file it sees with 'img_'
    #rmOldImgs()    

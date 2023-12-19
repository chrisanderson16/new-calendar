from PIL import Image, ImageDraw, ImageFilter
import os
import time



# These are useful definitions
newIconSize = (250, 250)
smallerIcon = (150,150)
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
def printBlackBMP(data, icon_BLK):

    newData = []
    
    for item in data:
        #if (item[0] < 100 and item[1] < 100 and item[2] < 100):
        #    newData.append(BLACK)
        #elif (item[0] < 128 and item[1] > 30 and item[2] > 30):
            newData.append(item)
        #else:
        #    newData.append(WHITE)

    icon_BLK.putdata(newData)

    #B_Image = background.copy()
    #B_Image.paste(icon_BLK, (20, 230))
    #B_Image.save(outFile_BLK, quality=95)

    return icon_BLK

def rmOldImgs(dir_img):
    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            os.remove(os.path.join(dir_img, item))
        if item.startswith('tmp'):
            os.remove(os.path.join(dir_img, item))


def convert_char_thumbnails(dir_img):
    
    IconSize = (250, 250)

    i = 1
    
    icon_files = list()

    for item in os.listdir(dir_img):
        if item.startswith('img_'):
            icon_file_path = os.path.join(dir_img, item)
            icon_files.append(icon_file_path)
            i += 1
    icon_files.sort()
    print(icon_files)

    if len(icon_files) > 1:
        print("OMG more than 1 bday today")
        
        empty_canvas_file = os.path.join(dir_img, 'NULL_COLOUR.png')

# Opens the the blank canvas as background
        background = Image.open(empty_canvas_file)


# This gets the RGBA data from the actual image and put its in the obj
        

        new_icon_1 = Image.new('RGBA', smallerIcon, WHITE)
        new_icon_2 = Image.new('RGBA', smallerIcon, WHITE)



        icon_open1 = Image.open(icon_files[0])    
        icon_open2 = Image.open(icon_files[1])    
            
# Resize and convert the obj for BLK to the correct dimensions
        icon_BLK1 = icon_open1.resize(smallerIcon)
        icon_BLK1 = icon_BLK1.convert("RGBA")
            
        icon_BLK2 = icon_open2.resize(smallerIcon)
        icon_BLK2 = icon_BLK2.convert("RGBA")

        img_blk_data1 = icon_BLK1.getdata()
        img_blk_data2 = icon_BLK2.getdata()
        #out = printBlackBMP(rmTransparency(addBorder(img_blk_data)), icon_BLK)
        
        new_icon_1.putdata(rmTransparency(addBorder(img_blk_data1)))
        new_icon_2.putdata(rmTransparency(addBorder(img_blk_data2)))

        new_icon_1.save(os.path.join(dir_img, 'tmp1.bmp'))
        new_icon_2.save(os.path.join(dir_img, 'tmp2.bmp'))


        time.sleep(2)

        new_thumb_path_1 = os.path.join(dir_img, 'tmp1.bmp')
        new_thumb_path_2 = os.path.join(dir_img, 'tmp2.bmp')

        new_thumb_1 = Image.open(new_thumb_path_1)
        new_thumb_2 = Image.open(new_thumb_path_2)

        blank_im = background.copy()
        blank_im.paste(new_thumb_1, (10,230), mask=None)
        blank_im.paste(new_thumb_2, (215,230), mask=None)

        blank_im.save(os.path.join(dir_img, 'thumbnail.bmp'))
        #rmOldImgs(dir_img)  
        return 2
    else:
        print("Normal operations")


        icon_open = Image.open(icon_file_path)     # Opens a iteration for RED of icon from API
        empty_canvas_file = os.path.join(dir_img, 'NULL_COLOUR.png')

# Opens the the blank canvas as background
        background = Image.open(empty_canvas_file)
# Resize and convert the obj for BLK to the correct dimensions
        icon_BLK = icon_open.resize(IconSize)
        icon_BLK = icon_BLK.convert("RGBA")

# This gets the RGBA data from the actual image and put its in the obj
        img_blk_data = icon_BLK.getdata()

        new_icon = Image.new('RGBA', (250,250), WHITE)


        #out = printBlackBMP(rmTransparency(addBorder(img_blk_data)), icon_BLK)
        
        new_icon.putdata(rmTransparency(addBorder(img_blk_data)))
        new_icon.save(os.path.join(dir_img, 'tmp.bmp'))

        thumb = Image.open(os.path.join(dir_img, 'tmp.bmp'))

        blank_im_one = background.copy()
        blank_im_one.paste(thumb, (55, 180), mask=None)

        blank_im_one.save(os.path.join(dir_img, 'thumbnail.bmp'))

        #rmOldImgs(dir_img)  
        return 1



########################################### MAIN FUNCTION #############################################################

if __name__ == '__main__':


# This will get the directory path of img/
    dir_img = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
# This will get the directory path of lib/
    dir_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

    rmOldImgs(dir_img) 
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

    convert_char_thumbnails(dir_img)


      
# This will remove the first file it sees with 'img_'
    #rmOldImgs()    

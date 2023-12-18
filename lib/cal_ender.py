from PIL import Image, ImageDraw, ImageFont, ImageChops


def calendar_icon():

    h, w = 50, 50

    img = Image.new('1', (h,w), 1)

    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([(5,5),(45,45)], radius=5, fill=None, outline='black', width=3, corners=None)
    draw.line([(5,15),(45,15)], fill='black', width=2, joint=None)

    s_h1, s_w1, s_h2, s_w2 = 0, 0, 5, 5

    #draw.rectangle([(s_h1+10,s_w1+19),(s_h2+10,s_w2+19)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+18,s_w1+19),(s_h2+18,s_w2+19)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+26,s_w1+19),(s_h2+26,s_w2+19)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+34,s_w1+19),(s_h2+34,s_w2+19)], fill='black', outline=None,width=1)

    draw.rectangle([(s_h1+10,s_w1+27),(s_h2+10,s_w2+27)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+18,s_w1+27),(s_h2+18,s_w2+27)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+26,s_w1+27),(s_h2+26,s_w2+27)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+34,s_w1+27),(s_h2+34,s_w2+27)], fill='black', outline=None,width=1)

    draw.rectangle([(s_h1+10,s_w1+35),(s_h2+10,s_w2+35)], fill='black', outline=None,width=1)
    draw.rectangle([(s_h1+18,s_w1+35),(s_h2+18,s_w2+35)], fill='black', outline=None,width=1)
    #draw.rectangle([(s_h1+26,s_w1+35),(s_h2+26,s_w2+35)], fill='black', outline=None,width=1)
    #draw.rectangle([(s_h1+34,s_w1+35),(s_h2+34,s_w2+35)], fill='black', outline=None,width=1)

    img = img.convert('L')
    img = ImageChops.invert(img)
    img = img.convert('1')



    #img.show()
    return img



"""import datetime
import time
from datetime import date
from calendar import monthrange 

import calendar

w, h = 480, 800

img = Image.new("RGB",(w,h), (255,255,255))
draw = ImageDraw.Draw(img)

boarder = 9
h_start= int(h/2)
h_end = int(h-boarder)
w_start = boarder
w_end = w-boarder
stepsizeV = int((w-2*boarder)/7)
stepsizeH = int((h_start-boarder)/5)

#draw.rectangle((10,h_start,w-10,h_end),outline=1,width=5,)
cols=[]
rows=[]
days = { 0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}
i=0
for x in range (boarder,w,stepsizeV):
    line = ((x,h_start),(x,h_end))
    draw.line(line,fill=1,width=3)
    cols.append(x+stepsizeV/2)
    if i<7:
        draw.text((x+stepsizeV/2 -10, h_start-stepsizeV/2), days[i], fill=(0,0,0))
        i+=1

for x in range (h_start,h,stepsizeH):
    line = ((w_start,x),(w_end,x))
    draw.line(line,fill=50, width=3)
    rows.append(x+stepsizeH/2)

Curdate = date.today() 
date =int(Curdate.strftime('%d'))
month = int(Curdate.strftime('%m'))
year = int(Curdate.strftime('%y'))

monthlen = calendar.monthrange(year,month)

k = monthlen[0] + 1
i=1
j=0
r = rows[j]
while i<= monthlen[1]:
    c = cols[k]
    draw.text((c,r), str(i), fill=(0,0,0))
    i+=1
    k = (k+1)%7
    if not k:
        j+=1
        r = rows[j]
img.show()
"""
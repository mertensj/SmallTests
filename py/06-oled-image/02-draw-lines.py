#! /usr/bin/python2

from PIL import Image
from PIL import ImageDraw

im1=Image.new("1",(64,64),"white")

#im.show()
#im.save("white.xbm")

draw=ImageDraw.Draw(im1)
#draw.line(((4,4),(60,4),(60,60),(4,60),(4,4)))
draw.line(((4,4),(30,4)))
draw.line(((4,30),(30,30)))
#for y in range(4,60,2):
#	draw.line(((4,y),(30,y)))
im1.show()
#im1.save("./images/white4.xbm")

#im2 = Image.open("./images/arch.png")
#im3 = Image.merge((im1, im2))
#im3.show()


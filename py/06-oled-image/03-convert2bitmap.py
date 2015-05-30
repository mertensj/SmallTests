#! /usr/bin/python2
# -------------------------------------------
# 1. Read any image format supported by PIL
# 2. Resize to 64x64 to fit on OLED
# 3. Convert to bitmap
# 4. Flip image
# 5. Rotate 90 degrees 
# 6. Invert image , looks better on OLED
# 7. Convert to 1 and 0 values
# 8. Convert to format readible by Arduino 
#    = to be included as a C-format bit string
# -------------------------------------------

import sys
from PIL import Image
#from PIL import ImageDraw

im = Image.open("./images/arch.png")
#im = Image.open("./images/jan.jpg")

#im.show()

print(im.size,im.mode)
im=im.resize((64,64))
bm = im.convert("1")
print(bm.size,bm.mode)
#bm.show()

bm = bm.transpose(Image.FLIP_LEFT_RIGHT)
bm = bm.rotate(90)
bm = bm.point(lambda i: 255-i) # invert image
bm = bm.point(lambda i: i/255) # convert 255 to 1

pix = bm.load()
line = ""
for x in range(64):
        y=0
	for byte in range(8):
		line += "B"
		for bit in range(8):
			line += str(pix[x,y])
			y += 1
		line += ", "
	print(line)
        line = ""

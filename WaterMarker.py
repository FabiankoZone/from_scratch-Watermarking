#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('Cat03.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "Amachay"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text,fill="black", font=font)
im.show()

#Save watermarked image
im.save('watermark.jpg')
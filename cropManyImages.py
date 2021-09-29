# Importing Image class from PIL module
import PIL
import os
import os.path
from PIL import Image

# The crop method from the Image module takes four coordinates as input.
    # The right can also be represented as (left+width)
    # and lower can be represented as (upper+height).
    # TOP LEFT IS 0,0
    # BOTTOM RIGHT IS THE IMG DIMENSIONS
(left, upper, right, lower) = (500, 500, 1300, 1300)



def cropImage(img):
    img = img.crop((left, upper, right, lower))
    return img


 
 
f = r'c://Users/Owner/Desktop/imagetest'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)


    # Cropping
    img = cropImage(img)
    img.save(f_img)



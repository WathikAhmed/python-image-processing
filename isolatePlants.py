import os
import os.path
from PIL import Image
import numpy as np
import argparse
import cv2
import hashlib
import random

#Del this file soon

def getGreen(img):
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "./source/513108.jpg")
    args = vars(ap.parse_args())
    # load the image
    image = cv2.imread(img)


    # define the list of boundaries
    boundaries = [
        ([0, 102, 0], [221, 255, 204])
    ]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)
        
        # Image directory
        directory = r'c://Users/Owner/Desktop/results'
        os.chdir(directory)

        # Filename
        mystring = img + str(random.randint(0,900))
        # Assumes the default UTF-8
        hash_object = hashlib.md5(mystring.encode())
        filename = str(hash_object.hexdigest()) + ".jpg"
        
        # Saving the image
        cv2.imwrite(filename, output)

 

 
f = r'c://Users/Owner/Desktop/imagetest'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    print(f_img)
    getGreen(f_img)



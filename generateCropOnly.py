# The function of this python script is to generate cropped images as output.
import PIL
import os
import os.path
import cv2 
from PIL import Image
import sys
import numpy as np

# Assumes images are in 1944x2592 dimensions and in .jpg format
sourceFolder = "./source"
sourceFolderCropped = "xxx"
currentDir="xxx"



def cropTopLeft():
    (left, upper, right, lower) = (0, 0, 1024, 1024)
    
    for file in os.listdir(sourceFolder):
        f_img = sourceFolder+"/"+file
        img = Image.open(f_img)
        # Cropping
        img = img.crop((left, upper, right, lower))
        # You should change 'test' to your preferred folder.
        MYDIR = ("sourceFolderCropped")
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        # You should change 'test' to your preferred folder.
        MYDIR2 = ("Final")
        CHECK_FOLDER = os.path.isdir(MYDIR2)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR2)
            print("created folder : ", MYDIR2)
        
        newDir = os.path.join(os.getcwd(), MYDIR)
        global sourceFolderCropped
        global currentDir
        sourceFolderCropped = newDir
        currentDir = os.path.join(os.getcwd(), "Final")

        file = "cropTopLeft" + file
        destination = os.path.join(os.getcwd(), MYDIR, file)
        destination2 = os.path.join(currentDir, file)
        #print(destination)
        img.save(destination)
        img.save(destination2)

def cropBottomLeft():
    (left, upper, right, lower) = (0, 1568, 1024, 2592)
  
    for file in os.listdir(sourceFolder):
        f_img = sourceFolder+"/"+file
        img = Image.open(f_img)
        # Cropping
        img = img.crop((left, upper, right, lower))
        # You should change 'test' to your preferred folder.
        MYDIR = ("sourceFolderCropped")
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        newDir = os.path.join(os.getcwd(), MYDIR)
        global sourceFolderCropped 
        sourceFolderCropped = newDir
        #print(sourceFolderCropped)

        file = "cropBottomLeft" + file
        destination = os.path.join(os.getcwd(), MYDIR, file)
        #print(destination)
        destination2 = os.path.join(currentDir, file)
        #print(destination)
        img.save(destination)
        img.save(destination2)








cropTopLeft()
cropBottomLeft()
print("Done!")





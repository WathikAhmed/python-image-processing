# Importing Image class from PIL module
import PIL
import os
import os.path
import cv2 
from PIL import Image
import asyncio
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



def detectGreen(readDirr):
  
    for file in os.listdir(readDirr):
        f_img = readDirr+"/"+file
        MYDIR = ("detectGreen" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "detectGreen" + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
        destination2 = os.path.join(currentDir, fileName)
        #print("---------------------"+f_img)

        ## Read
        img = cv2.imread(f_img)
        #cv2.imshow('img', img)

        ## convert to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        ## mask of green (36,0,0) ~ (70, 255,255)
        mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))

        ## mask o yellow (15,0,0) ~ (36, 255, 255)
        mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))

        ## final mask and masked
        #mask = cv2.bitwise_or(mask1, mask2)
        target = cv2.bitwise_and(img,img, mask=mask1)

        #cv2.imwrite("target.png", target)
        #cv2.imshow('final', target)
        #cv2.waitKey(0)
        cv2.imwrite(destination, target)
        cv2.imwrite(destination2, target)

def increaseGreen(readDirr):
  
    for file in os.listdir(readDirr):
        f_img = readDirr+"/"+file
        MYDIR = ("increaseGreen" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "increaseGreen"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
        destination2 = os.path.join(currentDir, fileName)
        #print("---------------------"+f_img)

        #-----Reading the image-----------------------------------------------------
        img = cv2.imread(f_img)
        #cv2.imshow("img",img) 

        #-----converted the values to float32 during BGR2HSV transformation to avoid negative values during saturation transformation to due uint8 (default) overflow----------------------------------- 
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype("float32")
        #cv2.imshow("lab",lab)

        #-----splitting hsv values, adjusting the individual channels and then doing a merge-------------------------
        (r, g, b) = cv2.split(imgrgb)
        #cv2.imshow('r_channel', r)
        #cv2.imshow('g_channel', g)
        #cv2.imshow('b_channel', b)
        g = g*1.5
        g = np.clip(g,0,255)
        imgrgb = cv2.merge([r,g,b])

        #-----converted it back to default uint8 after my hue adjustment--------------------
        imgbgr = cv2.cvtColor(imgrgb.astype("uint8"), cv2.COLOR_RGB2BGR)
        #cv2.imshow('final', imgbgr)
        #cv2.waitKey(0)
        cv2.imwrite(destination, imgbgr)
        cv2.imwrite(destination2, imgbgr)

        #_____END_____#

def hue(readDirr):
  
    for file in os.listdir(readDirr):
        f_img = readDirr+"/"+file
        MYDIR = ("hue" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "hue"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
        destination2 = os.path.join(currentDir, fileName)

        #print("---------------------"+f_img)

        #-----Reading the image-----------------------------------------------------
        img = cv2.imread(f_img)
        #cv2.imshow("img",img) 

        #-----converted the values to float32 during BGR2HSV transformation to avoid negative values during saturation transformation to due uint8 (default) overflow----------------------------------- 
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
        #cv2.imshow("lab",lab)

        #-----splitting hsv values, adjusting the individual channels and then doing a merge-------------------------
        (h, s, v) = cv2.split(imghsv)
        h = h*2
        h = np.clip(h,0,255)
        imghsv = cv2.merge([h,s,v])

        #-----converted it back to default uint8 after my hue adjustment--------------------
        imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
        #cv2.imshow('final', imgrgb)
        #cv2.waitKey(0)
        cv2.imwrite(destination, imgrgb)
        cv2.imwrite(destination2, imgrgb)


        #_____END_____#

def saturation(readDirr):
  
    for file in os.listdir(readDirr):
        f_img = readDirr+"/"+file
        MYDIR = ("saturation" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "saturation"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
        destination2 = os.path.join(currentDir, fileName)
        #print("---------------------"+f_img)

        #-----Reading the image-----------------------------------------------------
        img = cv2.imread(f_img)
        #cv2.imshow("img",img) 

        #-----converted the values to float32 during BGR2HSV transformation to avoid negative values during saturation transformation to due uint8 (default) overflow----------------------------------- 
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
        #cv2.imshow("lab",lab)

        #-----splitting hsv values, adjusting the individual channels and then doing a merge-------------------------
        (h, s, v) = cv2.split(imghsv)
        s = s*2
        s = np.clip(s,0,255)
        imghsv = cv2.merge([h,s,v])

        #-----converted it back to default uint8 after my saturation adjustment--------------------
        imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
        #cv2.imshow('final', imgrgb)
        #cv2.waitKey(0)
        cv2.imwrite(destination, imgrgb)
        cv2.imwrite(destination2, imgrgb)

        #_____END_____#

def value(readDirr):
  
    for file in os.listdir(readDirr):
        f_img = readDirr+"/"+file
        MYDIR = ("saturation" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "saturation"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
        destination2 = os.path.join(currentDir, fileName)
        #print("---------------------"+f_img)

        #-----Reading the image-----------------------------------------------------
        img = cv2.imread(f_img)
        #cv2.imshow("img",img) 

        #-----converted the values to float32 during BGR2HSV transformation to avoid negative values during saturation transformation to due uint8 (default) overflow----------------------------------- 
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
        #cv2.imshow("lab",lab)

        #-----splitting hsv values, adjusting the individual channels and then doing a merge-------------------------
        (h, s, v) = cv2.split(imghsv)
        v = v*2
        v = np.clip(v,0,255)
        imghsv = cv2.merge([h,s,v])

        #-----converted it back to default uint8 after my hue adjustment--------------------
        imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
        #cv2.imshow('final', imgrgb)
        #cv2.waitKey(0)
        cv2.imwrite(destination, imgrgb)
        cv2.imwrite(destination2, imgrgb)

        #_____END_____# 

def value(readDirr):
  
    for file in os.listdir(readDirr):
        f_img = readDirr+"/"+file
        MYDIR = ("saturation" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "saturation"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
        destination2 = os.path.join(currentDir, fileName)
        #print("---------------------"+f_img)

        #-----Reading the image-----------------------------------------------------
        img = cv2.imread(f_img)
        #cv2.imshow("img",img) 

        #-----Converting image to LAB Color model----------------------------------- 
        lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        #cv2.imshow("lab",lab)

        #-----Splitting the LAB image to different channels-------------------------
        l, a, b = cv2.split(lab)
        #cv2.imshow('l_channel', l)
        #cv2.imshow('a_channel', a)
        #cv2.imshow('b_channel', b)

        #-----Applying CLAHE to L-channel-------------------------------------------
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        #cv2.imshow('CLAHE output', cl)

        #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
        limg = cv2.merge((cl,a,b))
        #cv2.imshow('limg', limg)

        #-----Converting image from LAB Color model to RGB model--------------------
        imgrgb = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        #cv2.imshow('final', imgrgb)
        #cv2.waitKey(0)
        cv2.imwrite(destination, imgrgb)
        cv2.imwrite(destination2, imgrgb)

        #_____END_____# 




#print(len(sys.argv))
#print(str(sys.argv))


async def main():

    # Detect Green
    detectGreen(sourceFolderCropped)
    
    # Increse Green in RGB
    increaseGreen(sourceFolderCropped)

    # Increse Hue
    hue(sourceFolderCropped)

    # Increse Saturation
    saturation(sourceFolderCropped)

asyncio.run(main())
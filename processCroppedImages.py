# The function of this python script is to process the already cropped images that are in the "sourceFolderCropped" folder.
# run using: py processCroppedImages.py
import PIL
import os
import os.path
import cv2 
from PIL import Image
import sys
import numpy as np

# Assumes images are in .jpg format
sourceFolderCropped = "./sourceFolderCropped"


def detectGreen():
  
    for file in os.listdir(sourceFolderCropped):
        f_img = sourceFolderCropped+"/"+file
        MYDIR = ("Final" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "detectGreen" + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
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

def increaseGreen():
  
    for file in os.listdir(sourceFolderCropped):
        f_img = sourceFolderCropped+"/"+file
        MYDIR = ("Final" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "increaseGreen"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
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

        #_____END_____#

def hue():
  
    for file in os.listdir(sourceFolderCropped):
        f_img = sourceFolderCropped+"/"+file
        MYDIR = ("Final" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "hue"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)

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


        #_____END_____#

def saturation():
  
    for file in os.listdir(sourceFolderCropped):
        f_img = sourceFolderCropped+"/"+file
        MYDIR = ("Final" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "saturation"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
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

        #_____END_____#

def value():
  
    for file in os.listdir(sourceFolderCropped):
        f_img = sourceFolderCropped+"/"+file
        MYDIR = ("Final" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "saturation"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
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

        #_____END_____# 

def value():
  
    for file in os.listdir(sourceFolderCropped):
        f_img = sourceFolderCropped+"/"+file
        MYDIR = ("Final" )
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            print("created folder : ", MYDIR)

        fileName = "saturation"  + file
        destination = os.path.join(os.getcwd(), MYDIR, fileName)
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

        #_____END_____# 





# Detect Green
detectGreen()
    
# Increse Green in RGB
increaseGreen()

# Increse Hue
hue()

# Increse Saturation
saturation()

print("Done!")

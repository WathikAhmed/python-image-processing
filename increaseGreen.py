import cv2
import numpy as np

#-----Reading the image-----------------------------------------------------
img = cv2.imread('513106.jpg', 1)
cv2.imshow("img",img) 

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
cv2.imshow('final', imgbgr)
cv2.waitKey(0)

#_____END_____#
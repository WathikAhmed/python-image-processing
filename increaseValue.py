import cv2
import numpy as np

#-----Reading the image-----------------------------------------------------
img = cv2.imread('513106.jpg', 1)
cv2.imshow("img",img) 

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
cv2.imshow('final', imgrgb)
cv2.waitKey(0)

#_____END_____#
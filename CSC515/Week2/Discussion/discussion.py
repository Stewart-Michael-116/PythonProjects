# Stewart Discussion Week 2 CSC 515

import cv2
import os
import numpy as np

img = cv2.imread('dollar.jpg')

cv2.imwrite('brain_image_copy.png', img)

cv2.imshow('brain_image_window', img)

#RGB functions
height,width,channels = img.shape
b,g,r = cv2.split(img)

rgb_split = np.empty([height,width*3,3], 'uint8')

rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])
resized_rgb_split = cv2.resize(rgb_split,None,fx=3,fy=3)
cv2.imshow("Channels", resized_rgb_split)
cv2.moveWindow("Channels",0,height)

#HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)
resized_hsv_split = cv2.resize(hsv_split,None,fx=3,fy=3)
cv2.imshow("split hsv", resized_hsv_split)

#Manual Transformation

manual_img = img.copy()
blue_matrix = np.array([[1, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]], dtype=np.float32)
blue_image = cv2.transform(manual_img, blue_matrix)
cv2.imshow("blue image manual", blue_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
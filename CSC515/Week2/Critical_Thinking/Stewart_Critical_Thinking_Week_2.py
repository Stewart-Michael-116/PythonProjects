# Stewart Critical Thinking 2
# Goal of this assignment is to use OpenCV to 
# open a photo of a puppy 
# extract these channels separately to make 2D images
# merge them back together into one photo
# Swap GR and see what the photos look like

import cv2
import os
import numpy as np

img = cv2.imread('puppy.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

cv2.imshow('puppy_image_window', img)

cv2.waitKey(0)

b,g,r = cv2.split(img)
concatenated = np.concatenate((b,g), axis=1)
final_concatenated = np.concatenate((concatenated,r), axis = 1)

cv2.imshow('puppy_B_G_R', final_concatenated)
cv2.waitKey(0)

merged_image = cv2.merge((b,g,r))
cv2.imshow('re_merged_image',merged_image)
cv2.waitKey(0)

merged_image = cv2.merge((b,r,g))
cv2.imshow('re_merged_image_swapped',merged_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
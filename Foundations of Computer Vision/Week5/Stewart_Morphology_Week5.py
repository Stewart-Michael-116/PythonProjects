# This week we are using opencv to perform morphological operations 
# We are using morphological operations in order to enhance the ability of computer vision systems to recognize fingerprints.
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in the fingerprint, grayscale to make it easy for threshold
original_img = cv2.imread("C:/Users/Michael/Documents/GitHub/PythonProjects/CSC515/Week5/fingerprint.jpg", cv2.IMREAD_GRAYSCALE)

# Resize to make multiple images easy to look at, then add threshold
img = cv2.resize(original_img,(0,0),fx = .25, fy = .25)
thresh, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# 
kernel = np.ones((2,2),np.uint8)
eroded_img = cv2.erode(binary_img, kernel, iterations = 1)
open_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
dilate_img = cv2.dilate(binary_img,kernel, iterations=1)
close_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)

combined_img1 = cv2.hconcat([img,binary_img])
combined_img2 = cv2.hconcat([eroded_img, open_img])
combined_img3 = cv2.hconcat([dilate_img, close_img])
combined_img4 = cv2.vconcat([combined_img1,combined_img2,combined_img3])

cv2.imshow("Binary Transformation of Fingerprint", combined_img4)

height, width = img.shape
print(height, width)

cv2.waitKey()
cv2.destroyAllWindows()
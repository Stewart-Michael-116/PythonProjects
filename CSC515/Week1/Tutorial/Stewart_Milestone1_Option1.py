import cv2
import os
img = cv2.imread('brain image.jpg')

cv2.imwrite('brain_image_copy.png', img)

cv2.imshow('brain_image_window', img)

cv2.waitKey(0)

# Public desktop
path = r"C:\Users\Public\Desktop\image"

# create folder if it does not exist already
if not os.path.exists(path):
    os.makedirs(path)

#Write it, and use path join to create new path.
cv2.imwrite(os.path.join(path , 'brain_image.png'), img)

cv2.destroyAllWindows()
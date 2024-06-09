# Draw things on my photo
import cv2
import os
import numpy as np

# import my dope selfie and make sure the computer did not lose it
img = cv2.imread("this_is_me.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"

# Resize since my photo was massive and show the image
img_resized = cv2.resize(img, (0,0), fx = 0.2, fy = 0.2)


# figure out how big my photo is.
height, width, _ = img_resized.shape
print(height, width)

cv2.rectangle(img_resized,(150,300),(220,350),(0,0,255),3)

cv2.rectangle(img_resized,(250,300),(320,350),(0,0,255),3)

cv2.circle(img_resized,(231,320),200,(0,255,0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_resized,"This is me",(50,50),font,2,(255,255,255),3,cv2.LINE_AA)

cv2.imshow("this is me", img_resized)



cv2.waitKey(0)

cv2.destroyAllWindows()
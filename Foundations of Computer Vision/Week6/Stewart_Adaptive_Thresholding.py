# Adaptive Thresholding Scheme
# Threshold an image based on the gray values in the image.

import cv2
import matplotlib.pyplot as plt
import numpy as np

indoor = cv2.imread("Indoor.jpg")
outdoor = cv2.imread("Outdoor.jpg")
deckbox = cv2.imread("Deckbox.jpg")

#fix color for thresholding to gray
indoor_g = cv2.cvtColor(indoor, cv2.COLOR_BGR2GRAY)
outdoor_g = cv2.cvtColor(outdoor,cv2.COLOR_BGR2GRAY)
deckbox_g = cv2.cvtColor(deckbox,cv2.COLOR_BGR2GRAY)

ret1, thresh1 = cv2.threshold(indoor_g, np.mean(indoor_g),255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(outdoor_g, np.mean(outdoor_g),255, cv2.THRESH_BINARY)
ret3, thresh3 = cv2.threshold(deckbox_g, np.mean(deckbox_g),255,cv2.THRESH_BINARY)


fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows = 2, ncols = 3, figsize = (10,10))
ax1.imshow(cv2.cvtColor(indoor,cv2.COLOR_BGR2RGB))
ax1.set_title('Indoor')
ax2.imshow(cv2.cvtColor(outdoor,cv2.COLOR_BGR2RGB))
ax2.set_title('Outdoor')
ax3.imshow(cv2.cvtColor(deckbox,cv2.COLOR_BGR2RGB))
ax3.set_title('Deckbox')
ax4.imshow(cv2.cvtColor(thresh1,cv2.COLOR_BGR2RGB))
ax4.set_title('Indoor Threshold')
ax5.imshow(cv2.cvtColor(thresh2,cv2.COLOR_BGR2RGB))
ax5.set_title('Outdoor Threshold')
ax6.imshow(cv2.cvtColor(thresh3,cv2.COLOR_BGR2RGB))
ax6.set_title('Outdoor Threshold')

print("\nThresholds Used\nIndoor:",np.mean(indoor_g),"Outdoor:",np.mean(outdoor_g),"Deckbox:",np.mean(deckbox_g))

plt.show()
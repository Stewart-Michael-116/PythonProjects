# Week 4 critical thinking
# Goal is to apply mean median and gaussian filters using different kernel sizes against an image that has impulse noise.
# These blurring effects should increase image quality for the user
import numpy as np
import cv2
import matplotlib.pyplot as plt


# Import image
img = cv2.imread('Mod4CT1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# creating arrays
Titles = []
images = []

# Apply mean filter using 3,3 kernel
threeMean = cv2.blur(img, (3,3))
Titles.append("Mean, 3x3")
images.append(threeMean)

# Apply median filter using 3,3 kernel
threeMedian = cv2.medianBlur(img, 3)
Titles.append("Median, 3x3")
images.append(threeMedian)

# Apply gaussian gaussian using 3,3 kernel. select two different values of sigma
gaussianThreeFirst = cv2.GaussianBlur(img,(3,3), 1)
gaussianThreeSecond = cv2.GaussianBlur(img,(3,3), 2)
Titles.append("Gaussian, 3x3, Sigma = 1")
images.append(gaussianThreeFirst)
Titles.append("Gaussian, 3x3, Sigma = 2")
images.append(gaussianThreeSecond)

# Apply mean filter using 5,5 kernel
fiveMean = cv2.blur(img, (5,5))
Titles.append("Mean, 5x5")
images.append(fiveMean)

# Apply median filter using 5,5 kernel
fiveMedian = cv2.medianBlur(img, 5)
Titles.append("Median, 5x5")
images.append(fiveMedian)

# Apply gaussian gaussian using 5,5 kernel. select same values of sigma as the first kernel
gaussianFiveFirst = cv2.GaussianBlur(img,(5,5), 1)
gaussianFiveSecond = cv2.GaussianBlur(img,(5,5), 2)
Titles.append("Gaussian, 5x5, Sigma = 1")
images.append(gaussianFiveFirst)
Titles.append("Gaussian, 5x5, Sigma = 2")
images.append(gaussianFiveSecond)

# Apply mean filter using 7,7 kernel
sevenMean = cv2.blur(img, (7,7))
Titles.append("Mean, 7x7")
images.append(sevenMean)

# Apply median filter using 7,7 kernel
sevenMedian = cv2.medianBlur(img, 7)
Titles.append("Median, 7x7")
images.append(sevenMedian)

# Apply mean gaussian using 7,7 kernel. select same values of sigma as the first kernel
gaussianSevenFirst = cv2.GaussianBlur(img,(7,7), 1)
gaussianSevenSecond = cv2.GaussianBlur(img,(7,7), 2)
Titles.append("Gaussian, 7x7, Sigma = 1")
images.append(gaussianSevenFirst)
Titles.append("Gaussian, 7x7, Sigma = 2")
images.append(gaussianSevenSecond)

# Make Arrays with titles
Titles.append("Original image")
images.append(img)

plt.figure(figsize=(20,10))
# Plot All Images
for i in range(len(Titles)):
    plt.subplot(4, 4, i+1), plt.imshow(images[i], 'gray')
    
    plt.title(Titles[i])

    plt.xticks([]),plt.yticks([])

plt.show()
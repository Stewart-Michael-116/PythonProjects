# Capstone Project for Computer Vision
# Face Detection and Privacy
# Create a facial detection program that blurs eyes for privacy

# different subjects
# Two images of human subjects Facing the Front, One image with non-human subject
# Human whole body
# Multiple Human subjects
# Person's face far away

# Apply blurring method to extracted image.

'''
To address privacy concerns you may want to use data anonymization.  On images, 
this can be achieved by hiding features that could lead to a person or personal data
 identification, such as the person’s facial features or a license plate number.

The goal of this project is to write algorithms for face detection and feature 
blurring.  Select three color images from the web that meet the following requirements:

Two images containing human subjects facing primarily to the front and one image with a non-human subject.
At least one image of a human subject should contain that person’s entire body.
At least one image should contain multiple human subjects.
At least one image should display a person’s face far away.
All images should vary in light illumination and color intensity. 
First, using the appropriate trained cascade classifierLinks to an external 
site., write one algorithm to detect the human faces in the gray scaled versions of 
the original images.  Put a red boundary box around the detected face in the image in order 
to see what region the classifier deemed as a human face. If expected results are not achieved
 on the unprocessed images, apply processing steps before implementing the classifier for optimal results.

After the faces have been successfully detected, you will want to process
only the extracted faces before detecting and applying blurring to hide the eyes. Although 
the eye classifierLinks to an external site. is fairly accurate, it is important that
 all faces are centered, rotated, and scaled so that the eyes are perfectly aligned. If expected results are not achieved, implement more image processing for optimal eye recognition. Now, apply a blurring method to blur the eyes out in the extracted image.

Inspect your results and write a summary describing the techniques you used to 
detect and blur the eyes out of human faces in images. Reflect on the challenges you 
faced
 and how you overcame these challenges.  Furthermore, discuss in your summary, the accuracy
   of your results for all three images and techniques you used to improve the accuracy after
     each repeated experiment.

Your submission should be one executable Python script and one summary of 2-3 pages in length.
'''

#Sample
import numpy as np

import cv2

img = cv2.imread('face.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

pretrained = 'haarcascade_frontalface_alt.xml'

#create a trained classifier object with the xml file

face_cascade = cv2.CascadeClassifier(pretrained)

#detect the face with the classifier

face = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5, minSize = (40,40))

#draw a rectangle around each detected face with

#the list of returned bounding box coordinates

for (x, y, w, h) in face:

    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) #red bounding box

cv2.imshow('face_detected',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Other sample
import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Blur sample

# Python program to explain cv2.blur() method  
  
# importing cv2  
import cv2  
  
# path  
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
  
# Reading an image in default mode  
image = cv2.imread(path)  
  
# Window name in which image is displayed  
window_name = 'Image'
  
# ksize 
ksize = (10, 10) 
  
# Using cv2.blur() method  
image = cv2.blur(image, ksize)  
  
# Displaying the image  
cv2.imshow(window_name, image)  
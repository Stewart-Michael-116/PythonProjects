# Capstone Project for Computer Vision
# Face Detection and Privacy
# Create a facial detection program that blurs eyes for privacy

# different subjects
# Two images of human subjects Facing the Front, One image with non-human subject
# Human whole body
# Multiple Human subjects
# Person's face far away

# Apply blurring method to extracted image.

import cv2
import numpy as np

pretrained_face = 'haarcascade_frontalface_alt.xml'
pretrained_eyes = 'haarcascade_eye.xml'
pretrained_body = 'haarcascade_fullbody.xml'
face_cascade = cv2.CascadeClassifier(pretrained_face)
eye_cascade = cv2.CascadeClassifier(pretrained_eyes)
body_cascade = cv2.CascadeClassifier(pretrained_body)

'''
This code segment used to be a separate function, but it ended up easier including it in the recognize face function.

def blur_eyes(faces,grayscalecode):
    eyes = eye_cascade.detectMultiScale(grayscalecode, scaleFactor = 1.05, minNeighbors = 5, minSize = (15,15))
    for (x, y, w, h) in eyes:
        roi = eyes[y:y+h, x:x+w]
        cv2.imshow('face_detected',roi)
        cv2.waitKey(0)
       
        # apply gaussian blur to face rectangle
        roi = cv2.GaussianBlur(roi, (17, 17), 30)
        
        # add blurred face on original image to get final image
        faces[y:y+roi.shape[0], x:x+roi.shape[1]] = roi
'''


def recognize_face(img):
    image_copy = img.copy()
    grayscalecode = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(grayscalecode, scaleFactor = 1.05, minNeighbors = 5, minSize = (40,40))

    for (x, y, w, h) in face:

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = grayscalecode[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            '''
            This was my attempt at replacing people's eyes with a blurred version of their eyes, but some organization didn't work out too
            well and the assignment said to extract the eyes from the photo and blur them so I switched directions.

            temp_blur = img
            temp_blur = cv2.blur(temp_blur,(30,30))
            h, w, c = img.shape

            mask = np.zeros((h, w, c), dtype=np.uint8)

            start_point = (ex+x, ey+y) 
            end_point = (ex+ew+x, ey+eh+y) 
            color = (255, 255, 255) 
            thickness = -1
            
            cv2.rectangle(mask, start_point, end_point, color, thickness)
            cv2.imshow('mask',mask)
            out = np.where(mask==(255, 255, 255), out, temp_blur)
            '''
            blur = cv2.blur(image_copy, (20,20))
     
            cropped = blur[ey+y:ey+y+eh, ex+x:ex+ew+x]
     
            cv2.imshow('original', img)
            cv2.imshow('Eye Blurred', cropped)

            cv2.waitKey(0)
            



    


def recognize_body(img):

    grayscalecode = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = body_cascade.detectMultiScale(grayscalecode, scaleFactor = 1.05, minNeighbors = 5, minSize = (40,40))

    for (x, y, w, h) in face:

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) #red bounding box
        #blur_eyes(face[y:y+h, x:x+w])

    
    cv2.imshow('face_detected',img)
    cv2.waitKey(0)


image1 = cv2.imread("image1.jpeg")
image2 = cv2.imread("image2.jpeg")
image3 = cv2.imread("image3.jpeg")
image4 = cv2.imread("image4.jpeg")

recognize_face(image2)
recognize_face(image1)
recognize_face(image3)
recognize_face(image4)
recognize_body(image4)

cv2.destroyAllWindows()
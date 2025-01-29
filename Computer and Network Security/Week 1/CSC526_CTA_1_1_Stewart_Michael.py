import PIL.ImageDraw
import PIL.Image
import matplotlib.pyplot as plt
import face_recognition

# Find all the faces in the image       
faces_image = face_recognition.load_image_file("faces.jpg")
face_locations = face_recognition.face_locations(faces_image)

numberOfFaces = len(face_locations)
print("Found {} face(s) in this picture.".format(numberOfFaces))

# Load the image into a Python Image Library object so that you can draw on top of it and display it

pilImage = PIL.Image.fromarray(faces_image)

for faceLocation in face_locations:

     # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
     top, right, bottom, left = faceLocation

     print("A face is located at pixel location Top: {}, Left {},Bottom: {}, Right: {}".format(top, left, bottom, right))

     # Draw a box around the face     
     drawHandle = PIL.ImageDraw.Draw(pilImage)     
     drawHandle.rectangle([left, top, right, bottom], outline="red")

# Display the image on screen
pilImage.show()

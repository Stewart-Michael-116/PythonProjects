import PIL.ImageDraw
import PIL.Image
import matplotlib.pyplot as plt
import face_recognition

# Find all the faces in the image       
face1_image = face_recognition.load_image_file("image1.jpg")
person_1_face_encoding = face_recognition.face_encodings(face1_image)[0]

known_faces = [person_1_face_encoding]

unknown_image = face_recognition.load_image_file("image2.jpg")
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

unkown_image2 = face_recognition.load_image_file("image1.jpg")
unknown_face_encodings2 = face_recognition.face_encodings(unkown_image2)

for unknown_face_encoding in unknown_face_encodings:

    results = face_recognition.compare_faces(known_faces, unknown_face_encoding, tolerance=0.6)
    name = "unkown"

    if results[0]:
        name = "Person 1"

    print(f"Found {name} in the second photo!")

for unknown_face_encoding2 in unknown_face_encodings2:

    results = face_recognition.compare_faces(known_faces, unknown_face_encoding2, tolerance=0.6)
    name = "unkown"

    if results[0]:
        name = "Person 1"

    print(f"Found {name} in the first photo!")
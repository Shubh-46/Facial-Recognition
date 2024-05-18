import face_recognition
import cv2
import numpy as np
import os
# from datetime import datetime

# taking input from the webcam
video_capture = cv2.VideoCapture(0)

#  now calling faces of students one by one...
akash_singh_image = face_recognition.load_image_file("photos/Akash_Singh.jpg")
akash_singh_encoding = face_recognition.face_encodings(akash_singh_image)[0]

akash_shukla_image = face_recognition.load_image_file("photos/Akash_Shukla.jpg")
akash_shukla_encoding = face_recognition.face_encodings(akash_shukla_image)[0]

ayush_sahoo_image = face_recognition.load_image_file("photos/Ayush_Sahoo.jpg")
ayush_sahoo_encoding = face_recognition.face_encodings(ayush_sahoo_image)[0]

gaurav_sharma_image = face_recognition.load_image_file("photos/Gaurav_Sharma.jpg")
gaurav_sharma_encoding = face_recognition.face_encodings(gaurav_sharma_image)[0]

jitendra_goyal_image = face_recognition.load_image_file("photos/Jitendra_Goyal.jpg")
jitendra_goyal_encoding = face_recognition.face_encodings(jitendra_goyal_image)[0]

nikhil_malhotra_image = face_recognition.load_image_file("photos/Nikhil_Malhotra.jpg")
nikhil_malhotra_encoding = face_recognition.face_encodings(nikhil_malhotra_image)[0]

nitin_singh_image = face_recognition.load_image_file("photos/Nitin_Singh.jpg")
nitin_singh_encoding = face_recognition.face_encodings(nitin_singh_image)[0]

pramod_kumar_singh_image = face_recognition.load_image_file("photos/Pramod_Kumar_Singh.jpg")
pramod_kumar_singh_encoding = face_recognition.face_encodings(pramod_kumar_singh_image)[0]

shubham_shrivastava_image = face_recognition.load_image_file("photos/Shubham_Shrivastava.jpg")
shubham_shrivastava_encoding = face_recognition.face_encodings(shubham_shrivastava_image)[0]

tarun_sharma_image = face_recognition.load_image_file("photos/Tarun_Sharma.jpg")
tarun_sharma_encoding = face_recognition.face_encodings(tarun_sharma_image)[0]

vikas_rajpoot_image = face_recognition.load_image_file("photos/Vikas_Rajpoot.jpg")
vikas_rajpoot_encoding = face_recognition.face_encodings(vikas_rajpoot_image)[0]

vikash_kumar_singh_image = face_recognition.load_image_file("photos/Vikash_Kumar_Singh.jpg")
vikash_kumar_singh_encoding = face_recognition.face_encodings(vikash_kumar_singh_image)[0]


known_face_encoding = [akash_singh_encoding, akash_shukla_encoding, ayush_sahoo_encoding, gaurav_sharma_encoding, jitendra_goyal_encoding, 
                       nikhil_malhotra_encoding, nitin_singh_encoding, pramod_kumar_singh_encoding, shubham_shrivastava_encoding, 
                       tarun_sharma_encoding, vikas_rajpoot_encoding, vikash_kumar_singh_encoding]


known_faces_names = ["akash singh", "akash shukla", "ayush sahoo", "gaurav sharma", "jitendra goyal", "nikhil malhotra", "nitin singh", 
                     "pramod kumar singh", "shubham shrivastava", "tarun sharma", "vikas rajpoot", "vikash kumar singh"]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True


while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
                
            if name in known_faces_names:
                if name in students:
                    print(name)

    
    cv2.imshow("facial_recognition", frame)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
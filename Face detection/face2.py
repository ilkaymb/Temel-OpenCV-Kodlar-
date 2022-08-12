import cv2
from cv2 import destroyAllWindows
from cv2 import waitKey
import numpy as np
import matplotlib.pyplot as plt 
 
 
# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

 
 
 
# create a function to detect face
def adjusted_detect_face(img):
     
    face_img = img.copy()
     
    face_rect = face_cascade.detectMultiScale(face_img,
                                              scaleFactor = 1.2,
                                              minNeighbors = 5)
     
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)\
         
    return face_img
 
 

 
# Reading in the image and creating copies

kamera=cv2.VideoCapture(1)
ret,img=kamera.read()
face = adjusted_detect_face(img)
plt.imshow(face)
waitKey(0)
destroyAllWindows()
  
    
cv2.imshow('face', face)
        


 
# Detecting the face

# Saving the image

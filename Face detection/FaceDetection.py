import cv2
from cv2 import destroyAllWindows
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
img = cv2.imread('sinem.jfif')
resim1=cv2.blur(img,(3,3))
ret,resim2=cv2.threshold(resim1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()
 
# Detecting the face
face = adjusted_detect_face(resim2)
plt.imshow(face)
# Saving the image
cv2.imshow('face', face)
cv2.waitKey(0)
cv2.destroyAllWindows()
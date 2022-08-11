import cv2
import numpy as np

kamera=cv2.VideoCapture(1)
while True:
    ret,goruntu=kamera.read()
    
    cv2.imshow("kamera",goruntu)
    
    if cv2.waitKey(30) &0xFF==ord("q"):
        break

kamera.release()

cv2.destroyAllWindows()
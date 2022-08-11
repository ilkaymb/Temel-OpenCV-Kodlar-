import cv2
import numpy as np

cap = cv2.VideoCapture("http://10.3.4.17:8080/video")
while(True):
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
cap.relaese()
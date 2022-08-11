import cv2
from cv2 import circle
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv2.rectangle(goruntu,(100,100),(200,200),(0,0,255),2)
    cv2.line(goruntu,(0,0),(100,100),(255,0,0),1)
    cv2.circle(goruntu,(150,100),50,(0,255,0),1)
    cv2.putText(goruntu,"ILKAY",(150,150),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,50),1)
    
    cv2.imshow("kamera",goruntu)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):#waitkey saniyede alınan kare sayısını ayarlıyor arttırdıkça yavaşlar
        break

kamera.release()

cv2.destroyAllWindows()
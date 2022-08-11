from multiprocessing.connection import wait
from turtle import width
import cv2
from cv2 import waitKey
import numpy

camera=cv2.VideoCapture(0)
width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc=cv2.VideoWriter_fourcc(*'MP4V')#formatı belirleme
writer=cv2.VideoWriter("kayit.mp4",fourcc,30,(width,height))#20 frame per second



while True:
    ret,frame=camera.read()
    writer.write(frame)
    
    cv2.imshow("camera",frame)
    
    if cv2.waitKey(30) &0XFF==ord("q"):
        break
    
    
camera.release()
writer.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")
cv2.line(resim,(0,0),(100,100),(0,0,255),2)
cv2.circle(resim,(100,100),20,(0,0,255),2)
cv2.putText(resim,"Merhaba",(150,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
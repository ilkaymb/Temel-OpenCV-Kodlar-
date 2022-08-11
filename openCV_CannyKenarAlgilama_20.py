from statistics import median
import cv2
from cv2 import Canny
import numpy as np




image=cv2.imread("trafik_isaret.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)

def autoCanny(blur,sigma=0.33):
    median=np.median(blur)
    
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0+sigma)*median))
    canny=cv2.Canny(blur,lower,upper)
    
    return canny
    
wide=cv2.Canny(blur,10,220)
tight=cv2.Canny(blur,200,230)
auto=autoCanny(blur)

cv2.imshow("auto",auto)
cv2.imshow("wide",wide)
cv2.imshow("tight",tight)
cv2.imshow("edges",np.hstack([auto,wide,tight]))


cv2.waitKey(0)
cv2.destroyAllWindows()
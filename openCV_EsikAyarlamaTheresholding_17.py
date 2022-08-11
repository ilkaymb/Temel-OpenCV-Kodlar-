import cv2
import numpy as np

image=cv2.imread("gok.png",0)

ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("thres1",thresh1)
cv2.imshow("thres2",thresh2)
cv2.imshow("thres3",thresh3)
cv2.imshow("thres4",thresh4)
cv2.imshow("thres5",thresh5)

cv2.imshow("image",image)



cv2.waitKey(0)
cv2.destroyAllWindows()
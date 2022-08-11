import cv2
import numpy as np

image=cv2.imread("resim2.jpg",0)
#Sımple thresholding
ret,thres1=cv2.threshold(image,160,255,cv2.THRESH_BINARY)
cv2.imshow("simple threshold",thres1)
#Adaptive thresholding
thres2=cv2.adaptiveThreshold(image,160,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                      cv2.THRESH_BINARY,11,2)
cv2.imshow("adaptive mean threshold",thres2)


thres3=cv2.adaptiveThreshold(image,160,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                      cv2.THRESH_BINARY,11,2)
cv2.imshow("adaptive gauss threshold",thres3)


cv2.imshow("resim",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
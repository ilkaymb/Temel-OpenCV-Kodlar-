import cv2
import numpy as np

image=cv2.imread("resim2.jpg")

meanfilter=cv2.blur(image,(7,7))
medianfilter=cv2.medianBlur(image,7)
gauss1=cv2.GaussianBlur(image,(3,3),0)
gauss2=cv2.GaussianBlur(image,(5,5),0)
gauss3=cv2.GaussianBlur(image,(7,7),0)

cv2.imshow("resim",image)
cv2.imshow("gauss1",gauss1)
cv2.imshow("gauss2",gauss2)
cv2.imshow("gauss3",gauss3)


cv2.waitKey(0)
cv2.destroyAllWindows()
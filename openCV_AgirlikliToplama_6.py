import cv2
import numpy as np

resim2=cv2.imread("resim2.jpg")
resim1=cv2.imread("resim1.jpg")

print(resim2[100,200])
print(resim1[300,430])

print(resim2[100,200]+resim1[300,430])


cv2.imshow("resim1",resim1)
cv2.imshow("resim2",resim2)


cv2.waitKey(0)
cv2.destroyAllWindows()
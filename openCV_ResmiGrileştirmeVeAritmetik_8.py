import cv2
import numpy as np

resim=cv2.imread("resim2.jpg")
resimGri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imshow("resim",resimGri)

yukseklik,genislik,kanalsayisi=resim.shape
print(yukseklik)
print(genislik)
print(kanalsayisi)

cv2.waitKey(0)
cv2.destroyAllWindows()
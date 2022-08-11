import cv2
import numpy as np

Resim=cv2.imread("1.png")
Resim[50,30]=[255,255,255]

for i in range(100):
    Resim[70,i]=[255,255,255]


cv2.imshow("resim",Resim)
print(Resim[(230,80)])
print("Resmin boyutu: "+str(Resim.size))
print("Resmin Özellikleri: "+str(Resim.shape))
print("Resmin veri tipi: "+str(Resim.dtype))




cv2.waitKey(0)
cv2.destroyAllWindows()



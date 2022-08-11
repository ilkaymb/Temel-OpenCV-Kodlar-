import cv2
import numpy as np

resim=cv2.imread("1.png")
cv2.rectangle(resim,(100,50),(150,30),[0,0,255],2)

cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
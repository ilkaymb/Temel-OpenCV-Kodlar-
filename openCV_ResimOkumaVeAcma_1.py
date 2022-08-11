import cv2
import numpy as np

resim = cv2.imread("1.png",0)

resim2 = cv2.imread("siyah_beyaz.png")

cv2.imshow("Resim adi",resim)

print(resim.shape)

#print(resim)

#cv2.imwrite("siyah_beyaz.png",resim)

#print(resim.size)

#print(resim.dtype)

cv2.waitKey(0)
cv2.destroyAllWindows()
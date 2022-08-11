import cv2
import numpy as np

resim=cv2.imread("resim2.jpg")
ikiKat=cv2.pyrUp(resim)
ikiKatKucuk=cv2.pyrDown(resim)

cv2.imshow("orjResim",resim)
cv2.imshow("ikiKat",ikiKatKucuk)

print(resim.shape)
print(ikiKatKucuk.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
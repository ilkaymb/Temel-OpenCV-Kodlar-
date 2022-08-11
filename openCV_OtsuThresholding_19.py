import cv2
from cv2 import imshow
from cv2 import threshold
import numpy as np

image=cv2.imread("resim1.jpg",0)

ret1,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#otsu thresholding
ret2,thresh2=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thres2",thresh2)
cv2.imshow("orj",image)
cv2.imshow("thres1",thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()



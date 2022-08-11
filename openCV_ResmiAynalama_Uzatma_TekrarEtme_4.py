import cv2
import numpy as np

resim = cv2.imread("1.png",0)

aynalama=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)

uzatma=cv2.copyMakeBorder(resim,75,75,50,50,cv2.BORDER_REPLICATE)


cv2.imshow("Resim adi",uzatma)




cv2.waitKey(0)
cv2.destroyAllWindows()
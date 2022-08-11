from contextlib import closing
import cv2
import numpy as np

image=cv2.imread("resim2.jpg")

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)#aşındırma

dilation=cv2.dilate(erosion,kernel,iterations=1)#genişleme
dilation2=cv2.dilate(erosion,kernel,iterations=2)#genişleme iteration attıkça arttırır

opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("image",image)

#cv2.imshow("opening",opening)
#cv2.imshow("closing",closing)
cv2.imshow("gradyan",gradyan)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)


cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

image=cv2.imread("resim2.jpg")

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)#aşındırma

dilation=cv2.dilate(erosion,kernel,iterations=1)#genişleme
dilation2=cv2.dilate(erosion,kernel,iterations=2)#genişleme iteration attıkça arttırır


cv2.imshow("image",image)
cv2.imshow("image2",erosion)

cv2.imshow("image3",dilation)
cv2.imshow("image4",dilation2)

cv2.waitKey(0)
cv2.destroyAllWindows()
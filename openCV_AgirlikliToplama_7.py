import cv2
import numpy as np

resim2=cv2.imread("1.png")
resim1=cv2.imread("siyah_beyaz.png")


toplam=cv2.add(resim1,resim2)
agirliklitoplama=cv2.addWeighted(resim2,0.7,resim1,0.3,0)

#cv2.imshow("resim1",resim1)
#cv2.imshow("resim2",resim2)
#cv2.imshow("toplam",toplam)
cv2.imshow("toplam",agirliklitoplama)

cv2.waitKey(0)
cv2.destroyAllWindows()
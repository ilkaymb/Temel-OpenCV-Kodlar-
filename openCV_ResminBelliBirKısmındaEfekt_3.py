import cv2
import numpy as np

resim=cv2.imread("1.png")

kesit=resim[50:150,300:400]
resim[0:100,0:100]=kesit
#cv2.imshow("resim",kesit)
cv2.imshow("sa",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()

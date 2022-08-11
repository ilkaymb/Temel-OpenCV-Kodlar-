import cv2
import numpy as np

image1=cv2.imread("NOT11.png")
image2=cv2.imread("NOT21.png")
cv2.imshow("image1",image1)
cv2.imshow("image2",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
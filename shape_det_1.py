#importing the module cv2
import cv2
import numpy as np


imageread = cv2.imread('ucgen2.jpg')

imagegray = cv2.cvtColor(imageread, cv2.COLOR_BGR2GRAY)

_, imagethreshold = cv2.threshold(imagegray, 245, 255, cv2.THRESH_BINARY_INV)
#cv2.threshold(imagegray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(imagethreshold,kernel,iterations=1)#aşındırma

imagethreshold=erosion

imagecontours, _ = cv2.findContours(imagethreshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for count in imagecontours:
    
    epsilon = 0.01 * cv2.arcLength(count, True)
    
    approximations = cv2.approxPolyDP(count, epsilon, True)
   
    cv2.drawContours(imageread, [approximations], 0, (200,0,0), 3)

    i, j = approximations[0][0] 
    
    if len(approximations) == 3:
        cv2.putText(imageread, "Triangle", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    elif len(approximations) == 4:
        cv2.putText(imageread, "Rectangle", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    elif len(approximations) == 5:
        cv2.putText(imageread, "Pentagon", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    elif 6 < len(approximations) < 15:
        cv2.putText(imageread, "Ellipse", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    else:
        cv2.putText(imageread, "Circle", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        




cv2.imshow("Resulting_image", imageread)
    
cv2.imshow("R", imagethreshold)
cv2.imshow("Re", erosion)

    
cv2.waitKey(0)
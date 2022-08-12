from imutils import paths
import cv2

magePath=list(paths.list_images("resimler"))
print(magePath)

for imagePath in magePath:
    image=cv2.imread(imagePath)
    cv2.imshow("frame",image)
    #print("piksellerin matriksleri: ",image)
    print("piksellerin toplamı: ",image.size)
    print("resmin boyutları: ",image.shape)
    print("resmin data tipi: ",image.dtype)
    cv2.waitKey(0)
    cv2.destroyAllWindows

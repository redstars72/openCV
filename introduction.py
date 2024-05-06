import cv2

#reading and displaying an image
readimg=cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
cv2.imshow("pikachu",readimg)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#reading image in greyscale
rimggrey=cv2.imread("pikachu.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("pikachugrey",rimggrey)
cv2.waitKey(0)
cv2.destroyAllWindows()

#saveimg
cv2.imwrite("pikachugreyscale.png",rimggrey)

#splitting bgr channels
b,g,r=cv2.split(readimg)
cv2.imshow("b",b)
cv2.waitKey(0)
cv2.imshow("g",g)
cv2.waitKey(0)
cv2.imshow("r",r)
cv2.waitKey(0)
cv2.destroyAllWindows()
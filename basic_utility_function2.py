import cv2

readams=cv2.imread("alienMountainScene.jpg")
cv2.imshow("ams",readams)
cv2.waitKey(0)

#rotate image
rows,columns=readams.shape[0:2]
m=cv2.getRotationMatrix2D((columns/2,rows/2),96,1)
rotatedimage=cv2.warpAffine(readams,m,(rows,columns))
cv2.imshow("ri",rotatedimage)
cv2.waitKey(0)

#converting image to grayscale
amsgray=cv2.cvtColor(readams,cv2.COLOR_BGR2GRAY)
cv2.imshow("amsgray",amsgray)
cv2.waitKey(0)

#blurring images
blurams=cv2.blur(readams,(77,23))
cv2.imshow("blurams",blurams)
cv2.waitKey(0)
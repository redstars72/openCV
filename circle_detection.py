import cv2, numpy

f=cv2.imread("alienMountainScene.jpg")
"""g=cv2.imread("ghost.png")"""
cv2.imshow("face",f)
cv2.waitKey(0)

grayf=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
blurgrayf=cv2.blur(grayf,(3,3))

detectcirc=cv2.HoughCircles(blurgrayf,cv2.HOUGH_GRADIENT,1,10,param1=65,param2=32,minRadius=0,maxRadius=9999)

print(detectcirc)

if detectcirc is not None:
    detectcirc= numpy.uint(numpy.around(detectcirc))
    for x,y,r in detectcirc[0]:
        print(x,y,r)
        detectedcirc=cv2.circle(f,(x,y),r,(0,255,0),4)
        cv2.imshow("circle detection",detectedcirc)

cv2.waitKey(0)
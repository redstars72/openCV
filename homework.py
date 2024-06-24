import cv2
import numpy

bg=cv2.imread("R.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("bg",bg)
cv2 .waitKey(0)

cv2.rectangle(bg,(1000,500),(1300,800),(0,255,255),-1)
cv2.imshow("body",bg)
cv2 .waitKey(0)

cv2.circle(bg,(1150,650),125,(255,255,255),-1)
cv2.imshow("eye",bg)
cv2 .waitKey(0) 

cv2.circle(bg,(1165,665),90,(0,0,0),-1) 
cv2.imshow("eye",bg)
cv2 .waitKey(0)

cv2.circle(bg,(1135,635),35,(255,255,255),-1)
cv2.imshow("eye",bg)
cv2 .waitKey(0) 

cv2.circle(bg,(1200,700),25,(255,255,255),-1)
cv2.imshow("eye",bg)
cv2 .waitKey(0)

drawg=cv2.cvtColor(bg,cv2.COLOR_BGR2GRAY)
drawgb=cv2.blur(drawg,(3,3))
 
circlecheck=cv2.HoughCircles(drawgb,cv2.HOUGH_GRADIENT,1,20,param1=65,param2=32,minRadius=15,maxRadius=125)

if circlecheck is not None:
    circlecheck= numpy.uint(numpy.around(circlecheck))
    for x,y,r in circlecheck[0]:
        print(x,y,r)
        circlecheck2=cv2.circle(bg,(x,y),r,(255,0,255),4)
        cv2.imshow("circle detection",circlecheck2)

cv2.waitKey(0)
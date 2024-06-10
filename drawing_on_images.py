import cv2

#displaying image
ams=cv2.imread("alienMountainScene.jpg",cv2.IMREAD_COLOR)
cv2.imshow("ams",ams)
cv2 .waitKey(0)

#drawing the line
cv2.line(ams,(20,1100),(1200,20),(15,30,200),6)
cv2.imshow("ams line",ams)
cv2 .waitKey(0)

#drawing a rectangle
cv2.rectangle(ams,(500,100),(1000,1000),(25,150,150),24)
cv2.imshow("ams rectangle",ams)
cv2 .waitKey(0)

#drawing a filled rectangle
cv2.rectangle(ams,(210,500),(500,750),(0,255,255),-1)
cv2.imshow("ams filled rectangle",ams)
cv2 .waitKey(0)

#drawing a circle
cv2.circle(ams,(800,700),80,(12,254,68),13)
cv2.imshow("ams circle",ams)
cv2 .waitKey(0)

#drawing a filled circle
cv2.circle(ams,(400,300),90,(12,45,76),-1)
cv2.imshow("ams filled circle",ams)
cv2 .waitKey(0)

#adding text
cv2.putText(ams,"CV2CV2CV2",(800,772),cv2.FONT_HERSHEY_SIMPLEX,4,(243,214,143),4)
cv2.imshow("ams text",ams)
cv2 .waitKey(0)

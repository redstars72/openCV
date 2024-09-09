import cv2
import numpy as np

vid=cv2.VideoCapture("video.mp4")
for i in range(60):
    success,bg=vid.read()
    if success==False:
        continue

lred=np.array([155,40,40])
ured=np.array([180,255,255])

while vid.isOpened():
    success,frame=vid.read()
    if success==False:
        break
    hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask1=cv2.inRange(hsvframe,lred,ured)
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3)),iterations=2)
    mask2=cv2.bitwise_not(mask1)
    result1=cv2.bitwise_and(bg,bg,mask=mask1)
    result2=cv2.bitwise_and(frame,frame,mask=mask2)
    result=cv2.add(result1,result2)
    cv2.imshow("masking",result)
    key=cv2.waitKey(15)
    if key==27:
        break
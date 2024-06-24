import cv2
import numpy

circlecounter=0
blob=cv2.imread("blooob.jpg")
params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=100
params.filterByCircularity=True
params.minCircularity=0.9
params.filterByConvexity=True
params.minConvexity=0.8
params.filterByInertia=True
params.minInertiaRatio=0.8
blobalob=cv2.SimpleBlobDetector_create(params)
blobalot=blobalob.detect(blob)
circlecounter=len(blobalot)
print(blobalot)
blobalobalot=cv2.drawKeypoints(blob,blobalot,numpy.zeros((1,1)),(255,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.putText(blobalobalot,"circle count: "+str(circlecounter),(0,500),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.4,(20,20,20),1)
cv2.imshow("blobalobalot",blobalobalot)
cv2.waitKey(0)
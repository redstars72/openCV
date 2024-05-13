import cv2
import numpy as np

#read images
readams=cv2.imread("alienMountainScene.jpg")
cv2.imshow("AMS",readams)
cv2.waitKey(0)

readwl=cv2.imread("winterLodge.jpg")
cv2.imshow("WL",readwl)
cv2.waitKey(0)
cv2.destroyAllWindows()

#add images
addamswl=cv2.add(readams,readwl)
cv2.imshow("AMS+WL",addamswl)
cv2.waitKey(0)
cv2.destroyAllWindows()

#weighted addition
addamswl2=cv2.addWeighted(readams,0.7,readwl,0.3,0)
cv2.imshow("AMS+WL 2",addamswl2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#subtraction
subtractamswl=cv2.subtract(readams,readwl)
cv2.imshow("AMS-WL",subtractamswl)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing an image
resizeams=cv2.resize(readams,(4900,200))
cv2.imshow("resize AMS",resizeams)
cv2.waitKey(0)
cv2.destroyAllWindows()

#add borders
pikachu=cv2.imread("pikachu.png")
addborderpikachu=cv2.copyMakeBorder(pikachu,1,30,4,10,cv2.BORDER_CONSTANT,value=(32,255,1))
cv2.imshow("adding borders",addborderpikachu)
cv2.waitKey(0)
addborderpikachu2=cv2.copyMakeBorder(pikachu,15,10,40,15,cv2.BORDER_REFLECT,value=(1,253,79))
cv2.imshow("adding borders",addborderpikachu2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#edge detection
detectams=cv2.Canny(readams,83,165)
cv2.imshow("edge detection",detectams)
cv2.waitKey(0)

"""cv2.imshow("AMS",readams)
cv2.waitKey(0)"""

cv2.destroyAllWindows()
detectpikachu=cv2.Canny(pikachu,83,165)

cv2.imshow("edge detection",detectpikachu)
cv2.waitKey(0)

"""cv2.imshow("AMS",pikachu)
cv2.waitKey(0)"""

cv2.destroyAllWindows() 

#erosion
erodeams=cv2.erode(readams,np.ones((2001,2001)))
cv2.imshow("eroding AMS",erodeams)
cv2.waitKey(0)
cv2.destroyAllWindows() 
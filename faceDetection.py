import cv2,os
mainfolder="images"
subfolder=input("What is your name? >")
path=os.path.join(mainfolder,subfolder)
if not os.path.isdir(path):
    os.makedirs(path)
    print("created")
xml="haarcascade_frontalface_default.xml"
det=cv2.CascadeClassifier(xml)
vid=cv2.VideoCapture(0)
imgcount=0
while imgcount<30:
    ret,fra=vid.read()
    gryfra=cv2.cvtColor(fra,cv2.COLOR_BGR2GRAY)
    facedet=det.detectMultiScale(gryfra,1.4,4)
    print(facedet)
    cv2.imshow("camera",fra)
    cv2.waitKey(10)
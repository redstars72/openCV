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
width=100
height=115
while imgcount<30:
    ret,fra=vid.read()
    gryfra=cv2.cvtColor(fra,cv2.COLOR_BGR2GRAY)
    facedet=det.detectMultiScale(gryfra,1.4,4)
    #print(facedet)leel
    if len(facedet)>0:
        imgcount+=1
        for x,y,w,h in facedet:
            cv2.rectangle(fra,(x,y),(x+w,y+h),(0,255,0),3)
            face=gryfra[y:y+h,x:x+w]
            resiface=cv2.resize(face,(width,height))
            cv2.imwrite(os.path.join(path,str(imgcount)+".png"),resiface)
    print(imgcount)
    cv2.imshow("camera",fra)
    key=cv2.waitKey(5)
    if key==27:
        break

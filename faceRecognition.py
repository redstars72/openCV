import cv2,os,numpy

mainfolder="images"
names={}
images=[]
labels=[]
id=0
for root, subfolders, files in os.walk(mainfolder):
    for subfolder in subfolders:
        names[id]=subfolder
        path=os.path.join(mainfolder,subfolder)
        for file in os.listdir(path):
            imagepath=os.path.join(path,file)
            images.append(cv2.imread(imagepath,0))
            labels.append(id)
        id+=1
print(names)
print(labels)
images=numpy.array(images)
labels=numpy.array(labels)
model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
xml="haarcascade_frontalface_default.xml"
det=cv2.CascadeClassifier(xml)
cam=cv2.VideoCapture(0)
width=100
height=115
while True:
    ret,fra=cam.read()
    gryfra=cv2.cvtColor(fra,cv2.COLOR_BGR2GRAY)
    facedet=det.detectMultiScale(gryfra,1.4,4)
    if len(facedet)>0:
        for x,y,w,h in facedet:
            cv2.rectangle(fra,(x,y),(x+w,y+h),(0,255,0),3)
            face=gryfra[y:y+h,x:x+w]
            resiface=cv2.resize(face,(width,height))
            pred,conf=model.predict(resiface)
            cv2.putText(fra,names[pred]+":"+str(round(conf))+"%",(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),5)
    cv2.imshow("camera",fra)
    key=cv2.waitKey(5)
    if key==27:
        break

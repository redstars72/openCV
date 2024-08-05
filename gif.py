import cv2,os
from PIL import Image
path="D:\\elini\\Google Drive EliNicholls2\\Jet Learn\\Visual Studio Code Files\\openCV\\pixilart-frames"
os.chdir(path)
print(os.listdir(path))
for file in os.listdir(path):
    if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
        img=Image.open(os.path.join(path,file))
        resimg=img.resize((150,150))
        resimg.save(file,"PNG")
merchr="merrychristmas.avi"
mcvid=cv2.VideoWriter(merchr,0,2,(150,150))
for file in os.listdir(path):
    if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
        print(file)
        image=cv2.imread(os.path.join(path,file))
        mcvid.write(image)

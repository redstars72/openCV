import cv2,os

path="D:\\elini\\Google Drive EliNicholls2\\Jet Learn\\Visual Studio Code Files\\openCV\\pixilart-frames"
os.chdir(path)
merchr="merrychristmas.avi"
mcvid=cv2.VideoWriter(merchr,0,2,(150,150))
for file in os.listdir(path):
    print(file)
    image=cv2.imread(os.path.join(path,file))
    mcvid.write(image)
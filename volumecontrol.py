import cv2 as cv
import time
import mediapipe as mp
import numpy as np 
import hand_tracking_module as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#############
wCam, hCam = 1280, 720
#############


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol=0
volBar=400
volPer=0

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime=0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success,img = cap.read()
    detector.findHands(img)
    lmList = detector.findPosition(img ,draw=False)
    if len(lmList)!=0:
        #print(lmList[4],lmList[8])
        x1, y1 = lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1],lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv.circle(img,(x1,y1),10,(255,0,0),cv.FILLED)
        cv.circle(img,(x2,y2),10,(255,0,0),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv.circle(img,(cx,cy),10,(255,0,0),cv.FILLED)
        length = math.hypot(x2-x1, y2-y1)
        print(length)
        # Hand range 50 - 400
        # vol range -65 - 0
        vol = np.interp(length,[50,400],[minVol,maxVol])
        volBar = np.interp(length,[50,400],[400, 150])
        volPer = np.interp(length,[50,400],[0,100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length<50:
            cv.circle(img,(cx,cy),10,(0,255,0),cv.FILLED)

    cv.rectangle(img,(50,200),(85,400),(255,0,0),3)
    cv.rectangle(img,(50,int(vol)),(85,400),(255,0,0),cv.FILLED)
    cv.putText(img, f' {int(volPer)}',(40,450),cv.FONT_HERSHEY_PLAIN,2,(255,0,0),3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}',(10,50),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),3)

    cv.imshow("Webcam",img)
    cv.waitKey(10)

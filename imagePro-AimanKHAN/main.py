import cv2
import numpy as np
import os
from PIL import Image

def re(out, img):
    w = img.shape[1]
    h = img.shape[0]
    sum = (w, h)
    res = cv2.resize(out, sum, interpolation=cv2.INTER_AREA)
    return res


# w, h = 1280, 720
# data = np.zeros((h, w, 3), dtype=np.uint8)
# data[0:720, 0:1280] = [255, 255, 0]
# img = Image.fromarray(data, 'RGB')
# img.save('back/11.jpg')

cam = cv2.VideoCapture(0)
success, shot = cam.read()
step = 0
imgFol = os.listdir("back")
bgList = []
kindList = []
for path in imgFol:
    name, extension = os.path.splitext(path)
    if extension == '.jpg':
        bgv = cv2.imread(f'back/{path}')
        bgList.append(bgv)
        kindList.append('img')
    elif extension == '.mp4':
        bgv = cv2.VideoCapture(f'back/{path}')
        bgList.append(bgv)
        kindList.append('vid')

index = 0

while True:
        success, img = cam.read()

        if kindList[index] == 'vid':
            backVideo = bgList[index]
            success, bgv = backVideo.read()

        elif kindList[index] == 'img':
            bgv = bgList[index]

        bg = re(bgv,shot)

        if step==0:
                shot = img

        sub=cv2.subtract(shot,img)
        mask = cv2.cvtColor(sub.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        mask[np.abs(mask) < 8] = 0
        mask[mask > 0] = 255
        mask = cv2.medianBlur(mask, 5)
        maskInv = cv2.bitwise_not(mask)
        maskInv = cv2.medianBlur(maskInv, 5)

        fg = cv2.bitwise_and(img,img,mask = mask)
        BG = cv2.bitwise_and(bg,bg,mask = maskInv)
        out = cv2.add(BG,fg)

        cv2.putText(out, 'To capture the background press (z) ', (0, 600), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0), 1,cv2.LINE_4)
        cv2.putText(out, 'To re-capture the background press (x) ', (0, 650), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0), 1, cv2.LINE_4)
        cv2.putText(out, 'To close it press (c) ', (0, 700), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0), 1, cv2.LINE_4)
        cv2.putText(out, '-- To change the background press (a) ', (270, 700), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1,cv2.LINE_4)

        # cv2.imshow('background model', shot)
        # cv2.imshow('current background',img)
        # cv2.imshow('subtracted background gray', gray)
        # cv2.imshow('subtracted ', sub)
        # cv2.imshow('mask', mask)
        # cv2.imshow('mask inverzting', maskInv)
        # cv2.imshow('fg', fg)
        # cv2.imshow('bgz', BG)
        cv2.imshow('Background Replacing',out)



        key = cv2.waitKey(3) & 0xFF
        if ord('c') == key:
                break
        elif ord('z') == key:
                step = 1
                print("Background Captured")
        elif ord('x') == key:
                step = 0
                print("Ready to Capture new Background")
        elif ord('a') == key:
                if index == 0:
                        index += 1
                elif index<len(bgList)-1:
                        index += 1
                else:
                        index = 0
                print("Background has been changed")

cv2.destroyAllWindows()
cam.release()

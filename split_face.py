import cv2
import json
import sys,os
from os.path import isfile, isdir, join
facepPsitions=open('face_position.json','r')

# 指定要列出所有檔案的目錄
mypath = "newDownload"

for j in facepPsitions.readlines():
    print(j)
    face=json.loads(j)
    (x, y, w, h)=(face['faceRectangle']['left'],face['faceRectangle']['top'],face['faceRectangle']['width'],face['faceRectangle']['height'])
    filename=face['faceId']
    # print(join(mypath,filename))
    image=cv2.imread(join(mypath,filename))
    # print(image)
    h=int(h*1.1)
    w=int(w*1.1)
    if y-h*0.05<0:
        y=0
    else:
        y=int(y-h*0.05)
    if x-w*0.05<0:
        x=0
    else:
        x=int(x-w*0.05)
    face=image[y:y+h,x:x+w]
    cv2.imwrite(join(mypath+'/face',filename),face)
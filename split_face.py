import cv2
import json
import sys,os
from os.path import isfile, isdir, join
facepPsitions=open('face_position.json','r')

mypath = "/www/LaravelBeauty/public/images"


def split_face (mypath,filename,x, y,w,h):
    image=cv2.imread(join(mypath,filename))
    # print(image)
    scale=1.2
    h=int(h*scale)
    w=int(w*scale)
    eps=(scale-1)/2
    if y-h*eps<0:
        y=0
    else:
        y=int(y-h*eps)
    if x-w*eps<0:
        x=0
    else:
        x=int(x-w*eps)
    face=image[y:y+h,x:x+w]
    cv2.resize(face,(128,128))
    print(join('/home/hausung1998/trainingData/face',filename))
    cv2.imwrite(join('/home/hausung1998/trainingData/face',filename),face)

def preprocess(mypath,filename,x, y):
    image=cv2.imread(join(mypath,filename))
    # print(image)
    length=min(image.shape[0],image.shape[1])
    if length+y>image.shape[0]:
        y=image.shape[0]-length
    if length+x>image.shape[1]:
        x=image.shape[1]-length
    if y-length/2<0:
        y=0
    else:
        y= int(y-length/2)
    if x-length/2<0:
        x=0
    else:
        x=int(x-length/2)
    preprocessImage=image[y:y+length,x:x+length]
    cv2.resize(preprocessImage,(256,256))
    cv2.imwrite(join('/home/hausung1998/trainingData/entireImage',filename),preprocessImage)



for j in facepPsitions.readlines():
    face=json.loads(j)
    (x, y, w, h)=(face['faceRectangle']['left'],face['faceRectangle']['top'],face['faceRectangle']['width'],face['faceRectangle']['height'])
    filename=face['faceId']
    split_face(mypath,filename,x, y,w,h)
    preprocess(mypath,filename,int(x+w/2),int(y+h/2))
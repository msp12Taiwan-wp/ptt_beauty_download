import cv2
import sys
import numpy as np
import urllib
import http.client
import json

text=open('apiKey.txt','r')
key=text.read()
text.close()

params = urllib.parse.urlencode({
    'returnFaceId': "true",
    'returnFaceLandmarks': 'false',
}) 
headers = {
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': key,
}

def detect_face_num(path):
    image=cv2.imread(path)
    f = open(path, "rb")
    body = f.read()
    f.close()
    try:
        conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    json_data=json.loads(data)
    l=len(json_data)
    if l!=1:
        return l
    face = json_data[0]
    f=open('face_position.json','a')
    f.write(json.dumps(face)+'\n')
    f.close()
    return l

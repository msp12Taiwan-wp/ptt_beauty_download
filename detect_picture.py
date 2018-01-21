from keras.models import load_model
from keras.models import model_from_json
import sys
import cv2

ans=['可愛','性感','氣質','陽光']

model = load_model('model.h5')
print("Loaded model from disk")

path=sys.argv[2]

def get_result(ImgArray):
    ImgArray = cv2.resize(ImgArray,(64,64))
    ImgArray = ImgArray.astype('float32')
    ImgArray = ImgArray/255
    ImgArray = ImgArray.reshape(1, 64, 64, 3)
    predicted_classes = model.predict_classes(ImgArray)
    return predicted_classes

image=cv2.imread(path)
result=get_result(image)
print(ans[result[0]-1])
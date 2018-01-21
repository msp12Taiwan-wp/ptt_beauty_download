import numpy as np
import cv2
import MySQLdb
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.optimizers import SGD, Adam
from keras.utils import np_utils


# Data loading and preprocessing
def load_data_CNN():
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='beauty')
    cursor=conn.cursor()
    SQLQuery="SELECT vote_records.feature_id, vote_records.is_agree, images.image_name FROM vote_records INNER JOIN images  ON vote_records.image_id=images.image_id"
    cursor.execute(SQLQuery)
    results = cursor.fetchall()
    x_train=[]
    y_train=[]
    temp={}
    df = pd.DataFrame(list(results), columns=['feature','orNot','filename'])
    abc = pd.crosstab(index=df['orNot'],columns=[ df['filename'],df['feature']], margins=True)
    abc=abc/abc.loc['All']
    a=df.filename.unique()
    for filename in a:
        col =abc[filename].columns
        tmp_list=[0,0,0,0]
        for feature in range(1,5):
            if feature in col:
                tmp_list[feature-1]=abc[filename][feature][1]
            else:
                tmp_list[feature-1]=0
        y_train.append(tmp_list)
        image=cv2.imread('/home/hausung1998/trainingData/entireImage/%s'%(filename))
        image=cv2.resize(image,(64,64))
        x_train.append(image)
    x_train=np.array(x_train,dtype=float)
    y_train=np.array(y_train,dtype=float)
    y_train=(y_train-y_train.min(0))/(y_train.max(0)-y_train.min(0))
    x_train = x_train.reshape(x_train.shape[0], 256, 256, 3)
    #x_test = x_test.reshape(x_test.shape[0], 25, 25, 1)
    x_train = x_train.astype('float32')
    x_train = x_train/255
    #x_test = x_test.astype('float32')
    #x_test = x_test/255
    #y_train = np_utils.to_categorical(y_train, 36)
    y_train = y_train.astype('float32')
    #y_test = np_utils.to_categorical(y_test, 26)
    return (x_train, y_train)#, (x_test, y_test)

# Create CNN model
(x_train, y_train) = load_data_CNN()

model = Sequential()

model.add(Conv2D(32, (5, 5), input_shape = (256, 256, 3)))

model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(64, (5, 5)))

model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())

model.add(Dense(units = 128, activation = 'relu'))
model.add(Dense(units = 4, activation='softmax'))

model.compile(loss = 'categorical_crossentropy',
              optimizer = SGD(lr = 0.2),
              metrics = ['accuracy'])

model.fit(x_train, y_train, batch_size = 100, epochs = 20)

model.save('model.h5')
print("Saved model to disk")

#score = model.evaluate(x_test, y_test)
#print('Test loss:', score[0])
#print('Test accuracy:', score[1])

#predicted_prob = model.predict(x_test)
#predicted_classes = model.predict_classes(x_test)

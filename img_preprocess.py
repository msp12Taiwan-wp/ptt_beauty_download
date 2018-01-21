
# coding: utf-8

# In[1]:

from sklearn import cluster, datasets
import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy import misc,ndimage


# In[2]:


from scipy import misc,ndimage
import matplotlib.pyplot as plt
# # scipy.ndimage
# f = misc.face()
# f = misc.imread('2195_1_8.jpg')
# # blurred_face = ndimage.gaussian_filter(f, sigma=3)
# img = cv2.imread('2196_8_18.jpg')
# plt.imshow(img)
# plt.show()


# In[3]:

img = misc.imread('newDownload/2196_4_10.jpg')
sqrimg=img[0:img.shape[1],0:img.shape[1]]
# height, width =sqrimg.shape[:2]
res = cv2.resize(sqrimg,(256, 256), interpolation = cv2.INTER_AREA)
blured = cv2.blur(res,(5,5))  
# mask = np.zeros((256+2, 256+2), np.uint8) 
# ret,blured,mask,ret=cv2.floodFill(blured, mask, (256-1,256-1), (255,255,255), (2,2,2),(3,3,3),8)
plt.imshow(blured)
plt.show()
blured.shape


# In[4]:


img = blured#cv2.imread('2195_1_8.jpg',0)
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()


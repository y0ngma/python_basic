import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('Charger69.jpg')
rows, cols, ch=img.shape

pt1=np.float32([[50, 50], [200, 50], [50, 200]])
pt2=np.float32([[10, 100], [200, 50], [100, 250]])

matrix=cv2.getAffineTransform(pt1, pt2)
new_img=cv2.warpAffine(img, matrix,(cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(new_img), plt.title('Output')
plt.show()
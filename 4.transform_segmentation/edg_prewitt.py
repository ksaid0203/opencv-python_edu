import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "../img/sudoku.jpg"

img = cv2.imread(file_name)

#gx_k = np.array([[-1,0,1], [-1,0,1],[-1,0,1]])
#gy_k = np.array([[1,1,1],[0,0,0], [-1,-1,-1]])
gx_k = (np.array([[1,1,1]]).T* (np.array([[-1,0,1]])))
gy_k = (np.array([[1,0,-1]]).T* (np.array([[1,1,1]])))

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

cv2.imshow('origin',img)
cv2.imshow('Gx', edge_gx)
cv2.imshow('Gy', edge_gy)
cv2.imshow('Gx+Gy', edge_gx+edge_gy)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
imgs = [('Origin', img), ('Gx', edge_gx), ('Gy', edge_gy), ('Gx+Gy', edge_gx + edge_gy)]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.title(imgs[i][0])
    plt.imshow(imgs[i][1])
    plt.xticks([]), plt.yticks([])
plt.show()
'''
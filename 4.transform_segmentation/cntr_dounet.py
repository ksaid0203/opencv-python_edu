import cv2
import numpy as np

file_name = '../img/shapes_dounet.jpg'
img = cv2.imread(file_name)
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

im2, contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
im2, contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contour, -1, (0,255,0), 3)
cv2.drawContours(img2, contour2, -1, (0,255,0), 3)

cv2.imshow('thresh', imthres)
cv2.imshow('RETR_EXTERNAL', img)
cv2.imshow('RETR_TREE', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
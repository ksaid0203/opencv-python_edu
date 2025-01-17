import cv2
import numpy as np

img = cv2.imread('../img/opencv_logo.png')                      # 기본 값 옵션
bgr = cv2.imread('../img/opencv_logo.png', cv2.IMREAD_COLOR)    # IMREAD_COLOR 옵션
bgra = cv2.imread('../img/opencv_logo.png', cv2.IMREAD_UNCHANGED) # IMREAD_UNCHANGED 옵션
print("default", img.shape, "color", bgr.shape, "unchanged", bgra.shape) # 각 옵션에 따른 이미지 shape

cv2.imshow('bgr', bgr)
cv2.imshow('bgra', bgra)
cv2.imshow('alpha', bgra[:,:,3])  # 알파 채널만 표시
cv2.waitKey(0)
cv2.destroyAllWindows()
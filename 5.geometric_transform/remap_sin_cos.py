import cv2
import numpy as np

l = 20      # 파장(wave length)
amp = 15    # 진폭(amplitude)

img = cv2.imread('../img/taekwonv1.jpg')
rows, cols = img.shape[:2]

# 초기 매핑 배열 생성 ---①
mapy, mapx = np.indices((rows, cols),dtype=np.float32)

# sin, cos 함수를 적용한 변형 매핑 연산 ---②

# 영상 재매핑 ---③
cnt = 0
while True:
    sinx = mapx + amp * np.sin(mapy/l)  
    cosy = mapy + amp * np.cos(mapx/l)

    img_sinx=cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR) # x축만 sin 곡선 적용
    img_cosy=cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR) # y축만 cos 곡선 적용
    # x,y 축 모두 sin, cos 곡선 적용 및 외곽 영역 보정
    img_both=cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE)
    cnt+=1
    # 결과 출력 
    cv2.imshow('origin', img)
    cv2.imshow('sin x', img_sinx)
    cv2.imshow('cos y', img_cosy)
    cv2.imshow('sin cos', img_both)

    if cv2.waitKey(100) != -1: break
cv2.destroyAllWindows()
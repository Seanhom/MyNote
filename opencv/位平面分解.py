import cv2
import numpy as np
lena=cv2.imread("lena.jpg",0)
cv2.imshow('lena',lena)
r,c = lena.shape
x= np.zeros((r,c,8),dtype=np.uint8)
# 提取各个位平面的提取矩阵的值
for i in range(8):
    x[:,:,i]=2**i
r=np.zeros((r,c,8),dtype=np.uint8)
# 实现各个位平面的提取、阈值处理和显示
for i in range(8):
    r[:,:,i] = cv2.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    print(r[:,:i])
    cv2.imshow(str(i),r[:,:,i])
cv2.waitKey(0)
cv2.destroyAllWindows()

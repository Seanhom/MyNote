import cv2
import numpy as np
o = cv2.imread("scenery.jpg")

# 生成高斯金字塔
G0 = o
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)

# 生成拉普拉斯金字塔
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)

# 复原G0
RG0 = L0 + cv2.pyrUp(G1)
print("G0's shape=",G0.shape)
print("RG0'shape=",RG0.shape)
result = RG0 - G0
result = abs(result)
print("原始图像G0与恢复图像RG0差值的绝对值和：",np.sum(result))

# 复原G1
RG1 = L1 + cv2.pyrUp(G2)
print("G1's shape=",G1.shape)
print("RG1'shape=",RG1.shape)
result = RG1 - G1
result = abs(result)
print("原始图像G0与恢复图像RG0差值的绝对值和：",np.sum(result))

# 复原G2
RG2 = L2 + cv2.pyrUp(G3)
print("G2's shape=",G2.shape)
print("RG2'shape=",RG2.shape)
result = RG2 - G2
result = abs(result)
print("原始图像G0与恢复图像RG0差值的绝对值和：",np.sum(result))


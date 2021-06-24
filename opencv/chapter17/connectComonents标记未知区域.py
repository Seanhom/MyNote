import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("water_coins.jpg")
# 灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 换颜色空间
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 拷一份RGB
ishow = img.copy()
# 阈值分割
# cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU  将阈值设置为0，它会自动根据其直方图得到最优阈值
ret1,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 开操作：先腐蚀，再膨胀
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

# cv2.dilate(): 膨胀
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# 对二值化图像进行处理，计算前景对象中像素离 0 的距离， 对计算结果阈值化，就可以分离出前景
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret2 , fore = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
fore = np.uint8(fore)

ret,markers1 = cv2.connectedComponents(fore)
foreAdv = fore.copy()
unknown = cv2.subtract(sure_bg,foreAdv)
ret, markers2 = cv2.connectedComponents(foreAdv)
markers2 = markers2+1
markers2[unknown == 255] = 0


plt.subplot(121)
plt.imshow(markers1)
plt.axis('off')

plt.subplot(122)
plt.imshow(markers2)
plt.axis('off')

print(ret)
plt.show()






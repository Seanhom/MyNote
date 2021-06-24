
import numpy as np
import cv2
import matplotlib.pyplot as plt
#1. 开运算对原始图像O去噪
img = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)    #thresh 为二值化图像
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel,iterations=2)

#2. 腐蚀确定背景B。  “原始图像 - 确定背景”
sure_bg = cv2.dilate(opening,kernel,iterations=3)

#3. 距离变换函数 cv2.distanceTransform()对原始图像运算，并进行阈值处理，确定前景F
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret2, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)

#4. 计算未知区域 UN = O - B - F
unknown = cv2.subtract(sure_bg,sure_fg)

#5. cv2.connectedComponents()  对原始图像O进行标注
ret3, markers = cv2.connectedComponents(sure_fg)

#6. 对cv2.connectedComponents()的结果进行修正
markers = markers+1
markers[unknown==255] = 0

#7. 使用分水岭函数完成对图像的分割
markers = cv2.watershed(img, markers)
img[markers == -1] = [0,255,0]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(241)
plt.imshow(ishow)
plt.title('0.原图')
plt.axis('off')
plt.subplot(242)
plt.imshow(opening)
plt.title('1.开运算')
plt.axis('off')
plt.subplot(243)
plt.imshow(sure_bg)
plt.title('2.腐蚀运算')
plt.axis('off')

plt.subplot(244)
plt.imshow(sure_fg)
plt.title('3.距离变换')
plt.axis('off')

plt.subplot(245)
plt.imshow(unknown)
plt.title('4.unkown')
plt.axis('off')

plt.subplot(246)
plt.imshow(sure_fg)
plt.title('5. 对O标注')
plt.axis('off')

plt.subplot(247)
plt.imshow(sure_fg)
plt.title('6.markers修正')
plt.axis('off')

plt.subplot(248)
plt.imshow(img)
plt.title('7.分水岭对图像分割')
plt.axis('off')
plt.show()








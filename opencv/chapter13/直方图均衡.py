import cv2
import matplotlib.pyplot as plt
img = cv2.imread("equ.bmp",cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
cv2.imshow("original",img)
cv2.imshow("result",equ)
plt.figure("原始图像直方图")
plt.hist(img.ravel(),256)
plt.figure("均衡化结果直方图")
plt.hist(equ.ravel(),256)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()




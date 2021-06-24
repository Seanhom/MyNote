import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.bmp",0)
#傅里叶变换
f = np.fft.fft2(img)

#0频率分量移到频域图像的中心位置
fshift = np.fft.fftshift(f)

# 将复数数组的值调整到[0,255]的灰度空间内
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(img,cmap="gray")
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(magnitude_spectrum,cmap="gray")
plt.title("result")
plt.axis("off")
plt.show()








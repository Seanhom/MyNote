import cv2
import matplotlib.pyplot as plt
o = cv2.imread("boatGray.bmp")
histb = cv2.calcHist([o],[0],None,[256],[0,255])
plt.plot(histb,color='b')
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow = img.copy()

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
cv2.imshow("opening",opening)
cv2.waitKey(0)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)

ret, fore = cv2.threshold(dist_transform, 0.7*dist_transform.max(),255,0)

plt.subplot(131)
plt.imshow(ishow)
plt.axis('off')
plt.subplot (132)
plt.imshow(dist_transform)
plt.axis('off')
plt.subplot(133)
plt.imshow(fore)
plt.axis('off')
plt.show()

















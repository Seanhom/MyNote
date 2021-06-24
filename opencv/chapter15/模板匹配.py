import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("lena512g.bmp",0)
template = cv2.imread("temp.bmp",0)
th,tw = template.shape[::]
rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
topLeft = minLoc
bottomRight = (topLeft[0]+tw,topLeft[1]+th)
cv2.rectangle(img,topLeft,bottomRight,255,2)
plt.subplot(121),plt.imshow(rv,cmap="gray")
plt.title("Matching Result"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(img,cmap="gray")
plt.title("Deteced Point"),plt.xticks([]),plt.yticks([])
plt.show()



















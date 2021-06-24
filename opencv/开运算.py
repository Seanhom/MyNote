import cv2
import numpy as np
img = cv2.imread("fushi.png")
k = np.ones((10,10),np.uint8)
r1 = cv2.morphologyEx(img,cv2.MORPH_OPEN,k)
cv2.imshow("original",img)
cv2.imshow("result",r1)
cv2.waitKey()
cv2.destroyAllWindows()
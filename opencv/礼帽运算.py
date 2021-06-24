import cv2
import numpy as np
o1 = cv2.imread("fushi.png")
o2 = cv2.imread("lena.jpg")
k = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(o1,cv2.MORPH_TOPHAT,k)
r2 = cv2.morphologyEx(o2,cv2.MORPH_TOPHAT,k)
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as np
o = cv2.imread("fushi.png",cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(o,kernel)
cv2.imshow("original",o)
cv2.imshow("erosion",erosion)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as  np
o = cv2.imread("lena.jpg")
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(o,kernel,iterations=3 )
cv2.imshow("original",o)
cv2.imshow("dilation",dilation)
cv2.waitKey()
cv2.destroyAllWindows()
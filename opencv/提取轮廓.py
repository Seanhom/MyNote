import  cv2
import numpy as np
o = cv2.imread("scenery.jpg")
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(o.shape,np.uint8)
mask = cv2.drawContours(mask,contours,-1,(255,255,255),-1)
cv2.imshow("mask",mask)
loc= cv2.bitwise_and(o,mask)
cv2.imshow("location",loc)
cv2.waitKey()
cv2.destroyAllWindows()


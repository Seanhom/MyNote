import cv2
import numpy as np

o = cv2.imread("edges_close.bmp")
cv2.imshow("original",o)


gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    x,y,w,h = cv2.boundingRect(contours[i])
    print("x ={0},y={1},w ={2},h={3}".format(x, y, w, h))
    brcnt = np.array([[[x,y]],[[x+w,y]],[[x+w,y+h]],[[x,y+h]]])
    cv2.drawContours(o,[brcnt],-1,[255,255,255],2)
cv2.imshow("result",o)
cv2.waitKey(0)

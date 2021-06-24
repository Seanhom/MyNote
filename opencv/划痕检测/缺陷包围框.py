import cv2
import  numpy as np
o = cv2.imread("edges_close.bmp")
src = cv2.imread("Image0001.bmp")
height,width = src.shape[0:2]
src = cv2.resize(src,(int(width/2),int(height/2)))
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    cv2.polylines(src, [hull], True, (0, 255, 0), 2)
cv2.imshow("result",src)
cv2.imwrite("result.bmp",src)
cv2.waitKey(0)
cv2.destroyAllWindows()





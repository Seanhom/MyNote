import cv2
o = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
SobelX = cv2.Sobel(o,cv2.CV_64F,1,0,ksize=3)
SobelY = cv2.Sobel(o,cv2.CV_64F,0,1,ksize=3)
SobelX = cv2.convertScaleAbs(SobelX)
SobelY = cv2.convertScaleAbs(SobelY)
SobelXY = cv2.addWeighted(SobelX,0.5,SobelY,0.5,0)

ScharrX = cv2.Scharr(o,cv2.CV_64F,1,0)
ScharrY = cv2.Scharr(o,cv2.CV_64F,0,1)
ScharrX = cv2.convertScaleAbs(ScharrX)
ScharrY = cv2.convertScaleAbs(ScharrY)
ScharrXY = cv2.addWeighted(ScharrX,0.5,ScharrY,0.5,0)

cv2.imshow("original",o)
cv2.imshow("Sobelxy",SobelXY)
cv2.imshow("ScharrXY",ScharrXY)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
o = cv2.imread("bianyuan.png",cv2.IMREAD_GRAYSCALE)
SobelX = cv2.Sobel(o,cv2.CV_64F,1,0)
SobelY = cv2.Sobel(o,cv2.CV_64F,0,1)
SobelX=cv2.convertScaleAbs(SobelX)
SobelY=cv2.convertScaleAbs(SobelY)
SobelXY = cv2.addWeighted(SobelX,0.5,SobelY,0.5,0)
cv2.imshow("original",o)
cv2.imshow("xy",SobelXY)
cv2.waitKey()
cv2.destroyAllWindows()



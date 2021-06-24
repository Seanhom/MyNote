import cv2
o = cv2.imread("lena.jpg")
r = cv2.bilateralFilter(o,25,170,170)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
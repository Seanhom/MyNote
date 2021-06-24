import cv2
o = cv2.imread("lena.jpg")
r1 =cv2.boxFilter(o,-1,(5,5),normalize=0)
r2 = cv2.boxFilter(o,-1,(2,2),normalize=0)
cv2.imshow("o",o)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
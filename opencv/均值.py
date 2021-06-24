import cv2
c= cv2.imread("lena.jpg")
r = cv2.blur(c,(5,5))
r2 = cv2.blur(c,(30,30))
cv2.imshow("original",c)
cv2.imshow("result",r)
cv2.imshow("r2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
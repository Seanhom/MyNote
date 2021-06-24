import cv2
lena=cv2.imread("lena.jpg",-1)
# print(lena)
# cv2.namedWindow("lesson")
cv2.imshow("demo",lena)
r = cv2.imwrite('kk.bmp',lena)
key =cv2.waitKey()
# if key==ord('A'):
#     cv2.imshow("PressA",lena)
# elif key==ord('B'):
#     cv2.imshow("PressB",lena)
cv2.destroyWindow("demo")
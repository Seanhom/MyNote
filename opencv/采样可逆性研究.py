import cv2
o = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
down = cv2.pyrDown(o)
up = cv2.pyrUp(down)
diff = up - o
print("o's shape : ",o.shape)
print("up.shape :", up.shape)
cv2.imshow("original",o)
cv2.imshow("up",up)
cv2.imshow("defference",diff)
cv2.waitKey()
cv2.destroyAllWindows()
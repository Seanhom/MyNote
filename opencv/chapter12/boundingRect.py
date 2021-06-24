import cv2
o = cv2.imread("cc.bmp")
cv2.imshow("original",o)


gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(o,(x,y),(x+w,y+h),(255,255,255),2)
sum = 0
count = 0
for m in range(w):
    for n in range(h):
        # print("row+m ={0},col+n={1}".format(x+m,y+n))
        if binary[y+n, x+m] > 0:
            count = count + 1
            sum = sum + ((x+m)-x)**2 + ((y+n)-y)**2
print("binary's shape =",binary.shape)
cv2.imshow("binary",binary)
print("count = ",count)
print("sum= ",sum)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()


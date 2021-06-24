import cv2
import numpy as np
#读取原始载体图像
lena= cv2.imread("lena.jpg",0)
#读取水印图像
watermark=cv2.imread("scenery.jpg",0)
watermark=watermark[400:928,500:1032]
w=watermark[:,:]>0
watermark[w]=1
r,c = lena.shape
t254 = np.ones((r,c),dtype=np.uint8)*254

lenaH7=cv2.bitwise_and(lena,t254)
e = cv2.bitwise_or(lenaH7,watermark)

t1 = np.ones((r,c),dtype=np.uint8)

wm = cv2.bitwise_and(e,t1)
print(wm)

w = wm[:,:]>0
wm[w]=255
cv2.imshow("lena",lena)
cv2.imshow("watermark",watermark*255)
cv2.imshow("e",e)
cv2.imshow("wm",wm)
cv2.waitKey(0)
cv2.destroyAllWindows()
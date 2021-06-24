import  cv2
import numpy as np
img = np.zeros((8,8),dtype= np.uint8)
print("img=\n",img)
cv2.imshow("one",img)
print("读取像素点img[0,3]=",img[0,3])
img[0,3] = 255
cv2.imshow("two",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
lena = cv2.imread("lena.jpg",0)
r,c = lena.shape
key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption = cv2.bitwise_xor(lena,key)
decryption = cv2.bitwise_xor(encryption,key)
cv2.imshow("lena",lena)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)
cv2.waitKey(0)
cv2.destroyAllWindows()
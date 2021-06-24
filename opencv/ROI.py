import numpy as np
import  cv2
a=cv2.imread('lena.jpg',cv2.IMREAD_UNCHANGED)
face = a[220:400,250:350]
cv2.imshow("original",a)
cv2.imshow("face",face)
cv2.waitKey()
cv2.destroyAllWindows()
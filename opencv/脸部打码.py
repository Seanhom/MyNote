import numpy as np
import  cv2
a=cv2.imread('lena.jpg',cv2.IMREAD_UNCHANGED)
face = np.random.randint(0,256,(180,100,3))
a[220:400,250:350]=face
cv2.imshow("result",a)
# cv2.imshow("face",face)
cv2.waitKey()
cv2.destroyAllWindows()
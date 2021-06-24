import cv2
import numpy as np
mask = np.zeros([600,600],np.uint8)
mask[200:400,200:400] = 255
cv2.imshow("mask",mask)
cv2.waitKey()
cv2.destroyAllWindows()





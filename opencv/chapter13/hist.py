import cv2
import matplotlib.pyplot as plt
o = cv2.imread("boat.jpg")
# cv2.imshow("originao",o)
plt.hist(o.ravel(),256)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()


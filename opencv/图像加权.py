import  cv2
lena=cv2.imread('lena.jpg',cv2.IMREAD_UNCHANGED)
scenery = cv2.imread('scenery.jpg',cv2.IMREAD_UNCHANGED)
# print(scenery.shape)
# print(lena.shape)
sce = scenery[300:828,1250:1782]
print(sce.shape)
add=cv2.addWeighted(lena,0.6,sce,0.4,0)
cv2.imshow('result',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
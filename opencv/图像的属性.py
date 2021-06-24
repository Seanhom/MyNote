import cv2
gray=cv2.imread("lena.jpg",0)
print("gray's shape = ",gray.shape)
print("gray's size = ",gray.size)
print("gray's dtype = ",gray.dtype)
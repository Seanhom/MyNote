#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

lsPointsChoose = []
tpPointsChoose = []
pointsCount = 0
count = 0

def on_mouse(event, x, y, flags, param):
	global img, point1, point2, count, pointsMax
	global lsPointsChoose, tpPointsChoose
	global pointsCount
	global img2, ROI_bymouse_flag
	img2 = img.copy()
	if event == cv2.EVENT_LBUTTONDOWN:
		pointsCount = pointsCount + 1
		print('pointsCount:', pointsCount)
		point1 = (x, y)
		print(x, y)
		cv2.circle(img2, point1, 10, (0, 255, 0), 2)
		lsPointsChoose.append([x, y])  # 用于转化为darry 提取多边形ROI
		tpPointsChoose.append((x, y))  # 用于画点
		print(len(tpPointsChoose))
		for i in range(len(tpPointsChoose) - 1):
			print('i', i)
			cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
		cv2.imshow('src', img2)


	if event == cv2.EVENT_RBUTTONDOWN:
		print("right-mouse")
		pointsCount = 0
		tpPointsChoose = []
		lsPointsChoose = []
		print(len(tpPointsChoose))
		for i in range(len(tpPointsChoose) - 1):
			print('i', i)
			cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
		cv2.imshow('src', img2)

	if event == cv2.EVENT_LBUTTONDBLCLK:
		ROI_byMouse()
		ROI_bymouse_flag = 1
		lsPointsChoose = []

def ROI_byMouse():
	global src, ROI, ROI_flag, mask2
	mask = np.zeros(img.shape, np.uint8)
	pts = np.array([lsPointsChoose], np.int32)
	pts = pts.reshape((-1, 1, 2))
	#画多边形
	mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
	#填充多边形
	mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
	cv2.imshow('mask', mask2)
	cv2.imwrite('mask.jpg', mask2)
	contours, hierarchy = cv2.findContours(cv2.cvtColor(mask2, cv2.COLOR_BGR2GRAY), cv2.RETR_TREE,
												  cv2.CHAIN_APPROX_NONE)
	ROIarea = cv2.contourArea(contours[0])
	print("ROIarea:", ROIarea)
	ROI = cv2.bitwise_and(mask2, img)
	cv2.imwrite('ROI.jpg', ROI)
	cv2.imshow('ROI', ROI)

img = cv2.imread('Image0001.bmp')
height,width = img.shape[0:2]    # (高，宽)
img = cv2.resize(img,(int(width/2),int(height/2)))          #（宽，高）
ROI = img.copy()
cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)
cv2.imshow('src', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# gray = cv2.imread("ROI.jpg")
# mask = cv2.imread("mask.jpg")
# re = cv2.bitwise_and(gray,mask)
# cv2.imshow('result', re)
# cv2.waitKey(0)
# cv2.destroyAllWindows()























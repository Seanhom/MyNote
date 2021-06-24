#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import math
import numpy as np

#提取出缺陷
gray = cv2.imread("ROI.bmp")
mask = cv2.imread("mask.bmp")
dst = cv2.bitwise_not(gray)
re = cv2.bitwise_and(dst,mask)
# cv2.imshow('result', re)
# cv2.imwrite("re.bmp",re)
# cv2.waitKey(0)

edge = cv2.Canny(re,20,100)
# cv2.imshow("edge",edge)
# cv2.imwrite("edge.jpg",edge)
# cv2.waitKey(0)

kernel = np.ones((8, 8), np.uint8)
edges_close = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel,iterations=1)    #形态学的变化，cv2.MORPH_OPEN 先进行腐蚀操作，再进行膨胀操作
# cv2.imshow('edges_close',edges_close)
# cv2.waitKey(0)

# 基于面积去噪
contours,hierarchy = cv2.findContours(edges_close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
for i in range(len(contours)):
    area =  cv2.contourArea(contours[i])
    threshold = 50
    if area < threshold:
        cv2.drawContours(edges_close, contours, i, 0, -1)  # -1 : 绘制实心轮廓
cv2.imwrite("edges_close.bmp",edges_close)
# cv2.imshow('edges_close',edges_close)
# cv2.waitKey(0)
contours,hierarchy = cv2.findContours(edges_close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
totalDefects = 0
for i in range(len(contours)):
    #求相对面积
    height, width = edges_close.shape[0:2]  # (高，宽)
    St = height * width
    Sc = cv2.contourArea(contours[i])
    Sr = (Sc / St) * math.pow(10, 4)

    # 求归一化方差
    # 求质心
    cnt = contours[i]
    M = cv2.moments(cnt)
    x0 = int(M['m10'] / M['m00'])
    y0 = int(M['m01'] / M['m00'])
    # print("x0 ={0},y0={1}".format(x0,y0))
    x, y, w, h = cv2.boundingRect(contours[i])
    # print("x ={0},y={1},w ={2},h={3}".format(x,y,w,h))
    sum = 0
    count = 0
    for m in range(2*w):
        for n in range(2*h):
            # print("row+m ={0},col+n={1}".format(x+m,y+n))
            if edges_close[y0-h+n,x0-w+m]>0:
                count = count + 1
                sum = sum + ((x0-w+m)-x0)**2 + ((y0-h+n)-y0)**2
    print("count = ", count)
    print("sum= ", sum)
    var = sum / (count * Sc)

    print("Sr ={0},Var={1}".format(Sr,var))
    if (Sr > 1) & (var > 2):
        totalDefects = totalDefects + 1
    # for delta_x in range(w+h):   #x
    #     for delta_y in range(w+h):  #y
    #         # print("row+m ={0},col+n={1}".format(x+m,y+n))
    #         y = y + delta_y
    #         x = x + delta_x
    #         if y > (height-1):
    #             y = height-1
    #         if x > (width-1):
    #             x = width-1
    #         # print("x ={0},y={1}".format( x, y))
    #         if edges_close[y, x] > 0:
    #             count = count + 1
    #             sum = sum + (x - x0) ** 2 + (y - y0) ** 2
    # print("count = ",count)
    # print("sum= ",sum)
    # var = sum / (count * Sc)
    # if (Sr>1) & (var>10) :
    #     totalDefects = totalDefects + 1

if totalDefects == 0 :
    print("该图像没有检测到划痕！")
else:
    print("该图像存在{}条划痕！".format(totalDefects))








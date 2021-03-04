# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:19:03 2018

@author: Clement LAGNEAU
"""









"""
ca marche 

import numpy as np
import cv2
im = cv2.imread('opencv_test2.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


import cv2
im = cv2.imread('opencv_test2.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)

cnt = contours[4]
img2 = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img2)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:12:59 2018

@author: Clement LAGNEAU
"""

import cv2
from PIL import Image


img = cv2.imread('image_opencv.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img2)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imwrite('image_opencv_modifie.jpg',img2)


def contours(URLImage, resolution = 5):
    img0 = Image.open(URLImage)
    colonne,ligne = img0.size
    image_en_memoire = img0.load()
    img = Image.new("RGB", img0.size , "white")
    res = img.load()
    for x in range(1,colonne-1):
        for y in range(1,ligne-1):
            p = image_en_memoire[x,y]
            if p>resolution :
                res[x,y] = (255,255,255)
            else:
                res[x,y] = (0,0,0)
    img.save(('.'.join(URLImage.split('.')[:-1]))+".contours."+(URLImage.split('.')[-1]))

def coef(URLImage):
    image = Image.open(URLImage)
    colonne,ligne = image.size
    n=colonne*ligne
    image_en_memoire = image.load()
    somme=0
    for x in range(1,colonne-1):
        for y in range(1,ligne-1):
            p = image_en_memoire[x,y]
            if p==(255,255,255):
                somme += 1
    return(somme,n)

"""
a=coef('testopencvimg.contours.res10.jpg')

a
Out[23]: (29349, 50232)

(a[1]-a[0])/a[1]
Out[26]: 0.41573100812231245
"""


"""

im = cv2.imread('test77.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2',img2)
"""

"""
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

cnt = contours[4]
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
"""
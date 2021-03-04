# -*- coding: utf-8 -*-
"""
OpenCV
"""

import cv2

#Ouverture + affichage image en noir en blanc
img = cv2.imread('image_opencv.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.imwrite('image_opencv_modifie.jpg',img)


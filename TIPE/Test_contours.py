# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:09:33 2018

@author: Clement LAGNEAU
"""
from PIL import Image

def contours(URLImage):
    img0 = Image.open(URLImage)
    colonne,ligne = img0.size
    image_en_memoire = img0.load()
    img = Image.new("RGB", img0.size , "white")
    res = img.load()
    for x in range(1,colonne-1):
        for y in range(1,ligne-1):
            p = image_en_memoire[x,y]
            m=p[0]+p[1]+p[2]
            m = int(m/3)
            if m>60 :
                res[x,y] = (255,255,255)
            else:
                res[x,y] = (0,0,0)
    img.save(('.'.join(URLImage.split('.')[:-1]))+".contours."+(URLImage.split('.')[-1]))

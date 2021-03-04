# -*- coding: utf-8 -*-
"""
Created on Wed May 30 18:28:18 2018

@author: Clement LAGNEAU
"""

from PIL import Image

def negatif(URLImage):
    image = Image.open(URLImage)
    colonne,ligne = image.size
    res = Image.new("RGB", image.size , "white")
    image_en_memoire = image.load()
    p0=0
    p1=0
    p2=0
    for y in range(ligne):
        for x in range(colonne):
            p0 = 255-image_en_memoire[x,y][0]
            p1 = 255-image_en_memoire[x,y][1]
            p2 = 255-image_en_memoire[x,y][2]
            res.putpixel((x,y),(p0,p1,p2))
    res.save("negatif-"+URLImage)
    res.close()
    image.close()



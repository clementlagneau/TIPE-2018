# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:52:58 2018

@author: Clement LAGNEAU
"""

from PIL import Image

def coef(URLImage):
    image = Image.open(URLImage)
    colonne,ligne = image.size
    n=colonne*ligne
    image_en_memoire = image.load()
    somme=0
    for x in range(colonne):
        for y in range(ligne):
            p = image_en_memoire[x,y]
            if p==(255,255,255) :
                somme += 1
    return(somme/n)


"""



a=coef('test9.convolution.contours.jpg')

a[0]/a[1]
Out[32]: 0.037247173116738336


"""
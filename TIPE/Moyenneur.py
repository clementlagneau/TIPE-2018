# -*- coding: utf-8 -*-
"""
Clement LAGNEAU
TIPE 2018

Moyenne de l'image
"""

from PIL import Image

def moyenne_image(img):
    image = Image.open(img) # on ouvre l'image
    enMemoire = image.load() # on la charge en memoire
    colonne,ligne = image.size #on calcul le nbre de pixel
    n = colonne*ligne
    moy_r=0
    moy_v=0
    moy_b=0
    for i in range(colonne):
        for j in range(ligne):
            p=enMemoire[i,j]
            moy_r += p[0]
            moy_v += p[1]
            moy_b += p[2]
    image.close()
    return((moy_r/n,moy_v/n,moy_b/n))

print(moyenne_image('test9.jpg'))



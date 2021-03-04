# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:00:13 2018

@author: Clement LAGNEAU
"""

def convolution(URLImage, Filtre):
    def Convolution(Filtre,TPix,x,y):
        p0 = 0
        p1 = 0
        p2 = 0
        for i in range(-1,2):
            for j in range(-1,2):
                p0 += Filtre[i+1][j+1]*TPix[x+i,y+j][0]
                p1 += Filtre[i+1][j+1]*TPix[x+i,y+j][1]
                p2 += Filtre[i+1][j+1]*TPix[x+i,y+j][2]
                # normalisation des composantes
                p0 = int(p0)
                p1 = int(p1)
                p2 = int(p2)
        # retourne le pixel convolué
        return (p0,p1,p2)
      
    imgo = Image.open(URLImage)
    img = Image.new("RGB", imgo.size , "white")
    colonne,ligne = imgo.size
    image_en_memoire = imgo.load()
    res = img.load()
    for x in range(1,colonne-1):
        for y in range(1,ligne-1):
            p = Convolution(Filtre,image_en_memoire,x,y)
            res[x, y]=p
    img.save(('.'.join(URLImage.split('.')[:-1]))+".convolution."+(URLImage.split('.')[-1]))
    img.close()


from PIL import Image

Filtre = [[-1,-1,-1],
          [-1,8,-1],
          [-1,-1,-1]]

ImageFile = 'test.jpg' #Pointe vers l'image

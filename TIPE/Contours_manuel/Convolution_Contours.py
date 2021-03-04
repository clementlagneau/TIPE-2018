# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:22:51 2018

@author: Clement LAGNEAU
"""

from PIL import Image

"""
Pour les test
"""

Filtre = [[-1,-1,-1],
          [-1,8,-1],
          [-1,-1,-1]]


ImageFile = 'test9.jpg' #Pointe vers l'image


"""
Vrai code
"""

def convolution(URLImage, Filtre):
    def Convolution(Filtre,image,x,y):
        p0 = 0
        p1 = 0
        p2 = 0
        for i in range(-1,2):
            for j in range(-1,2):
                p0 += Filtre[i+1][j+1]*image[x+i,y+j][0]
                p1 += Filtre[i+1][j+1]*image[x+i,y+j][1]
                p2 += Filtre[i+1][j+1]*image[x+i,y+j][2]
                # normalisation des composantes
                p0 = int(p0)
                p1 = int(p1)
                p2 = int(p2)
        # retourne le pixel convolué
        return (p0,p1,p2)
      
    image = Image.open(URLImage)
    resultat = Image.new("RGB", image.size , "white")
    colonne,ligne = image.size
    image_en_memoire = image.load()
    res = resultat.load()
    for x in range(1,colonne-1):
        for y in range(1,ligne-1):
            p = Convolution(Filtre,image_en_memoire,x,y)
            res[x, y]=p
    resultat.save('convolution.'+URLImage)
    resultat.close()
    image.close()


def contours(URLImage, resolution = 100):
    image = Image.open(URLImage)
    colonne,ligne = image.size
    image_en_memoire = image.load()
    for x in range(colonne):
        for y in range(ligne):
            p = image_en_memoire[x,y]
            m=p[0]+p[1]+p[2]
            m = int(m/3)
            if m>resolution :
                image_en_memoire[x,y] = (255,255,255)
            else:
                image_en_memoire[x,y] = (0,0,0)
    image.save('contours.'+URLImage)
    
    
def detection_contours(URLImage):
    convolution(URLImage, Filtre)
    contours('convolution.'+URLImage)




#detection_contours(ImageFile)

    
    
    
    
    
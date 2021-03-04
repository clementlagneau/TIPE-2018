# -*- coding: utf-8 -*-
"""
Module pour le traitement d'image par convolution

Clement LAGNEAU-DONZELLE
MP 2017-2017
Lycee Jean Perrin Lyon 9eme
Tipe
"""

"""
On Importe PIL
"""
from PIL import Image

n=3
part = int(n/2)
"""
def creation_filtre():
    res=[[]for x in range(n)]

"""


ImageFile = 'test.jpg' #Pointe vers l'image

#Change rien (sauf les bords)
Filtre_test = [[0,0,0],
               [0,1,0],
               [0,0,0]]

def filtre_test():
    res=[[0 for x in range(n)]for x in range(n)]
    res[part][part]=1
    return(res)


#Bords
Filtre_test2 = [[-2,-1,0],
                [-1,0,1],
                [0,1,2]]

def filtre_test2():
    res=[[x for x in range(-n+k+1,k+1)]for k in range(n)]
    return(res)


Filtre_test3 =[[1/9,1/9,1/9],
               [1/9,1/9,1/9],
               [1/9,1/9,1/9]]


Filtre_test4 = [[-1,-1,-1],
                [-1,8,-1],
                [-1,-1,-1]]

Filtre_test5= [[-1,-1,-1],
               [0,0,0],
               [1,1,1]]

Filtre= Filtre_test4

def Convolution(Filtre,im,x,y):
    """
    Prend en argument un filtre, une image et l'emplacement du pixel
    Renvoie le pixel convolué
    """
    p0 = 0
    p1 = 0
    p2 = 0
    for i in range(-1,2):
        for j in range(-1,2):
            p0 += Filtre[i+1][j+1]*im[y+i,x+j][0]
            p1 += Filtre[i+1][j+1]*im[y+i,x+j][1]
            p2 += Filtre[i+1][j+1]*im[y+i,x+j][2]
            # Composantes non entieres 
            p0 = int(p0)
            p1 = int(p1)
            p2 = int(p2)
            # retourne le pixel convolué
    return(p0,p1,p2)

def convolutionne(Filtre, ImageFile):
    #Ouverture de l'image
    try:
        im = Image.open(ImageFile)
    except:
        print ('Erreur sur ouverture du fichier ')
    #Traitement de l'image
    res = Image.new("RGB", im.size , "white")
    colonne,ligne = im.size
    image_en_memoire = im.load()
    for x in range(1,ligne-1):
        for y in range(1,colonne-1):
            p = Convolution(Filtre,image_en_memoire,x,y)
            res.putpixel((y,x),p)
    #Sauvegarde l'image
    res.save(('.'.join(ImageFile.split('.')[:-1]))+".contours."+(ImageFile.split('.')[-1]))
    im.close()
    res.close()



convolutionne(Filtre, ImageFile)






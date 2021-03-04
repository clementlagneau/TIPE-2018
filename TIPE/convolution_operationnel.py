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

"""
def creation_filtre():
    res=[[]for x in range(n)]

"""


ImageFile = 'test.jpg' #Pointe vers l'image

Filtre_test = [[0,0,0],
               [0,1,0],
               [0,0,0]]

Filtre_test2 = [[-2,-1,0],
                [-1,0,1],
                [0,1,2]]

Filtre_test3 =[[1/9,1/9,1/9],
               [1/9,1/9,1/9],
               [1/9,1/9,1/9]]

Filtre_test4 = [[-1,-1,-1],
                [-1,8,-1],
                [-1,-1,-1]]

Filtre= Filtre_test3

def Convolution(Filtre,TPix,x,y):
  p0 = 0
  p1 = 0
  p2 = 0
  for i in range(-1,2):
   for j in range(-1,2):
    p0 += Filtre[i+1][j+1]*TPix[y+i,x+j][0]
    p1 += Filtre[i+1][j+1]*TPix[y+i,x+j][1]
    p2 += Filtre[i+1][j+1]*TPix[y+i,x+j][2]
    # normalisation des composantes
    p0 = int(p0)
    p1 = int(p1)
    p2 = int(p2)
  # retourne le pixel convolué
  return (p0,p1,p2)

def convolutionne(Filtre, ImageFile):
    try:
      imgo = Image.open(ImageFile)
    except IOError:
      print ('Erreur sur ouverture du fichier ')
    img = Image.new("RGB", imgo.size , "white")
    colonne,ligne = imgo.size
    image_en_memoire = imgo.load()
    for x in range(1,ligne-1):
      for y in range(1,colonne-1):
       p = Convolution(Filtre,image_en_memoire,x,y)
       img.putpixel((y,x),p)
    img.save("Nouvelle_Image_Test_Convolution.jpg")
    # fermeture du fichier image
    img.close()

convolutionne(Filtre, ImageFile)






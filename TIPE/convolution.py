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

#n forcement impair
n=9
part=int(n/2)


def creation_filtre():
    res=[[1/n**2 for x in range(n)]for x in range(n)]
    return(res)

"""
Aucune convolution
    res=[[0 for x in range(n)]for x in range(n)]
    res[part][part]=1
"""

ImageFile = 'test.jpg' #Pointe vers l'image

Filtre = creation_filtre()


def Convolution(Filtre,TPix,x,y):
  p0 = 0
  p1 = 0
  p2 = 0
  for i in range(-part,part+1):
   for j in range(-part,part+1):
    p0 += Filtre[i+part][j+part]*TPix[y+i,x+j][0]
    p1 += Filtre[i+part][j+part]*TPix[y+i,x+j][1]
    p2 += Filtre[i+part][j+part]*TPix[y+i,x+j][2]
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
    img = Image.new("RGB", imgo.size , "black")
    colonne,ligne = imgo.size
    image_en_memoire = imgo.load()
    for x in range(part,ligne-part):
      for y in range(part,colonne-part):
       p = Convolution(Filtre,image_en_memoire,x,y)
       img.putpixel((y,x),p)
    img.save("Nouvelle_Image_Test_Convolution"+str(n)+".jpg")
    # fermeture du fichier image
    img.close()


convolutionne(Filtre, ImageFile)






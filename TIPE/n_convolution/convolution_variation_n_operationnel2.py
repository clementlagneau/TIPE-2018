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



def filtre_test2():
    res=[[x for x in range(-n+k+1,k+1)]for k in range(n)]
    return(res)



from PIL import Image

#n impair
n=3
part=n//2

def creation_filtre():
    res=[[1/n**2 for x in range(n)]for x in range(n)]
    return(res)

URLImage = 'image.jpg' #Pointe vers l'image

Filtre = creation_filtre()


def Convolution(Filtre,image,x,y):
  p0 = 0
  p1 = 0
  p2 = 0
  for i in range(-part,part+1):
      for j in range(-part,part+1):
          p0 += Filtre[i+part][j+part]*image[x+i,y+j][0]
          p1 += Filtre[i+part][j+part]*image[x+i,y+j][1]
          p2 += Filtre[i+part][j+part]*image[x+i,y+j][2]
          # normalisation des composantes
          p0 = int(p0)
          p1 = int(p1)
          p2 = int(p2)
          # retourne le pixel convolué
  return (p0,p1,p2)

def convolutionne(Filtre, URLImage):
    #Ouverture Image
    try:
        image = Image.open(URLImage)
    except IOError:
        print ('Erreur sur ouverture du fichier ')
    #Declaration des variables
    resultat = Image.new("RGB", image.size , "black")
    colonne,ligne = image.size
    image_en_memoire = image.load()
    #Traitement
    for y in range(part,ligne-part):
        for x in range(part,colonne-part):
            p = Convolution(Filtre,image_en_memoire,x,y)
            resultat.putpixel((x,y),p)
    #On enregistre l'image
    resultat.save("Convolution-"+str(n)+"-"+URLImage)
    # fermeture du fichier image
    resultat.close()
    image.close()


convolutionne(Filtre, URLImage)






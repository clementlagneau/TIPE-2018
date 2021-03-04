# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:37:27 2017

@author: Clement LAGNEAU
"""

from PIL import Image

try:
    im= Image.open('test2.jpg')
except:
    print("Probleme lors de l'ouverture de l'image")


"""
data = list(im.getdata())

r,g,b = im.split()  ## Récupération des différentes composantes de l'image 
r.save('r.jpg') ## Sauvegarde des différentes images composantes 
g.save('g.jpg') 
b.save('b.jpg')
"""

imNew = Image.new(im.mode, im.size)


colonne,ligne = im.size

def avec_moyennes():
    compteur = 0
    moyenne0 = 0
    moyenne1 = 0
    moyenne2 = 0
    
    for i in range(ligne):
      for j in range(colonne):
        pixel = im.getpixel((j,i)) # récupération du pixel
        moyenne0 += pixel[0]**2
        moyenne1 += pixel[1]**2
        moyenne2 += pixel[2]**2
        compteur += 1
    
    moyenne0 = int((moyenne0)**(0.5)/compteur)
    moyenne1 = int((moyenne1)**(0.5)/compteur)
    moyenne2 = int((moyenne2)**(0.5)/compteur)
    
    
    for i in range(ligne):
      for j in range(colonne):
        pixel = im.getpixel((j,i)) # récupération du pixel
        # on calcule le complement à MAX pour chaque composante - effet négatif
        p = ( pixel[0] - moyenne0,pixel[1] - moyenne1, pixel[2] - moyenne2)
        # composition de la nouvelle image
        imNew.putpixel((j,i), p)

for i in range(ligne):
  for j in range(colonne):
    pixel = im.getpixel((j,i)) # récupération du pixel
    # on calcule le complement à MAX pour chaque composante - effet négatif
    p = ( pixel[0],pixel[1], pixel[2])
    # composition de la nouvelle image
    imNew.putpixel((j,i), p)




imNew.save("Nouvelleimage2.jpg")
im.close()

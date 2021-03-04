# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:00:08 2018

@author: Clement LAGNEAU
"""
"""
Calcul des caracteristiques moyenne
"""

import os
monRepertoire='D:/Cours/MP/TIPE/Banque_image/ville'
os.chdir(monRepertoire)
fichiers = [f for f in os.listdir(monRepertoire) if os.path.isfile(os.path.join(monRepertoire, f))]

dic={}
somme=[0,0,0]
coefficient = 0
indice=0

for image in fichiers:
    indice += 1
    
    moy = moyenne_image(image)
    somme[0] += moy[0]
    somme[1] += moy[1]
    somme[2] += moy[2]
    
    dic[image]=moy
    
    detection_contours(image)
    coefficient += coef('contours.convolution.'+image)

somme[0] = somme[0]/indice
somme[1] = somme[1]/indice
somme[2] = somme[2]/indice
coefficient = coefficient/indice

print(somme,coefficient)

resolution = 0.1
if not os.path.exists('defectueuses'):
    os.makedirs('defectueuses')


def modif_moyenne(URLImage,moyimage,moybanque):
    image = Image.open(URLImage)
    enMemoire = image.load()
    colonne,ligne = image.size
    r=int(moybanque[0]-moyimage[0])
    v=int(moybanque[1]-moyimage[1])
    b=int(moybanque[2]-moyimage[2])
    p0=0
    p1=0
    p2=0
    for i in range(colonne):
        for j in range(ligne):
            p=enMemoire[i,j]
            p0 = p[0] + r
            p1 = p[1] + v
            p2 = p[2] + b
            enMemoire[i,j]=(p0,p1,p2)
    image.save('moyenne_modifie.'+URLImage)
    image.close()
    
for image in fichiers:
    if abs(coef(image)-coefficient)>resolution:
        os.rename(image,monRepertoire+'/defectueuses/'+image)
    else:
        modif_moyenne(image,dic[image],somme)





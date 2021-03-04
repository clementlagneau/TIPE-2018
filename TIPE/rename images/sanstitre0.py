# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:50:21 2018

@author: Clement LAGNEAU
"""
indice = 0
import os
monRepertoire='D:/Cours/MP/TIPE/Banque_image/ville'
os.chdir(monRepertoire)
fichiers = [f for f in os.listdir(monRepertoire) if os.path.isfile(os.path.join(monRepertoire, f))]

for x in fichiers:
    os.rename(x,monRepertoire+'/image'+str(indice)+'.jpg')
    indice += 1

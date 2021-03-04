# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:25:02 2017

@author: Clement LAGNEAU
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio as io

im = io.imread('http://info−llg.fr/commun−mp/images/picasso.png')


def convolution(m, c):
    n, p, q = m.shape
    mm = np.zeros_like(m)
    for i in range(1, n-1):
        for j in range(1, p-1):
            s = 0
            for u in range(3):
                for v in range(3):
                    s += c[u, v] * m[i-1+u, j-1+v]
                for k in range(q):
                    if s[k] < 0:
                        mm[i, j, k] = 0
                    elif s[k] > 255:
                        mm[i, j, k] = 255
                    else:
                        mm[i, j, k] = s[k]
    return mm


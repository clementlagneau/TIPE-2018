# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:32:14 2017

@author: Clement LAGNEAU
"""

from PIL import Image
im1 = Image.open("T:\Seville.png")
im2 = Image.new("RGB",(512,512))
im3 = Image.new("RGB",(512,512))

for y in range(512):
    for x in range(512):
        p = im1.getpixel((x,y))
        r = (p[0]+p[1]+p[2])/3
        v = r
        b = r
        im2.putpixel((x,y),(r,v,b))

for y in range(1,511):
    for x in range(1,511):
        pix0 = im2.getpixel((x,y))
        pix1 = im2.getpixel((x-1,y-1))
        pix2 = im2.getpixel((x,y-1))
        pix3 = im2.getpixel((x+1,y-1))
        pix4 = im2.getpixel((x-1,y))
        pix5 = im2.getpixel((x+1,y))
        pix6 = im2.getpixel((x-1,y+1))
        pix7 = im2.getpixel((x,y+1))
        pix8 = im2.getpixel((x+1,y+1))
        r = 8*pix0[0]-pix1[0]-pix2[0]-pix3[0]-pix4[0]-pix5[0]-pix6[0]-pix7[0]-pix8[0]
        r = r/1
        r = r+128
        r = 255-r
        v = r
        b = r
        im3.putpixel((x,y),(r,v,b))
        im3.save("T:\Seville_contours.png")
        im3.show()

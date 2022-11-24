# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 21:42:04 2022

@author: jovita amanda putri
"""

def pangkat(a,b,c=1):
    if b>0:
        c=c*a
        b=b-1
        pangkat(a, b, c)
    else:
        print(c)
        

angka=int(input('angka: '))
x=int(input('pangkat: '))
pangkat(angka, x)

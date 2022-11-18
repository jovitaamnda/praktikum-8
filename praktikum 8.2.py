# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:18:31 2022

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
pangkat(angka,x )

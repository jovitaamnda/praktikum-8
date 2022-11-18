# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:45:29 2022

@author: jovita amanda putri
"""

total = 0
itera = 1
jumlah = int(input("Masukkan Jumlah: "))

def penjumlahan ():
    global total, itera, jumlah
    angka = int(input(f"Masukkan Angka Ke-{itera}: "))
    total+=angka
    itera+=1
    if jumlah > 1:
        jumlah-=1
        print(total)
        penjumlahan()
    return total

print(penjumlahan())
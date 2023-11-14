import numpy as np
import pandas as pd
import os
from time import sleep
from klasifikasi import *

# Menentukan sisa saldo uang elektronik sehabis tol berdasarkan golongan dan gerbang akhir
# Definisi Fungsi
def sisasaldo(saldo,tarifharga):
    sisasaldo = saldo - tarifharga
    return sisasaldo
def isisaldo(saldo,jumlahisi):
    saldoakhir = saldo+jumlahisi
    return saldoakhir

Hgol = [[7500,14500,36500,41500],
         [11500,22000,54500,62000],
         [11500,22000,54500,62000],
         [15500,29000,72500,83000],
         [15500,29000,72500,83000]]

dataset = np.absolute([
    # p,l,t
    [7820,2100,3270],
    [4500,2000,2000],
    [5700,2300,2300],
    [11000,2500,2400],
    [12000,2500,2400],
    [16000,2500,2400]
])

arrGA = ["Jatinangor","Pamulihan","Sumedang","Cimalaka"]

# INPUT
os.system('cls')
print("GERBANG TOL OTOMATIS")
print("==============================================")
print("Penggolongan kendaraan")
p = int(input("panjang kendaraan (dalam milimeter): "))
l = int(input("lebar kendaraan (dalam milimeter): "))
t = int(input("tinggi kendaraan (dalam milimeter): "))
print("")
saldo = int(input("Masukkan saldo uang elektronik Anda: Rp"))
ukuran= [p,l,t]

gol = klasifikasi(dataset,ukuran)



# Proses

if(gol != 0):
    os.system('cls')
    print()
    print("GERBANG TOL OTOMATIS")
    print("==============================================")
    print("Selamat datang di tol Cileunyi.")
    print(f"Silahkan tap kartu uang elektronik Anda.")
    input("-> ")
    os.system('cls')
    # Anggap sudah di tap
    print()
    print("Gerbang tol dibuka")
    print()
    print(f"|==============================================|")
    print(f"                     Tol Cileunyi         ")
    print(f"                    Saldo Rp{saldo}         ")
    print(f"                    Golongan {gol}         ")
    print(f"|==============================================|")
    sleep(4)
    os.system('cls')
    # Anggap sudah sampai gerbang tol keluar
    print()
    print("GERBANG TOL OTOMATIS")
    print("==============================================")
    print()
    print("Masukkan gerbang tol keluar Anda: ")
    print("1. jatinangor") 
    print("2. pamulihan") 
    print("3. sumedang") 
    print("4. cimalaka")
    GA = int(input("--> "))
    hargatol = Hgol[gol-1][GA-1]
    print()
    print("Tap kartu elektronik Anda:")
    input("-> ")
    print()
    os.system('cls')

    while hargatol > saldo:
        # print("GERBANG TOL OTOMATIS")
        # print("==============================================")
        print(f"|==============================================|")
        print(f"        Saldo uang elektronik Anda kurang.")
        print(f"      Silahkan isi saldo uang elektronik Anda.")
        print(f"                 Jumlah pengisian: ")
        print(f"|==============================================|")
        saldotambah = int(input("Jumlah pengisian: Rp"))
        saldo = isisaldo(saldo,saldotambah)
        print()
        sleep(3)
        os.system('cls')
    saldo = sisasaldo(saldo,hargatol)
    print("GERBANG TOL OTOMATIS")
    print("==============================================")
    print(f"Gerbang tol keluar dibuka.")
    print()
    print(f"|======================================|")
    print(f"             CIleunyi-{arrGA[GA-1]}       ")
    print(f"                Golongan {gol}                ")
    print(f"               Biaya Rp{hargatol}            ")
    print(f"             Sisa Saldo Rp{saldo}            ")
    print(f"|======================================|")
    sleep(10)
    os.system('cls')
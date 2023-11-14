import math
import numpy as np

# # make matrix with numpy 
# gfg = np.absolute([[1,2,4]])
         
# # applying matrix.copy() method 
# geeks = gfg.copy() 
# geeks[0][1] = 0
# print(gfg)
# print(geeks)

def euclidean_distance(model, uji):
    sum = 0
    for i in range(len(uji)):
        sum += (uji[i] - model[i]) ** 2
    sum = math.sqrt(sum)
    return sum

def klasifikasi(model, uji):
    tabeljarak= model.copy()

    for i in range(len(model)):
        tabeljarak[i] = euclidean_distance(model[i], uji)
        
    # jarak = tabeljarak.copy()
    jarak = [0 for i in range (len(tabeljarak))]
    for i in range (len(tabeljarak)):
        jarak[i]=np.min(tabeljarak[i])

    indeks = np.argmin(jarak)

    if indeks == 0 or indeks == 1:
        golongan = 1
    elif indeks == 2:
        golongan = 2
    elif indeks == 3:
        golongan = 3
    elif indeks == 4:
        golongan = 4
    elif indeks == 5:
        golongan = 5
    

    # Output golongan kendaraan
    return golongan

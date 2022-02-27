from math import atan2, pi

# fungsi untuk menghitung determinan dari 3 titik
def determinan(titik1, titik2, titik3):
    return (titik1[0] * titik2[1]) + (titik1[1] * titik3[0]) + (titik2[0] * titik3[1]) - (titik3[0] * titik2[1]) - (titik3[1] * titik1[0]) - (titik2[0] * titik1[1])

# fungsi untuk mengembalikan nilai minimum dan maksimum dari suatu list titik
def maxmin(list_titik):
    minimum = list_titik[0]
    maximum = list_titik[0]
    
    for titik in list_titik:
        if(titik[0] <= minimum[0]):
            minimum = titik
        if(titik[0]) >= maximum[0]:
            maximum = titik
    return minimum,maximum

# fungsi untuk mencari sudut
def angle(A,B,C):
    Ax, Ay = A[0]-B[0], A[1]-B[1]
    Cx, Cy = C[0]-B[0], C[1]-B[1]
    a = atan2(Ay, Ax)
    c = atan2(Cy, Cx)
    if a < 0: a += pi*2
    if c < 0: c += pi*2
    return (pi*2 + c - a) if a > c else (c - a)

# fungsi untuk membagi 2 sisi kiri atau kanan dimana:
# kalo determinannya < 0 -> berada di sisi kiri
# kalo determinannya > 0 -> berada di sisi kanan
def bagiSisi(points,min,max):
    kiri = []
    kanan = []
    for titik in points:
        if(not((titik[0] == min[0]) and (titik[1] == min[1])) and not((titik[0] == max[0]) and (titik[1] == max[1]))):
            if(determinan(min,max,titik)>0):
                kanan.append(titik)
            if(determinan(min,max,titik)<0):
                kiri.append(titik)
                
    return kiri,kanan

def cariIndeks(titik,coordinate):
    i = 0
    for a in titik:
        if(coordinate[0] == a[0] and coordinate[1] == a[1]):
            return i
        else:
            i += 1
            
# Fungsi untuk menyatukan 2 buah list
def merge(list1, list2):
    for x in list2:
        list1.append(x)
    return list1

# melakukan Algoritma Divide and Conquer
# dengan membagi 2 sisi, kiri dan kanan
# lalu dilakukan fungsi quickhull kiri dan kanan (menyelesaikan permasalahan di dua sisi, kiri dan kanan)
def quickhull_kiri(kiri,min_absis,max_absis,titik):
    if(len(kiri) == 0):
        result = [[cariIndeks(titik,min_absis),cariIndeks(titik,max_absis)]]
        return result
    else:
        sudut = 0
        temp = kiri[0]
        for coordinate in kiri:
            if(sudut < angle(coordinate,min_absis,max_absis)):
                sudut = angle(coordinate,min_absis,max_absis)
                temp = coordinate
        kiri_baru1,_ = bagiSisi(kiri,min_absis,temp)
        kiri_baru2,_ = bagiSisi(kiri,temp,max_absis)
        # bagian melakukan rekursi sampai bagian kiri sampai habis
        result1 = quickhull_kiri(kiri_baru1,min_absis,temp,titik)
        result2 = quickhull_kiri(kiri_baru2,temp,max_absis,titik)
        return merge(result1, result2)
        
def quickhull_kanan(kanan,min_absis,max_absis,titik):
    if(len(kanan)==0):
        result = [[cariIndeks(titik,min_absis),cariIndeks(titik,max_absis)]]
        return result
    else:
        sudut = 0
        temp = kanan[0]
        for coordinate in kanan:
            if(sudut < angle(max_absis,min_absis,coordinate)):
                sudut = angle(max_absis,min_absis,coordinate)
                temp = coordinate
        _,kanan_baru1 = bagiSisi(kanan,min_absis,temp)
        _,kanan_baru2 = bagiSisi(kanan,temp,max_absis)
        # melakukan rekursi sampai bagian kanan sampai habis
        result1 = quickhull_kanan(kanan_baru1,min_absis,temp,titik)
        result2 = quickhull_kanan(kanan_baru2,temp,max_absis,titik)
        return merge(result1, result2)

# setelah melakukan quickhull pada masing masing sisi, maka dilakukan penggabungan(merge) antara
# quickhull kiri dan kanan
def myHull(titik):
    # mencari nilai max dan min masing masing absis
    # membagi sisi antara kiri dan kanan
    # melakukan rekursi antara quickhull kiri dan kanan
    # setelah selesai maka digabungkan (merge)
    result = []
    min_absis,max_absis = maxmin(titik)
    kiri,kanan = bagiSisi(titik,min_absis,max_absis)
    result_kiri = quickhull_kiri(kiri,min_absis,max_absis,titik)
    result_kanan = quickhull_kanan(kanan,min_absis,max_absis,titik)
    result = merge(result_kanan, result_kiri)
    return result
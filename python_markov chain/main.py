import pandas as pd
from openpyxl import load_workbook
import numpy as np
from scipy.linalg import solve

# Baca Data Excel
Data = pd.read_excel('Data.xlsx')

# Ekstrak data kolom kuantitas
df_data = Data["Kuantitas"]
print(df_data)

print("\n")

# # Drop missing values and reset index
# df_clean = df_data.dropna().reset_index(drop=True)

# Mencari nilai minimal, maksimal, range & jangkauan
nilai_min = df_data.min()
nilai_max = df_data.max()
nilai_range = nilai_max - nilai_min
nilai_jangkauan = nilai_range / 3

print("Min =", nilai_min)
print("Max =", nilai_max)
print("Range = ", nilai_range)
print("Jangkauan = ", nilai_jangkauan)

print("\n")

# Mencari nilai prediksi
Prediksi = []

for i in range (len(df_data)):
    if df_data[i] < 1212.33 :
        # Data['Prediksi'] = Prediksi.append('S')
        Prediksi.append('S')
    elif df_data[i] >= 1212.33 and df_data[i] < 2257.667 :
        # Data['Prediksi'] = Prediksi.append('C')
        Prediksi.append('C')
    elif df_data[i] >= 2257.667 :
        # Data['Prediksi'] = Prediksi.append('B')
        Prediksi.append('B')
print("Prediksi = ", Prediksi)

# Menghitung Jumlah Prediksi
jumlah_s, jumlah_c, jumlah_b = 0, 0, 0

for i in range(len(Prediksi)):
    Data['Prediksi'] = Prediksi
    if(Prediksi[i] == "S"):
        jumlah_s += 1
    elif(Prediksi[i] == "C"):
        jumlah_c += 1
    elif(Prediksi[i] == "B"):
        jumlah_b += 1

print("Jumlah S = ", jumlah_s)
print("Jumlah C = ", jumlah_c)
print("Jumlah B = ", jumlah_b)

total = jumlah_b + jumlah_c + jumlah_s
print("Total = ", total)

print("\n")

# Menghitung probabilitas awal
probabilitas_s = jumlah_s / total
probabilitas_c = jumlah_c / total
probabilitas_b = jumlah_b / total

print("Probabilitas S = ", probabilitas_s)
print("Probabilitas C = ", probabilitas_c)
print("Probabilitas B = ", probabilitas_b)

print("\n")

# Menghitung transisi
transis_ss, transis_sc, transis_sb = 0, 0, 0
transis_cs, transis_cc, transis_cb = 0, 0, 0
transis_bs, transis_bc, transis_bb = 0, 0, 0

for i in range(len(Prediksi) - 1):
    if Prediksi[i] == "S" and Prediksi[i + 1] == "S":
        transis_ss += 1
    elif Prediksi[i] == "S" and Prediksi[i + 1] == "C":
        transis_sc += 1
    elif Prediksi[i] == "S" and Prediksi[i + 1] == "B":
        transis_sb += 1
    elif Prediksi[i] == "C" and Prediksi[i + 1] == "S":
        transis_cs += 1
    elif Prediksi[i] == "C" and Prediksi[i + 1] == "C":
        transis_cc += 1
    elif Prediksi[i] == "C" and Prediksi[i + 1] == "B":
        transis_cb += 1
    elif Prediksi[i] == "B" and Prediksi[i + 1] == "S":
        transis_bs += 1
    elif Prediksi[i] == "B" and Prediksi[i + 1] == "C":
        transis_bc += 1
    elif Prediksi[i] == "B" and Prediksi[i + 1] == "B":
        transis_bb += 1

print("Transisi SS = ", transis_ss)
print("Transisi SC = ", transis_sc)
print("Transisi SB = ", transis_sb)

print("Transisi CS = ", transis_cs)
print("Transisi CC = ", transis_cc)
print("Transisi CB = ", transis_cb)

print("Transisi BS = ", transis_bs)
print("Transisi BC = ", transis_bc)
print("Transisi BB = ", transis_bb)

total_transisi = transis_ss + transis_sc + transis_sb + transis_cs + transis_cc + transis_cb + transis_bs + transis_bc + transis_bb
print("Total Transisi = ", total_transisi)

print("\n")

# Menghitung probabilitas setiap transisi
total_scb = transis_ss + transis_sc + transis_sb
total_csb = transis_cs + transis_cc + transis_cb
total_bsc = transis_bs + transis_bc + transis_bb

# print(total_scb)
# print(total_csb)
# print(total_bsc)

probabilitas_ss = transis_ss / total_scb
probabilitas_sc = transis_sc / total_scb
probabilitas_sb = transis_sb / total_scb

probabilitas_cs = transis_cs / total_csb
probabilitas_cc = transis_cc / total_csb
probabilitas_cb = transis_cb / total_csb

probabilitas_bs = transis_bs / total_bsc
probabilitas_bc = transis_bc / total_bsc
probabilitas_bb = transis_bb / total_bsc

print("probabilitas Transisi SS = ", probabilitas_ss)
print("probabilitas Transisi SC = ", probabilitas_sc)
print("probabilitas Transisi SB = ", probabilitas_sb)

print("probabilitas Transisi CS = ", probabilitas_cs)
print("probabilitas Transisi CC = ", probabilitas_cc)
print("probabilitas Transisi CB = ", probabilitas_cb)

print("probabilitas Transisi BS = ", probabilitas_bs)
print("probabilitas Transisi BC = ", probabilitas_bc)
print("probabilitas Transisi BB = ", probabilitas_bb)

print("\n")

# Membuat hasil dalam bentuk matrix
matrix_transisi = np.array([[probabilitas_ss, probabilitas_sc, probabilitas_sb], 
                            [probabilitas_cs, probabilitas_cc, probabilitas_cb],
                            [probabilitas_bs, probabilitas_bc, probabilitas_bb]])
print("Matrix Transisi: ")
print(matrix_transisi)

print("\n")


# Menghitung probabilitas panen dalam jumlah sedikit selama 3 tahun berturut-turut
prediksi_a = probabilitas_s * probabilitas_ss * probabilitas_ss
print("Probabilitas Jumlah (S) Selama 3 Tahun Berturut-Turut = ", prediksi_a)

# Menghitung probabilitas apabila saat ini sedikit maka peluang panen kondisi sedikit selama 2 tahun berturut-turut
prediksi_b = probabilitas_ss * probabilitas_ss * probabilitas_ss
print("Probabilitas Jumlah Saat Ini (S) Selama 2 Tahun Berturut-Turut = ", prediksi_b)

# Menghitung probabilitas apabila saat ini banyak maka peluang panen kondisi banyak selama 3 tahun berturut-turut
prediksi_c = probabilitas_bb * probabilitas_bb * probabilitas_bb * probabilitas_bb
print("Probabilitas Jumlah Saat Ini (S) Selama 2 Tahun Berturut-Turut = ", prediksi_c)

print("\n")

# Steady State

# Definisikan matriks awal
P_current = np.copy(matrix_transisi)
P_previous = np.zeros_like(matrix_transisi)

# Inisialisasi counter iterasi
iteration = 1

# Perulangan hingga mencapai konvergensi atau keadaan di mana matriks saat ini memiliki semua elemen yang sama dengan matriks sebelumnya
while True:
    P_previous = np.copy(P_current)
    P_current = np.dot(P_current, matrix_transisi)
    iteration += 1
    
    # Cetak matriks setelah setiap iterasi
    print("Iterasi", iteration-1)
    print(P_current)
    print()
    
    # Periksa konvergensi
    if np.array_equal(P_current, P_previous):
        break

# Cetak hasil matriks distribusi stasioner yang konvergen
print("Distribusi Stasioner (Konvergen) setelah", iteration-1, "iterasi:")
print(P_previous)
print("\n")

# Lanjutkan iterasi setelah mencapai matriks steady state
max_iterations = 6  # Jumlah iterasi tambahan yang diinginkan
for i in range(max_iterations):
    P_current = np.dot(P_current, matrix_transisi)
    iteration += 1

    # Cetak matriks setelah setiap iterasi tambahan
    print("Iterasi", iteration-1)
    print(P_current)
    print()

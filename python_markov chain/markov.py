import pandas as pd
import numpy as np

cuaca = pd.read_excel('cuaca.xlsx')
# print(cuaca)

# normalisasi untuk menghilangkan data yang nan ataupun yang tidak perlu di olah
df_cuaca = cuaca.drop('No', axis=1)
df_cuaca = df_cuaca.drop('Hari/waktu',axis=1)
# print(df_cuaca)
df_clean = df_cuaca.dropna()
# print(df_clean)  
# Mengubah nama kolom menjadi indeks bilangan bulat
df_clean.columns = range(df_clean.shape[1])
# print(df_clean)
df_reset = df_clean.reset_index()
# print(df_reset)
df_reset = df_reset.drop('index',axis=1)
print(df_reset)

print("\n")

# # df_transposed = df_reset.transpose()
# # print(df_transposed)

# menghitung data banyaknya label C, M, H
count_c = df_reset.applymap(lambda x: str(x).lower().count('c') if isinstance(x, str) else 0).sum().sum()
print("Jumlah Kemunculan C = ", count_c)
count_m = df_reset.applymap(lambda x: str(x).lower().count('m') if isinstance(x, str) else 0).sum().sum()
print("Jumlah Kemunculan M = ", count_m)
count_h = df_reset.applymap(lambda x: str(x).lower().count('h') if isinstance(x, str) else 0).sum().sum()
print("Jumlah Kemunculan H = ", count_h)

total_data = count_c+count_m+count_h
print("Total Data = ", total_data)

print("\n")

# menghitung peluang awal
p_c = count_c/total_data
print("Probablilitas Cerah = ", p_c)
p_m = count_m/total_data
print("Probablilitas Mendung = ", p_m)
p_h = count_h/total_data
print("Probablilitas Hujan = ", p_h)

print("\n")

count_cc = 0
for i in range(len(df_reset)):
    for j in range(len(df_reset.columns) - 1):
        if df_reset.iloc[i][j+1] == 'C' and df_reset.iloc[i][j+1] == 'M':
        # baca = df_reset.iloc[i, j]
        # if baca == 'C' and baca == 'C':
            count_cc += 1
print("count cc = ", count_cc)

# count_cc = 0
# for i in range(len(df_reset.columns)):
#     for j in range(len(df_reset)):
#         # baca = df_reset.iloc[i][j]
#         # if baca == 'H' and baca == 'C':
#         if df_reset.iloc[j][i] == 'C' and df_reset.iloc[j][i] == 'C':
#             count_cc += 1
# print("count cc =", count_cc)

#Menghitung keterkaitan antara jumlah angka 'C' dan 'C' berikutnya
# count_cc = 0
# for i in range(len(df_reset.columns)):
#     for j in range(len(df_reset)):
#         if i == 'C' and j == 'C':
#             count_cc += 1
#         # if df_reset.iloc[i][j] == 'C' and df_reset.iloc[i][j] == 'C':
#         #     count_cc += 1
#         # if df_reset.iloc[i][j] == 'C' and df_reset.iloc[i][j] == 'C':
#         #     count_cc += 1
# # Menampilkan hasil
# print("\nJumlah Kemunculan Pola 'C' ke 'C' Berikutnya:", count_cc)




# # for baris in range(len(df_reset)):
# #     for kolom in range(len(df_reset)):
        

# # menghitung data transisi nya

# Mengakses baris tertentu
# for baris in df_reset:
# baris = df_reset.loc[1][2]
# # print(baris)
# # baris_1 = df_reset.loc[1]
# # baris_2 = df_reset.loc[2]
# # baris_3 = df_reset.loc[3]
# count_cc = 0
# for baris in range(len(df_reset)):
#     for kolom in range(len(df_reset.columns)):
#         baca = df_reset.iloc[baris, kolom]
#         if df_reset.iloc[baca] == 'C' and df_reset.iloc[baca] == 'M':
#             count_cc += 1
# print("count cc = ", count_cc)





# Membaca data dalam baris secara menyamping
# for kolom in baris.index:
#     data = baris[kolom]
#     print(f"Data dalam kolom '{kolom}': {data}")

# for kolom in baris_1.index:
#     data = baris_1[kolom]
#     print(f"Data dalam kolom '{kolom}': {data}")
    
# for kolom in baris_2.index:
#     data = baris_2[kolom]
#     print(f"Data dalam kolom '{kolom}': {data}")


# for kolom in baris_3.index:
#     data = baris_3[kolom]
#     print(f"Data dalam kolom '{kolom}': {data}")


# # c-c
# # Menghitung keterkaitan antara jumlah angka 'C' dan 'C' berikutnya
# count_cc = 0
# for i in range(len(df_reset)):
#     if df_reset.iloc[0][i] == 'C' and df_reset.iloc[0][i+1] == 'C':
#         count_cc += 1
#     if df_reset.iloc[1][i] == 'C' and df_reset.iloc[1][i+1] == 'C':
#         count_cc += 1
#     if df_reset.iloc[2][i] == 'C' and df_reset.iloc[2][i+1] == 'C':
#         count_cc += 1
# # Menampilkan hasil
# print("\nJumlah Kemunculan Pola 'C' ke 'C' Berikutnya:", count_cc)

# # Menghitung keterkaitan antara jumlah angka 'C' ke 'M' berikutnya
# count_ch = 0
# for i in range(len(df_reset) - 1):
#     if df_reset.iloc[i][0] == 'C' and df_reset.iloc[i + 1][0] == 'H':
#         count_ch += 1
#     if df_reset.iloc[i][1] == 'C' and df_reset.iloc[i + 1][1] == 'H':
#         count_ch += 1
#     if df_reset.iloc[i][2] == 'C' and df_reset.iloc[i + 1][2] == 'H':
#         count_ch += 1

# # Menampilkan hasil
# print("Jumlah Kemunculan Pola 'C' ke 'H' Berikutnya:", count_ch)

# count_ch = 0
# for i in range(len(df_reset) - 1):
#     if df_reset.iloc[i][0] == 'C' and df_reset.iloc[i + 1][2] == 'H':
#         count_ch += 1

# # Menampilkan hasil
# print("Jumlah Kemunculan Pola 'C' ke 'H' Berikutnya:", count_ch)

# list_cc = []
# count_cc = 0
# for i in range(len(df_reset) - 1):
#     if df_reset.iloc[i][0] == 'C' and df_reset.iloc[i + 1][2] == 'C':
   
#         count_cc += 1
#         list_cc.append(count_cc)
#     else:
#         df_reset.iloc[i][0] != 'C' and df_reset.iloc[i + 1][2] != 'C'
#         count_cc = count_cc

# # Menampilkan hasil
# print("Jumlah Kemunculan Pola 'C' ke 'C' Berikutnya:", count_cc)

# count_cc = 0
# is_pattern = False

# for i in range(len(df_reset) - 1):
#     for j in range(len(df_reset.columns) - 1):
#         if df_reset.iloc[i][j] == 'C' and df_reset.iloc[i + 1][j + 1] == 'C':
#             if not is_pattern:
#                 is_pattern = True
#                 count_cc += 1
#             else:
#                 count_cc += 1
#         elif df_reset.iloc[i][j] != 'C' or df_reset.iloc[i + 1][j + 1] != 'C':
#             is_pattern = False

# # Menampilkan hasil
# print("Jumlah Kemunculan Pola 'C' ke 'C':", count_cc)







# count_cm = 0
# for i in range(len(df_reset) - 1):
#     for j in range(len(df_reset.columns)):
#         if df_reset.iloc[i][j] == 'C' and df_reset.iloc[i + 1][j] == 'M':
#             count_cm += 1
# print("\nJumlah Kemunculan Pola 'C' ke 'M' Berikutnya:", count_cm)

# # Inisialisasi variabel total_count_cm
# total_count_cm = 0

# # Perulangan untuk setiap kolom dalam DataFrame
# for col in df_reset.columns:
#     count_cm = 0
#     for i in range(len(df_reset) - 1):
#         if df_reset[col].iloc[i] == 'C' and df_reset[col].iloc[i + 1] == 'M':
#             count_cm += 1
#     total_count_cm += count_cm

# # Menampilkan hasil
# print("\nJumlah Kemunculan Pola 'C' ke 'M' pada setiap kolom:")
# for col in df_reset.columns:
#     count_cm = 0
#     for i in range(len(df_reset) - 1):
#         if df_reset[col].iloc[i] == 'C' and df_reset[col].iloc[i + 1] == 'M':
#             count_cm += 1
#     print("Kolom", col, ":", count_cm)

# print("\nTotal Jumlah Kemunculan Pola 'C' ke 'M':", total_count_cm)




# markov = [[0] * 2 for i in range(2)]
# markov[0][0] = 0.5
# markov[0][1] = 0.5
# markov[1][0] = 0.2
# markov[1][1] = 0.8

# for i in range(2):
#     for j in range(2):
#         hasil = markov[i][j]*markov[i][j]
#         markov.append(hasil)
# print(markov)
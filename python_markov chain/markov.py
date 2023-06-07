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
# print(df_reset)

# menghitung data banyaknya label C, M, H
count_c = df_reset.applymap(lambda x: str(x).lower().count('c') if isinstance(x, str) else 0).sum().sum()
print(count_c)
count_m = df_reset.applymap(lambda x: str(x).lower().count('m') if isinstance(x, str) else 0).sum().sum()
print(count_m)
count_h = df_reset.applymap(lambda x: str(x).lower().count('h') if isinstance(x, str) else 0).sum().sum()
print(count_h)

total_data = count_c+count_m+count_h
print(total_data)

# menghitung peluang awal
p_c = count_c/total_data
# print(p_c)
p_m = count_m/total_data
# print(p_m)
p_h = count_h/total_data
# print(p_h)

# menghitung data transisi nya

# c-c
# Menghitung keterkaitan antara jumlah angka 'C' dan 'C' berikutnya
count_cc = 0
for i in range(len(df_reset) - 1):
    if df_reset.iloc[i][0] == 'C' and df_reset.iloc[i + 1][0] == 'C':
        count_cc += 1
    if df_reset.iloc[i][1] == 'C' and df_reset.iloc[i + 1][1] == 'C':
        count_cc += 1
    if df_reset.iloc[i][2] == 'C' and df_reset.iloc[i + 1][2] == 'C':
        count_cc += 1
# Menampilkan hasil
print("\nJumlah Kemunculan Pola 'C' ke 'C' Berikutnya:", count_cc)

# Menghitung keterkaitan antara jumlah angka 'C' ke 'M' berikutnya
count_cm = 0
for i in range(len(df_reset) - 1):
    if df_reset.iloc[i][0] == 'C' and df_reset.iloc[0][i + 1] == 'H':
        count_cm += 1
    if df_reset.iloc[i][1] == 'C' and df_reset.iloc[1][i + 1] == 'H':
        count_cm += 1
    if df_reset.iloc[i][2] == 'C' and df_reset.iloc[2][i + 1] == 'H':
        count_cm += 1
# Menampilkan hasil
print("\nJumlah Kemunculan Pola 'C' ke 'M' Berikutnya:", count_cm)

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
import pandas as pd
from openpyxl import load_workbook

# Baca Data Excel
Data = pd.read_excel('Data.xlsx')

# Ekstrak data kolom kuantitas
df_data = Data["Kuantitas"]
print(df_data)

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
    Data['Prediksi'] = Prediksi[i]


# Menghitung nilai prediksi

df_data = Data["Prediksi"]
print(df_data)

# for i in range(len(Prediksi)):
#     Data['Prediksi'] = Prediksi[i]
#     # Data.insert(2, 'Prediksi', [Prediksi[i]])

# print(Data)
# # Add a new column using square bracket notation
# Data['Prediksi'] = for i in range (len(Prediksi))

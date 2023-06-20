# import numpy as np

# # Matriks transisi contoh
# matrix_transisi = np.array([[0.5, 0.2], [0.3, 0.5]])

# # Melakukan transpose matriks transisi
# matrix_transpose = np.transpose(matrix_transisi)

# # Menginisialisasi matriks baru
# new_matrix = np.zeros_like(matrix_transisi)

# for i in range(100):
#     new_matrix = np.dot(matrix_transisi, matrix_transpose)
#     if np.allclose(new_matrix, matrix_transpose):
#         print("Berhasil pada iterais ", i)
#         print(new_matrix)
#         break
#     matrix_transpose = new_matrix

# else:
#     print("Tidak konvergen ke steady state dalam jumlah iterasi maksimum.")


import numpy as np

# Matriks transisi contoh
matrix_transisi = np.array([[0.5, 0.2], [0.3, 0.5]])

# Melakukan transpose matriks transisi
matrix_transpose = np.transpose(matrix_transisi)

# Menginisialisasi matriks baru
new_matrix = np.zeros_like(matrix_transisi)

for i in range(1000):
    new_matrix = np.dot(matrix_transisi, matrix_transpose)
    if np.array_equal(new_matrix, matrix_transpose):
        print("Berhasil")
        print(new_matrix)
        break
    else:
        matrix_transpose = new_matrix

else:
    print("Tidak konvergen ke steady state dalam jumlah iterasi maksimum.")

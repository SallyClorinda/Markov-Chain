import numpy as np

# Matriks transisi contoh
matrix_transisi = np.array([[0.5, 0.2], [0.3, 0.5]])

# Melakukan transpose matriks transisi
matrix_transpose = np.transpose(matrix_transisi)
print(matrix_transpose)

for i in range(1, 100):
    new_matrix = matrix_transisi.dot(matrix_transpose)
    if np.array_equal(new_matrix, matrix_transpose):
        print("Berhasil Pada indeks ke", i)
        print(new_matrix)
        break
    matrix_transpose = new_matrix

else:
    print("Tidak konvergen ke steady state dalam jumlah iterasi maksimum.")

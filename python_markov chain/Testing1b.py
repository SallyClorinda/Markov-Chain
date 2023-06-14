import numpy as np

# Definisikan matriks transisi P
P = np.array([[0.88888889, 0.05555556, 0.05555556],
                [0.5,        0.5,         0       ],
                [1,         0,         0       ]])

# Definisikan matriks awal
P_current = np.copy(P)
P_previous = np.zeros_like(P)

# Inisialisasi counter iterasi
iteration = 1
n = 1

# Toleransi untuk perbedaan antara matriks saat ini dan matriks sebelumnya
tolerance = 1e-5

# Perulangan hingga mencapai konvergensi atau keadaan di mana matriks saat ini memiliki semua elemen yang sama dengan matriks sebelumnya
while np.max(np.abs(P_current - P_previous)) > tolerance:
    P_previous = np.copy(P_current)
    P_current = np.dot(P_current, P)
    iteration += 1
    
    # Cetak matriks setelah setiap iterasi
    print("Iterasi", iteration-1)
    print(P_current)
    print()

# Cetak hasil matriks distribusi stasioner yang konvergen
print("Distribusi Stasioner (Konvergen) setelah", iteration-1, "iterasi:")
print(P_previous)

# Lanjutkan iterasi setelah mencapai matriks steady state
max_iterations = 10  # Jumlah iterasi tambahan yang diinginkan
for i in range(max_iterations):
    P_current = np.dot(P_current, P)
    iteration += 1

    # Cetak matriks setelah setiap iterasi tambahan
    print("Iterasi", iteration-1)
    print(P_current)
    print()

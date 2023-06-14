import numpy as np

# Matriks transisi
transition_matrix = np.array([[0.88888889, 0.05555556, 0.05555556],
                             [0.5, 0.5, 0.],
                             [1., 0., 0.]])

# Inisialisasi vektor awal
current_state = np.array([0.25, 0.25, 0.5])

# Toleransi untuk kondisi steady state
tolerance = 1e-6

# Iterasi hingga mencapai kondisi steady state
while True:
    # Menghitung next_state dengan mengalikan current_state dengan transition_matrix
    next_state = np.dot(current_state, transition_matrix)

    # Memeriksa apakah perbedaan absolut antara next_state dan current_state kurang dari toleransi
    if np.max(np.abs(next_state - current_state)) < tolerance:
        break

    # Memperbarui current_state dengan next_state
    current_state = next_state

# Menampilkan nilai steady state
print("Nilai steady state:")
print(current_state)

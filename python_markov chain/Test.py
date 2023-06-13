import pandas as pd

# Membuat DataFrame dari data
data = [['C', 'C', 'C'],
        ['C', 'C', 'M'],
        ['C', 'C', 'H'],
        ['C', 'C', 'M'],
        ['C', 'C', 'C'],
        ['C', 'C', 'C'],
        ['C', 'C', 'C'],
        ['C', 'C', 'C'],
        ['C', 'C', 'M'],
        ['C', 'C', 'C'],
        ['C', 'C', 'M'],
        ['C', 'C', 'C'],
        ['C', 'C', 'M']]

df = pd.DataFrame(data)

# Menambahkan index pada DataFrame
df.index = df.index + 1

# Memberi nama kolom
df.columns = ['1', '2', '3']

# Menampilkan DataFrame
print(df)
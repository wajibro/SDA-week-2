# Buat Matriks random 10x10 dengan elemen 1 - 10

import numpy as np

x = np.random.randint(1,11,100)
x = x.reshape(10,10)

print('Ditemukan elemen 5' if 5 in x else 'Tidak ditemukan elemen 5')
print(f'Ada {np.count_nonzero(x == 5)} elemen 5')
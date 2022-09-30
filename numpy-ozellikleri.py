# ndim = boyut sayısı
# shape = boyut bilgisi
# size = toplam eleman sayısı
# dtype = array veri tipi

import numpy as np

a = np.random.randint(0,10,10)

print(a)

print(a.ndim)

print(a.shape)

print(a.size)

print(a.dtype)

b = np.random.randint(10, size = (3,5))

print(b)

print(b.ndim)

print(b.shape)

print(b.size)

print(b.dtype)
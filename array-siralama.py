import numpy as np

v = np.array([3,5,2,1])

print(v)

print(np.sort(v))

v.sort()

print(v)

# iki boyutlu array sıralama

m = np.random.randint(0,10,(5,5))

print(m)

print(np.sort(m, axis=0))

print(np.sort(m, axis=1))
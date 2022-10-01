import numpy as np

a = np.arange(20,30)

print(a)

print(a[0:3])

print(a[:3])

print(a[3:])

print(a[1::2])

# iki boyutlu arrayler

m = np.random.randint(10, size=(5,5))

print(m)

print(m[:,0])

print(m[:,3])

print(m[0:3,:])

print(m[0,:])
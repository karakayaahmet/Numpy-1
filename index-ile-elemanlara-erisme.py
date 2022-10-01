import numpy as np

a = np.random.randint(0,10, 10)

print(a)

print(a[0])

print(a[-2])

a[0] = 20

# iki boyutlu arraylerde indexleme

m = np.random.randint(0,10,(3,5))

print(m)

print(m[0,0])

m[3,3] = 12

print(m[3,3])


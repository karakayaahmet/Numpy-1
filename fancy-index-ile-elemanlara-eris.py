import numpy as np

a = np.random.randint(0,30,size=10)

print(a[1]) # 3

print(a[3]) # 9

print(a[5]) # 12

print([a[1],a[3],a[5]])

# fancy index

al_getir = [1,3,5]

print(a[al_getir])

# iki boyutta fancy

m = np.arange(9).reshape(3,3)

print(m)

satir = np.array([0,1])

sutun = np.array([1,2])

print(m[satir,sutun])
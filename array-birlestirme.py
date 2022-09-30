import numpy as np

x = np.array([1,2,3,4])
y = np.array([2,3,5,6])

print(np.concatenate([x,y]))

z = np.array([3,4,5,6])

print(np.concatenate([y,z,x]))

# iki boyut

a = np.array([[1,2,3],[4,5,6]])

print(a)

print(np.concatenate([a,a]))

print(np.concatenate([a,a], axis=0)) #satır bazında birleştirme

print(np.concatenate([a,a], axis=1)) #sütun bazında birleştirme
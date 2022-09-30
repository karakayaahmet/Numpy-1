import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])

print(np.split(x,[3,5]))

a,b,c = np.split(x,[3,5])

print(a) # ilk parça

print(b) # ikinci parça

print(c) # son parça

# iki boyutlu ayırma

m = np.arange(16).reshape(4,4)

print(m)

print(np.vsplit(m,[2]))

alt,ust = np.vsplit(m,[2])

print(alt)

print(ust)

sag,sol = np.hsplit(m,[2])

print(sag)

print(sol)
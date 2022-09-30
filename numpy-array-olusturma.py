import numpy as np

print(np.array([1,2,3,5,0]))

print(np.array([1,3,5,6], dtype="float"))

# sıfırdan array oluşturma

print(np.zeros(10, dtype=int))

print(np.ones(10))

print(np.ones((3,3), dtype=int ))

print(np.full((3,6), 3))

print(np.arange(0,20,2))

print(np.linspace(0,5,10))

print(np.random.normal(10,3,(3,3)))

print(np.random.randint(0,50,(6,4)))
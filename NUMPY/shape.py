import numpy as np

a = np.floor(10*np.random.random((3,4)))

print(a)
print(a.shape)
print()

a = a.ravel()
print(a)
print(a.shape)
print()

a = a.reshape(2,6)
print(a)
print()
print(a.T)
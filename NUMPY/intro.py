import numpy as np

list = [[21,32,35],[67,72,87],[92,11,12]]
print(list)
print(type(list))
print()

arr = np.arange(15)
print(arr)
print(type(arr))
print()

arr = arr.reshape(3,5)
print(arr)
print(arr.ndim)
print()

arr2 = np.arange(10)
print(arr2)
print(arr2.shape)
print(arr2.ndim)
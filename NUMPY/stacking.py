import numpy as np

a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))
print(a)
print(b)
print()

c = np.vstack((a,b))
print("vstack:")
print(c)
print()

d = np.hstack((a,b))
print("hstack:")
print(d)
print()

# copying
e = a.copy()
print("a:\n" + str(a))
print("e:\n" + str(e))
e[0] = 100
print("\na:\n" + str(a))
print("e:\n" + str(e))
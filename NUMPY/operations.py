import numpy as np


a = np.array([20,30,40,50])
b = np.arange(4)
print(a)
print(b)
print("-_________________")
c = a-b
print(c)
print()

print(c<30)
print()

print("a*b: " + str(a*b))
print("a@b: " + str(a@b))
print("a.dot(b): "+ str(a.dot(b)))
print()

f = np.ones((2,4))
g = np.zeros((2,4))
print("f: " + str(f))
print("g: " + str(g))
print()

h = np.random.random((2,4))
print("h: " + str(h))
print()

i = np.sum(b)
print(i)
print(b.sum())
print()

print(np.max(h))
print(np.min(h))
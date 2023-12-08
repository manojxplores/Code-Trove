import numpy as np

a = np.array([1, 2, 3])
print(a)

print(a.shape, a[0], a[2])

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0, 1])

a = np.zeros((2, 2))
print(a)
b = np.ones((2, 2))
print(b)
c = np.full((2, 2), 7)
print(c)
e = np.random.random((2, 2))
print(e)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 3, 2, 1], [2, 5 ,3, 2]])
print(a.shape)

b = a[1:3, 1:3]
print(b)
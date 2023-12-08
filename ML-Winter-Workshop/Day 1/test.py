import numpy as np

b = np.array([[1, 2, 3], [3, 4, 6], [3, 7, 8]])
a = np.array([[1, 2, 3]])
print(a.shape, b.shape)
c = a*b
print(c.shape)

a = np.random.randn(12288, 150)
b = np.random.randn(150, 45)

print(a.shape, b.shape)
c = np.dot(a, b)
print(c.shape)
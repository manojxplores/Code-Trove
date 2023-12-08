# Tensors
import numpy as np
import torch

# a = [[1, 2], [3, 4]]
# x_data = torch.tensor(a)

# from a numpy array
np_array = np.array([[2, 3], [3, 4]])
x_data = torch.from_numpy(np_array)


# from another tensor
# x_ones = torch.ones_like(x_data)
# x_rand = torch.rand_like(x_data, dtype=torch.float)

rand_tensor = torch.rand((3,2))
ones_tensor = torch.ones((3, 2))
zeros_tensor = torch.zeros((3, 2))

print(rand_tensor.shape, rand_tensor.dtype, rand_tensor.device)

test = torch.ones((4, 4))
test[:, 1] = 0

# joining tensors
# t1 = torch.cat([rand_tensor, zeros_tensor, ones_tensor], dim =1)
'''
tensor.mul(tensor) --->element-wise product
tensor.matmul(tensor) --->matrix-multiplication
'''
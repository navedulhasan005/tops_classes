import numpy as np

array1 = np.zeros((2, 2, 2, 2))

array2 = np.ones((2, 2, 2, 2))

# print(four_d_array1)
# print(four_d_array2)
a = np.stack((array1, array2), axis=2)
print(a)
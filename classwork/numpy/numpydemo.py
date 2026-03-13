import numpy as np

# print(np.__version__)
# a = np.array(40)

# a = np.array([1,2,3,4,5,6],ndmin=3)
# print(a.ndim)

# a = np.array([10,20,30,40,50,60])
# print(a[-1])
# print(a[1:5])

# a = np.array([[1,2,3],[4,5,6]])
# print(a[2,1:3])


# a = np.array([10,20,30,40,50,60])
# b = a.copy()
# c = a.view()
# a[1] = 1000
# print(b)

# print(b.base)
# print(c.base)

# b[1] = 5000
# print(b)
# print(a)

# a = np.array([1,2,3,4,5,6,7,8])
# n = a.reshape(2,4)
# print(n)

# a = np.array([[10,20,30],[40,50,60]])
# k = a.reshape(-1)
# print(k)

# for i in a:
#     for l in i:
#         print(l)

# for x in np.nditer(a):
#     print(x)


# a = np.array([10,20,30])
# b = np.array([40,50,60])
# x = np.concatenate((a,b))
# print(x)


# a = np.array([[10,20,30],[40,50,60]])
# b = np.array([[1,2,3],[4,5,6]])
# x = np.concatenate((a,b),axis=1)
# print(x)


# a = np.array([[[10,20,30,4],[40,50,60,4],[70,80,90,4]],[[10,20,30,4],[40,50,60,4],[70,80,90,4]]])
# b = np.array([[[1,2,3,5],[4,5,6,6],[7,8,9,5]],[[1,2,3,5],[4,5,6,6],[7,8,9,5]]])

# a = np.array([[10,20,30],[40,50,60]])
# b = np.array([[1,2,3],[4,5,6]])

# x = np.stack((a,b),axis=2)
# print(x)


# 10 20 30
# 40 50 60

# 1 2 3
# 4 5 6


# a = np.array([
#     [
#         [
#             [1,2],
#             [3,4]
#         ],
#         [
#             [10,20],
#             [30,40]
#         ]
#     ],
#     [
#         [
#             [100,200],
#             [300,400]
#         ],
#         [
#             [1000,2000],
#             [3000,4000]
#         ]
#     ]
# ])

# b = np.array([
#     [
#         [
#             [1,2],
#             [3,4]
#         ],
#         [
#             [10,20],
#             [30,40]
#         ]
#     ],
#     [
#         [
#             [100,200],
#             [300,400]
#         ],
#         [
#             [1000,2000],
#             [3000,4000]
#         ]
#     ]
# ])


a = np.array([[[[10,20,30],
              [40,50,60]],

              [[10,20,30],
              [40,50,60]]],
              
              [[[10,20,30],
              [40,50,60]],

              [[10,20,30],
              [40,50,60]]]])

print(a.sum(axis=2))

# array1 = np.zeros((2, 2, 2, 2))

# array2 = np.ones((2, 2, 2, 2))

# print(four_d_array1)
# print(four_d_array2)
# a = np.stack((array1, array2), axis=2)
# print(a)
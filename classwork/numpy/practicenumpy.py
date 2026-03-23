import numpy as np 

a = np.array([
                [1,5,7],
                [9,8,7]
            ])

b = np.array([
                [8,4,3],
                [5,9,1] 
            ])

# d = np.concatenate((a,b),axis=1)
# c = np.stack((a,b),axis=1)
# print(d)
# print(c)

c = np.sum((a,b),axis=1)
# c = np.add(a,b)
print(c)


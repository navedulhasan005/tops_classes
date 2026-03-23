"""41)Write a Python program to check whether a list contains a sub list"""

a = [5, 6, 3, 8, 2, 1, 7, 1]
b = [8, 2, 1]
c = [10,39,39,37]

result = str(b)[1:-1] in str(a)[1:-1]

print(result)
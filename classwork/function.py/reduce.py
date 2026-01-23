from functools import reduce
l = [30,24,26,6,8,87,9,67,57]

k = reduce(lambda a,b: a if a > b else b, l)
print(k)

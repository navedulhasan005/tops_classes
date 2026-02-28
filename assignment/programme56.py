"""56)Write a Python program to map two lists into a dictionary 
Sample output: Counter."""

l1 = ['a', 'b', 'c', 'd']
l2 = [400, 400, 300, 400]

d = map(lambda x, y: (x, y), l1, l2)
print(dict(d))
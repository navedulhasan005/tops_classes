"""57)Write a Python program to find the highest 3 values in a dictionary."""

# l = [30,24,26,6,8,87,9,67,57]
# k = reduce(lambda a,b: a if a > b else b, l)
# print(k)

l = {"a":30,"b":24,"c":26,"d":6,"e":8,"f":87,"g":9,"h":67,"i":57}

k = sorted(l.values(), reverse=True)[:3]
print(k)
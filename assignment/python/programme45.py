"""45)Write a Python program to unzip a list of tuples into individual lists."""

l = [(10,20,30),("Hello","Python","World")]

result = list(zip(*l))
print(result)

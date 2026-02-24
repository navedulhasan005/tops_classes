"""46)Write a Python program to convert a list of tuples into a dictionary"""

list = [(10,20,30),("Hello","Python","World","Hello")]

result = dict(zip(*list))
print(result)

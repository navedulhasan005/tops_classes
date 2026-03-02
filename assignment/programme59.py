"""59)Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string"""

str = "Navedul Hasan"

d = {}
for i in str:
    # d[i] = d.get(i, 0) + 1
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
"""40)Write a Python program to get unique values from a list"""

list1 = [1, 2, 3, 4, 4, 5, 5, 6]
for i in list1:
    if list1.count(i) == 1:
        print(i)


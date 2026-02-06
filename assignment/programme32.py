"""32)Write a Python program to remove duplicates from a list form original list"""

list1 = [10, 20, 30, 40, 50, 10,]
list2 = []
for i in list1:
    if list1.count(i) > 1:
        list2.append(i)
print("Original list:", list1)
print("List after removing duplicates:", list2)
 
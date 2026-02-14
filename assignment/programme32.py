"""32)Write a Python program to remove duplicates from a list form original list"""

list1 = [10, 20, 30, 40, 50, 10, 10, 100]
print("Original list:", list1)
for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)

print("List after removing duplicates:", list1)

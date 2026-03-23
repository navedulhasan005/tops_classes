"""36) Write a Python function that takes a list and returns a new list with 
unique elements of the first list."""

list1 = [1, 2, 3, 4, 4, 5, 5, 6]
def function(lst):
    return list(set(lst))

result = function(list1)
print(result)
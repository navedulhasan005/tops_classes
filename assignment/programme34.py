"""34) Write a Python function that takes two lists and returns true if they 
have at least one common member."""

list1 = [1, 2, 3, 4]
list2 = [5, 1, 7, 8]
def function(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

result = function(list1, list2)
print(result)


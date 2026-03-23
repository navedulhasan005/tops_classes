"""62)Write a Python function to check whether a number is in a given range"""

n = 2
def func(start, end):
    if n in range(start,end):
        return True
    else:
        return False

result = func(4,10)
print(result)
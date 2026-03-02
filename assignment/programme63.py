"""63)Write a Python function to check whether a number is perfect or not"""

def func(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

result = func(6)
print(result)
"""6)Write a Python program to get the Fibonacci series of given range."""

number = int(input("Enter the number: "))
i = 0
j = 1
c = 0 
print(i, j, end=' ')
for k in range(number):
    c = i + j
    print(c, end=' ')
    i = j
    j = c
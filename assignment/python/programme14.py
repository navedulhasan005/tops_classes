"""14)Write a python program to sum of the first n positive integers."""
n = int(input("Enter a positive integer: "))
sum = n * (n + 1) // 2
print("Sum of the first", n, "positive integers:", sum)
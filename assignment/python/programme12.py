"""12) Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero. """

number1 = int(input("Number1:"))
number2 = int(input("Number2:"))
number3 = int(input("Number3:"))

sum = number1 + number2 + number3

if number1 == number2 or number2 == number3 or number1 == number3:
    print("Sum: 0")
else:
    print(sum)
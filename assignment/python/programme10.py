"""10) Write a Python program to find whether a given number is even 
or odd, print out an appropriate message to the user."""

number = int(input("Enter the number: "))

if number % 2 == 0:
    print(f"{number} Is Even Number.")
else:
    print(f"{number} Is Odd Number.")
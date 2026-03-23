"""16) Write a Python program to count the number of characters 
(character frequency) in a string"""
str = input("Enter a string: ")

for char in str:
    count = str.count(char)
    print(f"{char}' occurs {count}")
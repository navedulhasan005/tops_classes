"""18)Write a Python program to count occurrences of a substring in a string"""
str = input("Enter a string: ")
sub_str = input("Enter a substring: ")
count = str.count(sub_str)
print(f"substring '{sub_str}' occurs {count} times.")
"""64)Write a Python function that checks whether a passed string is 
palindrome or not"""
str = input("Enter a string:")
def func(str):
    if str == str[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

func(str)

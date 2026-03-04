"""64)Write a Python function that checks whether a passed string is 
palindrome or not"""

def func(str):
    if str == str.reverse():
        print("Palindrome")
    else:
        print("Not Palindrome")


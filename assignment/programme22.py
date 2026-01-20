"""22) Write a Python function to reverses a string if its length is a multiple 
of 4."""

def reverse():
    string = input("Enter a string: ")
    if len(string) % 4 == 0:
        reversed_string = string[::-1]
        print("Reversed string:", reversed_string)
reverse()    
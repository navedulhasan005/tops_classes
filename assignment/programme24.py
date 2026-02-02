"""24)Write a Python function to insert a string in the middle of a string."""

def insert(str, str1):
    str = input("Enter the original string: ")
    str1 = input("Enter the string to insert: ")
    s = len(str) // 2
    new_str = str[:s] + str1 + str[s:]
    return new_str

result = insert(" ", " ")
print("String after insertion:", result)
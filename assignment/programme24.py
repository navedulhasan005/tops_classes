"""24)Write a Python function to insert a string in the middle of a string."""

def insert_in_middle(original_str, str_to_insert):
    str = input("Enter the original string: ")
    str1 = input("Enter the string to insert: ")
    mid_index = len(str) // 2
    new_str = str[:mid_index] + str1 + str[mid_index:]
    return new_str

result = insert_in_middle("", "")
print("String after insertion:", result)
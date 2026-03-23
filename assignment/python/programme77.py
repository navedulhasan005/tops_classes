"""77)Write a Python program to read a file line by line store it into a variable."""

file_content = ""

with open('demofile.txt', 'r') as file:
        file_content = file.read()

print(file_content)

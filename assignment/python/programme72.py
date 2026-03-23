"""72)Write a Python program to read an entire text file."""

with open('demofile.txt', 'r') as file:
    content = file.read()
    print(content)
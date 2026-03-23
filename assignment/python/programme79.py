"""79)Write a Python program to count the number of lines in a text file"""

with open('demofile.txt', 'r') as file:
    text = file.read()
line = len(text.splitlines())
print(line)
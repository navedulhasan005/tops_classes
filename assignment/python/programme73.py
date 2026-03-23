"""73)Write a Python program to append text to a file and display the text."""

with open("demofile.txt", "a") as file:
    file.write("\nThis is an appended line.\n")

with open("demofile.txt", "r") as file:
    content = file.read()
    print(content)
"""76)Write a Python program to read a file line by line and store it into a list"""
list = []
with open("demofile.txt", "r") as file:
    for line in file:
        list.append(line.strip())
print(list)
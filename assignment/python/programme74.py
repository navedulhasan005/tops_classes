"""74)Write a Python program to read first n lines of a file."""
n = 5
with open("demofile.txt", "r") as file:
    for _ in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end="")
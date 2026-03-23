"""75)Write a Python program to read last n lines of a file."""
n = 5
with open("demofile.txt", "r") as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]
    for line in last_n_lines:
        print(line, end="")
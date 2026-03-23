"""82)Write a Python program to copy the contents of a file to another file."""

with open("demofile.txt") as file:
    with open("copy_content.txt", "w") as file2:
        for line in file:
            file2.write(line)
print("Contents have been copied to copy_content.txt")

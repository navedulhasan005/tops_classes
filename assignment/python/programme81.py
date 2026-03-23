"""81)Write a Python program to write a list to a file."""

list = ['apple', 'banana', 'cherry', 123, 45.67]
with open("demofile.txt","w") as file:
    file.write("\n".join(str(item) for item in list))
    print("List has been written to the file.")


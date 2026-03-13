"""81)Write a Python program to write a list to a file."""

list = ['apple', 'banana', 'cherry', 123, 45.67]
with open("demofile.txt","w") as file:
    for item in list:
        file.write(f"{item}\n")
print(item)


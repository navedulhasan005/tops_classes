"""50)Write a Python script to check if a given key already exists in a 
dictionary."""

dict = {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

key = 'city'

if key in dict:
    print(f"Key exists in the dictionary.")
else:
    print(f"Key does not exist in the dictionary.")
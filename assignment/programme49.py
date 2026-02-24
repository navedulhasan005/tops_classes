"""49)Write a Python script to concatenate following dictionaries to create 
a new one."""

dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}

dict2 = {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

result = dict1.copy()
result.update(dict2)

print(result)
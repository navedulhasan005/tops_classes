"""48)Write a Python script to sort (ascending and descending) a 
dictionary by value."""

d = {"a": 3, "b": 1, "c": 2}

sorted_dict = sorted(d.items(), key=lambda item: item[1])

print(dict(sorted_dict))




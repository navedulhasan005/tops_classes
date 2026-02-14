import re

# k = re.match("Sun","Sun rises in east")
# l = re.search("S","Sun rises in east")
# m = re.findall("s","Sun rises in east")

# print(k)
# print(l)
# print(m)
# o = re.finditer("s","Sun rises in east")

# print(next(o))
# print(next(o))
# print(next(o))

# k = re.findall("P.t","Hello Python Hello World")
# k = re.search("^H","Hello Python Hello World")
# k = re.search("World$","Hello Python Hello World")
# k = re.search("He*l","Hello Python Hello World")
# k = re.search("He+l","Hello Python Hello World")
# k = re.search("He?l","Hello Python Hello World")

# k = re.findall("[A-Z]","Hello World Hello Pyhton")
# k = re.findall(r"\d","Hello World Hello Pyhton 12 32")
# k = re.findall(r"\D","Hello World Hello Pyhton 12 32")
# k = re.findall(r"\w","Hello World Hello Pyhton 12 !@ 32")
# k = re.findall(r"\W","Hello World Hello Pyhton 12 !@ 32")
# k = re.findall(r"\S","Hello World Hello Pyhton 12 !@ 32")
# k = re.findall(r"\s","Hello World Hello Pyhton 12 !@ 32")
# k = re.search(r"\Bued","The certificate was issued")
k = re.search(r"\d{,10}","8239899067")


print(k)
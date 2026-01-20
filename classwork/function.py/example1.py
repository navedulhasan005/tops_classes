# def get_msg():
#     print("Hello, World!")

# def sum(a, b):
#     print(f"Sum: {a + b}")

# def square(n):
#     return n * n

# get_msg()
# sum(3, 5)
# result = square(4)
# print(result)

def total(a, b, c):
    t = a + b + c
    return t

def per(a):
    print(a*100/75)

total_result = total(10, 20, 20)
# print(total_result)
# per(total_result)        

def person(name, email="None", phone=0):
    print(name, email, phone)

# person("my", "my@example.com", "1234567890")
# person("Nick")
# person("Bob",phone="0987654321")

def sum(*a):
    addition = 0  
    for i in a:
        addition += i
    print(addition)
    return addition

sum(10, 20, 30)

def student(**a):
    print(a)

student(name = "my_name", email = "my@gamil.com", age = 21)    
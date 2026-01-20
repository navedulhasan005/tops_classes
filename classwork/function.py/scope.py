a = 10

def test():
    global a
    a  = 120
    print("Inside function:", a)

print(a)
test()
print(a)

square = lambda x: x * x
print(square(5))
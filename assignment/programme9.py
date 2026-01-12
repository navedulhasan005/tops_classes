"""9) Write python program that swap two number with temp variable 
and without temp variable."""

# With temp variable 
number1 = 123
number2 = 456

temp = number1
number1 = number2
number2 = temp
print("***********************************************")
print("After swapping:")
print("Number 1:", number1)
print("Number 2:", number2)

#without temp variable
a = 123
b = 456

a,b = b,a

print("************************************************")

print("After swapping:")
print("a:", a)
print("b:", b)

print("************************************************")
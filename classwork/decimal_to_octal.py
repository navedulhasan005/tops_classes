number = int(input("Enter a decimal number: "))
st = 0
m = 1

while number != 0:
    rem = number % 8
    st = (rem * m) + st
    number //= 8
    m *= 10
print("Octal:", st)
number = int(input("Enter a decimal number: "))
st = 0
m = 1

while number != 0:
    rem = number % 2
    st = (rem * m) + st
    number //= 2
    m *= 10
print("Binary:", st)
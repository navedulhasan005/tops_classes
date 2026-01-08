number = int(input("Enter a binary number: "))
st = 0
m = 1

while number != 0:
    rem = number % 10
    st = (rem * m) + st
    number //= 10
    m *= 2
print("Decimal:", st)
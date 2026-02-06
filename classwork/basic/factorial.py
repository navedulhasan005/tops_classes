num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)


num = 5
fact = 1
while num != 0:
    fact *= num
    num -= 1
print("Factorial:", fact)

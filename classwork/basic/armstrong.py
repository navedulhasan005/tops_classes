for num in range(100, 1000):
    temp = num
    sum = 0
    addition = 0
    while num != 0:
        rem = num % 10
        sum += rem ** 3
        num //= 10
    if sum == temp:
        print(temp, "is an Armstrong number")
    else:
        pass
n = int(input("Enter the number: "))
i = 0
j = 1
for k in range(n):
    print(i)
    i, j = j, i + j
    
    
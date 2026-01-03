n = int(input("Enter the number: "))
i = 0
j = 1
c = 0 
print(i, j, end=' ')
for k in range(n):
    c = i + j
    print(c, end=' ')
    i = j
    j = c
    

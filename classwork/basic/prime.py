for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            print(i,"not prime")
            break
    else:
        pass
        # print(i,"prime")

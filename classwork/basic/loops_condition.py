a = int(input("Enter a marks:"))

if a>=91 and a <= 100:
    print("A Grade")
elif a<=90 and a>=71:
    print("B Grade")    
elif a>=50 and a<=70:
    print("C Grade")
elif a>=35 and a<=50:
    print("D Grade")
elif a>=0 and a<=34:
    print("Fail")
else:
    print("                 ---Invalid input---                 ")            

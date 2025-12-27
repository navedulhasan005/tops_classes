a = int(input("Enter a number:"))
choice = int(input("Enter your operation:"))
print("(1-add,2-minus,3-multipication,4-division)")
b = int(input("Enter a number:"))

match choice:
    case 1:
        choice = a+b
        print("Answer:",choice)
    case 2:
        choice = a-b
        print("Answer:",choice)
    case 3:
        choice = a*b
        print("Answer:",choice)
    case 4:
        choice = a/b
        print("Answer:",choice)
    case _:
        print("_______INVALID CHOICE OF OPERATION______")                

# def before(func):
#     def execute():
#         print("calling before text..")
#         func()
#         print("calling after text..")
#     return execute
    
# @before
# def test():
#     print("text calling..")


# test()

# def before(func):
#     def execute(*a):
#         print("Addition:",a[0] + a[1])
#         return func(*a)
#     return execute

# @before
# def test(i, j):
#     pass

# test(10, 20)

def is_digit(func):
    def check(s):
        s = input("Enter a data: ")
        if s.isdigit():
            return func(s)
        else:
            print("Invalid input! Please enter a digit string.")
    return check

def is_character(func):
    def check(s):
        s = input("Enter a data: ")
        if s.isdigit():
            return func(s)
        else:
            print("Invalid input! Please enter a character string.")
    return check

@is_digit
def input_data(s):
    print(f"You entered a valid data: {s}")

input_data("")

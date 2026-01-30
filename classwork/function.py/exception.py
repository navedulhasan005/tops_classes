# try:
#     a = 100 / 2
#     print("Result:", a)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else: 
#     print("Division successful....")
# finally:
#     print("Execution completed.")


# try:
#     k = 21+"welcome"
#     print(k)
# except TypeError as e:
#     print(e)

def number():
    try:
        n = int(input("Enter a number: "))
        return n
    except Exception as e:
        return e
    finally:
            print("Execution completed.")

result = number()
print("Result:", result)
    
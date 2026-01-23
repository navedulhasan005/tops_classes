# def square(number):
#     print(number * number)
#     number+=1
#     if number <= 10:
#         square(number)
# square(1)        
# l = [10,20,30,40,50]
# k = map(lambda a:a*a,l)
# print(list(k))

# subjects = ["java","python","node","android","php","react"]

# length = map(lambda a:len(a),subjects)
# print(list(length))

subjects = ["java","python","node","android","php","react"]

k = filter(lambda a: 'a' in a, subjects)
print(list(k))
# l = [1,2,3,4,5,6,7,8,9,10]

# k = filter(lambda a: a%2==0,l)
# print(list(k))
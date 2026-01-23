
# Example of creating an iterator from a tuple and using next() to get elements one by one
# l = [100, 200, 300, 400, 500]
# t = (10, 20, 30, 40, 50)

# k = iter(t)

# print(next(k))

def sqaure(n):
    for i in range(n):
        yield i * i

a = (sqaure(5))

print(next(a))
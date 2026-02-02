# class pen:
#     price = 10
#     color = "Red"
#     company = "Cello"

#     def to_write(self):
#         print(self.price,self.color,self.company)

# pen1 = pen()
# print(pen1.color,pen1.price,pen1.company)
# pen1.to_write()

class Demo():

    def __init__(self,name,email,phone_number):
        
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def display(self):
        print(self.name,self.email,self.phone_number)

d1 = Demo("Me","Me@gmail.com",123)
d1.display()

d2 = Demo("You","You@gmail.com",123)
d2.display()
class User:
    clg = "DRB"

    def __init__(self, name, email):
        self.name = name
        self.email = email


    def display(self):
        print(self.name, self.email, self.clg)


# User.clg = "ABC" 
u1 = User("sagar","sagar@gamil.com")
u1.display()  

u2 = User("name","name@gamil.com")
u2.display()  
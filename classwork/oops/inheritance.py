class Animal:

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def display():
        print(self.name,self.type)


class Dog(Animal):

    def __init__(self,name,type,height,weight):
        super.__init__(name,type)
        self.height = height
        self.weight = weight

    def display(self):
        print(self.name,self.type,self.height,self.weight)
        super().display()


class Cat(Animal):
    pass


c1 = Cat("Leo","persian")
c1.display()
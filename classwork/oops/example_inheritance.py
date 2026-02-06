class Bike:
    
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def display(self):
        print(self.name,self.color)


class OtherComponent(Bike):
    def __init__(self,name,color,CC,typeOfBike):
        super().__init__(name,color)
        self.CC = CC
        self.typeOfBike = typeOfBike

    def display(self):
        print(self.name,self.color,self.CC,self.typeOfBike)
        super().display()


class Bajaj(OtherComponent):
    def __init__(self,engineType,name,color,CC,typeOfBike):
        super().__init__(self,name,color,CC,typeOfBike)
        self.engineType = engineType

    def display(self):
        print(self.name,self.color,self.CC,self.typeOfBike,self.engineType)
        super().display()




class RoyalEnfield(OtherComponent):
    pass


b = Bajaj("ns200","red",200,"sports","DOCH")
b.display()


r = RoyalEnfield("Bullet350","White",350,"cruiser")
r.display()


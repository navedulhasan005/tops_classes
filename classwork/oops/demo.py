class pen:
    price = 10
    color = "Red"
    company = "Cello"

    def to_write(self):
        print(self.price,self.color,self.company)

pen1 = pen()
print(pen1.color,pen1.price,pen1.company)
pen1.to_write()

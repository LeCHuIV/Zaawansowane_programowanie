from House import House
from Property import Property


class Fiat(Property):
    def __init__(self, floor, property: Property):
        self.floor = floor
        self.property = property

    def __str__(self):
        return f"{self.property}. Dom ma {self.floor} piętra "


Dom1 = Property("Paderewa", 14, "10000000", "bogucicka")
Dzialka1 = House(5000)
Oferta = Fiat("3",Dom1)
print(Oferta)

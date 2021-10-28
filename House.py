from Property import Property


class House(Property):
    def __init__(self,plot:int):
        self.plot=plot
        
    def __str__(self):
        return f". Działka ma {self.plot}m^2"

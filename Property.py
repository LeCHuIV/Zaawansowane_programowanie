class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość znajduje się w:{self.area} ma {self.rooms} pokoi, kosztuje: {self.price} jest na ulicy: {self.address}"
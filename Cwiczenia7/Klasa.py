import json


class Movie:
    def __init__(self, id, title, kat):
        self.id = id
        self.title = title
        self.kat = kat


class xd:
    pass

    @property
    def z(self):
        return self.z

    @z.setter
    def z(self, value):
        pass



    def oblicz_wartosc_zamowienia(self) -> float:
        return round((self._ilosc * self._cenajednostkowa), 2)
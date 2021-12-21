from Dieta import Dieta
from Pacjent import Pacjent
from Dietetyk import Dietetyk


class Zamowienie:
    _numer: str
    _wartosc: float
    _diety: list
    _pacjent: Pacjent
    _dietetyk: Dietetyk
    _kalorie: float

    @property
    def kalorie(self):
        return self._kalorie

    @kalorie.setter
    def kalorie(self, value: float):
        self._kalorie = value

    @property
    def numer(self):
        return self._numer

    @numer.setter
    def numer(self, value: str):
        self._numer = value

    @property
    def wartosc(self):
        return self._wartosc

    @wartosc.setter
    def wartosc(self, value: float):
        self._wartosc = value

    @property
    def diety(self):
        return self._diety

    @diety.setter
    def diety(self, value):
        self._diety = value

    @property
    def pacjent(self):
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value):
        self._pacjent = value

    @property
    def dietetyk(self):
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, value):
        self._dietetyk = value

    def __str__(self):
        return f"Zamówienie numer:{self._numer}, o wartości: {self._wartosc}," \
               f" z liczbą kalorii: {self._kalorie} od:{self._dietetyk}, dla:{self._pacjent}"

    def oblicz_wartosc(self):
        wartosc = 0
        for z in self.diety:
            wartosc += z._cena
        return round(wartosc, 2)


    def oblicz_kalorie(self):
        wartosc = 0
        for z in self.diety:
            wartosc += z._kalorie
        return round(wartosc, 2)

dieta1 = Dieta("350g", 4, 17, 1800)
dieta2 = Dieta("350g", 4, 17, 1800)
pacjent1 = Pacjent("Patryk", "Lech", 95, 190)
deietetyk1 = Dietetyk("Karol", "Okrasa", 100, 4)
zamowienie1 = Zamowienie()
zamowienie1.numer = 1
zamowienie1.diety = [dieta1,dieta2]
zamowienie1.dietetyk = deietetyk1
zamowienie1.pacjent = pacjent1
zamowienie1.wartosc = zamowienie1.oblicz_wartosc()
zamowienie1.kalorie = zamowienie1.oblicz_kalorie()
print(zamowienie1)

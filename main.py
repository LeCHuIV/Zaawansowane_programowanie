from Dieta import Dieta
from Pacjent import Pacjent
from Dietetyk import Dietetyk
from Zamowienie import Zamowienie


class Baza(Dieta, Pacjent, Dietetyk, Zamowienie):
    def __init__(self, dieta: Dieta, dietetyk: Dietetyk, pacjent: Pacjent, zamowienie: Zamowienie):
        self._dieta = dieta
        self._dietetyk = dietetyk
        self._pacjent = pacjent
        self._zamowienie = zamowienie

    def oblicz_wartosc(self) -> float:
        return round((self._dieta.cena * self._dieta.posilki), 2)

    dieta1 = Dieta("350g",4,17,1800)
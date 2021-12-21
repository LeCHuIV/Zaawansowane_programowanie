class Dieta:
    def __init__(self, waga, posilki: int, cena: int, kalorie):
        self._waga = waga
        self._posilki = posilki
        self._cena = cena
        self._kalorie = kalorie

    @property
    def waga(self):
        return self._waga

    @property
    def posilki(self):
        return self._posilki

    @property
    def cena(self):
        return self._cena

    @property
    def kalorie(self):
        return self._kalorie

    def __str__(self):
        return print(f"Dieta składa się z{self._posilki} posiłków zawiera {self._kalorie} kalorii waży: {self._waga}")

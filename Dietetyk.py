class Dietetyk:
    def __init__(self, imie, nazwisko, cena: int, ocena: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._cena = cena
        self._ocena = ocena

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def cena(self):
        return self._cena

    @property
    def ocena(self):
        return self._ocena

    def __str__(self):
        return f"Dietetyk: {self._imie} {self._nazwisko}" \
               f"świadczy wizyty w cenie: {self._cena} a jego ocena to: {self._ocena}"

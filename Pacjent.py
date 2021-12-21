class Pacjent:
    def __init__(self, imie, nazwisko, waga: int, wzrost: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._waga = waga
        self._wzrost = wzrost

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def waga(self):
        return self._waga

    @property
    def wzrost(self):
        return self._wzrost

    def __str__(self):
        return f"Pacjent: {self._imie} {self._nazwisko} o wadze: {self._waga} i wzroście {self._wzrost}"

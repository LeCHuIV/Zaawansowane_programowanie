class Produkt:
    def __init__(self,Nazwa,Kraj,Liczba,Opis,Cena):
        self.nazwa=Nazwa
        self.kraj=Kraj
        self.liczba=Liczba
        self.opis=Opis
        self.cena=Cena
    def __str__(self):
        return f"{self.nazwa} Pochodzi z{self.kraj}, o wartości:{self.liczba}{self.cena}. Opis \n{self.opis}"

    @property
    def nazwa(self)-> str:
        return self.nazwa


    @nazwa.setter
    def nazwa(self, value):
        self.nazwa = value

    @property
    def kraj(self) -> str:
        return self.kraj


    @kraj.setter
    def kraj(self, value):
        self.kraj = value


    @property
    def liczba(self)-> int:
        return self.liczba


    @liczba.setter
    def liczba(self, value):
        self.liczba = value


    @property
    def opis(self)-> str:
        return self.opis


    @opis.setter
    def opis(self, value):
        self.opis = value


    @property
    def cena(self)-> int:
        return self.cena


    @cena.setter
    def cena(self, value):
        self.cena = value

class Magazyn:
    def __init__(self,Nazwa,Numer,Kraj,Miasto,Kod):
        self.nazwa=Nazwa
        self.numer=Numer
        self.kraj=Kraj
        self.miasto=Miasto
        self.kod=Kod
    def __str__(self):
        return f"Magazyn:{self.nazwa} o numerze:{self.numer} znajduje się w {self.kraj}, w mieście:{self.miasto} a jego kod to:{self.kod}"

    @property
    def nazwa(self) -> str:
        return self.nazwa

    @nazwa.setter
    def nazwa(self, value):
        self.nazwa = value

    @property
    def kraj(self) -> str:
        return self.kraj

    @kraj.setter
    def kraj(self, value):
        self.kraj = value


    @property
    def numer(self) -> int:
        return self.numer


    @numer.setter
    def numer(self,value):
        self.numer=value


    @property
    def miasto(self) -> str:
        return self.miasto


    @miasto.setter
    def miasto(self,value):
        self.miasto=value


    @property
    def kod(self)-> int:
        return self.kod


    @kod.setter
    def kod(self,value):
        self.kod=value

class KlientDetaliczny:
    def __init__(self,Nazwa,Adres,Miasto,Rabat,Kraj):
        self.nazwa=Nazwa
        self.adres=Adres
        self.miasto=Miasto
        self.rabat=Rabat
        self.kraj=Kraj
    def __str__(self):
        return f"{self.nazwa} z{self.kraj} w mieście:{self.miasto} w sklepie na ulicy:{self.adres} uzyskał rabat w wysokości:{self.rabat} "

    @property
    def nazwa(self) -> str:
        return self.nazwa


    @property
    def adres(self) -> str:
        return self.adres


    @property
    def miasto(self)-> str:
        return self.miasto


    @property
    def rabat(self) -> str:
        return self.rabat


    @property
    def kraj(self) -> str:
        return self.kraj

    @adres.setter
    def adres(self, value):
        self._adres = value

    @nazwa.setter
    def nazwa(self, value):
        self._nazwa = value

    @miasto.setter
    def miasto(self, value):
        self._miasto = value

    @rabat.setter
    def rabat(self, value):
        self._rabat = value

    @kraj.setter
    def kraj(self, value):
        self._kraj = value


class Zamowienie(Magazyn, Produkt, KlientDetaliczny):
    def __init__(self,Numer,Opiekun,Klient : KlientDetaliczny,Magazyn : Magazyn,Produkt : Produkt):
        self.numer=Numer
        self.opiekun=Opiekun
        self.klient=Klient
        self.magazyn=Magazyn
        self.produkt=Produkt

    @property
    def numer(self)-> int:
        return self.numer

    @numer.setter
    def numer(self,value):
        self.numer=value
    @property
    def opiekun(self) -> str:
        return self.opiekun

    @opiekun.setter
    def opiekun(self,value):
        self.opiekun=value


    @property
    def klient(self)-> str:
        return self.klient

    @klient.setter
    def klient(self,value):
        self.klient=value

    @property
    def magazyn(self) -> str:
        return self.magazyn

    @magazyn.setter
    def magazyn(self,value):
        self.magazyn=value
    @property
    def produkt(self)-> str:
        return self.produkt

    @produkt.setter
    def produkt(self,value):
        self.produkt=value

    def __str__(self):
        return f"Zamównie numer:{self.numer}, dla{self.klient}, z magazynu:{self.magazyn}, produkt:{self.produkt}"
Klient1 = KlientDetaliczny("Jan","Bogucicka","Katowice","15","Polska")
Magazyn1 = Magazyn("Głowny" , 1 ,"Polska","Katowice",113)
Produkt1 = Produkt("Chleb","Polska",2,"Żytni",10)
Zamowienie1 =Zamowienie(1,"Jan",Klient1,Magazyn1,Produkt1)

print(Zamowienie1)
class KlientBiznesowy:
    def __init__(self, Nazwa, Adres, Kod, Rabat, Kraj):
        self.nazwa = Nazwa
        self.adres = Adres
        self.kod = Kod
        self.rabat = Rabat
        self.kraj = Kraj
    def __str__(self):
        return f"{self.nazwa} z{self.kraj}{self.adres} o numerze:{self.kod} uzyskał rabat w wysokości:{self.rabat} "

    @property
    def nazwa(self) -> str:
        return self.nazwa
    @nazwa.setter
    def nazwa(self,value):
        self.nazwa=value

    @property
    def adres(self) -> str:
        return self.adres

    @adres.setter
    def adres(self,value):
        self.adres=value
    @property
    def kod(self) -> str:
        return self.kod

    @kod.setter
    def kod(self,value):
        self.kod=value
    @property
    def rabat(self) -> str:
        return self.rabat

    @rabat.setter
    def rabat(self,value):
        self.rabat=value
    @property
    def kraj(self) -> str:
        return self.kraj
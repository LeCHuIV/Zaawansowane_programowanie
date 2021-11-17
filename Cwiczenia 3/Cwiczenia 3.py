#1

print("Zadanie 1")
def metoda(name: str, surname: str) -> str: return (f"Cześć, {name} {surname}!")

x = metoda("Patryk","Lech")
print(x)

#2
print("Zadanie 2")
def mnozenie(x: int, y:int) -> int: return (x*y)

print(mnozenie(14,4))

#3
print("Zadanie 3")
def parzysta(x: int) -> bool:
    if x%2!=0:
        return False
    else:
        return True
y = parzysta(3)
if y == True:
            print("Liczba parzysta")
else:
            print("Liczba nieparzysta")
#4
(print("Zadanie 4"))
def czy_wieksza(x: int, y: int, z: int) -> bool:
    if x+y>=z:
        return True
    else:
        return False
y = czy_wieksza(2,3,4)
if y==True:
    print("Suma dwóch pierwszych liczb jest większa od trzeciej")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej")
#5
print("Zadanie 5")
def sprawdzenie(x: list, y:int) -> bool:
    if y in x:
        return True
    else:
        return False
z = sprawdzenie([3,4,2],2)
if z==True:
    print("Zawiera się")
else:
    print("Nie zawiera się")
#6
print("Zadanie 6")
def laczenie_list(x: list, y: list) -> list:
    d = set(x+y)
    lista = [i**3 for i in d]
    return (lista)
z = laczenie_list([1,2,3,4],[2,3,4,8,7])

print(z)
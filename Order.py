from Book import Book
from Employee import Employee
from main import Student
from Library import Library


class Order(Employee , Book, Student):
    def __init__(self,employee: Employee,student: Student ,books: Book,order_date):
        self.employee= employee
        self.student= student
        self.books=books
        self.order_date=order_date

    def __str__(self):
        return f"Pracownik: {self.employee} przygotował zamówienie dla:{self.student} w postaci {self.books} książek w dniu {self.order_date} "

Pracownik1 = Employee("Patryk","Lech","12.10.2018r","22.12.2020r","Katowice","Bogucicka",32-345,555555555)
Pracownik2 = Employee("Patryk","Piotrowski","12.10.2014r","22.12.2010r","Katowice","Bogucicka",32-335,5555555555)
Pracownik3 = Employee("Kinga","Lech","12.10.2007r","22.12.2021r","Zawiercie","Bogucicka",32-325,55555555)
bilbioteka1 = Library("Katowice","Bogucicka",44-244,"8-22",555555555)
bilbioteka2 = Library("Zawiercie","Bogucicka",44-444,"8-22",455555555)
Książka1 = Book(bilbioteka1,"1.11.2021r","Adam","Nowak",150)
Książka2 = Book(bilbioteka2,"1.11.2011r","Jan","Nowak",160)
Książka3 = Book(bilbioteka1,"1.11.1995r","Adam","Kowalski",170)
Książka4 = Book(bilbioteka2,"1.11.2001r","Jan","Kowalski",180)
Książka5 = Book(bilbioteka1,"1.11.2000r","Patryk","Nowak",190)
Książka1 = Book(bilbioteka1,"1.11.2021r","Adam","Nowak",150)
Książka2 = Book(bilbioteka2,"1.11.2011r","Jan","Nowak",160)
Książka3 = Book(bilbioteka1,"1.11.1995r","Adam","Kowalski",170)
Książka4 = Book(bilbioteka2,"1.11.2001r","Jan","Kowalski",180)
Książka5 = Book(bilbioteka1,"1.11.2000r","Patryk","Nowak",190)
Student1 = Student("Patryk",55)
Student2 = Student("Bartek",42)
Student3 = Student("Kinga",98)
Zamowienie1=Order(Pracownik1 ,Student3,Książka5,"12.02.2021r")
Zamowienie2=Order(Pracownik2,Student2,Książka4,"12.04.2018r")

print(Zamowienie1,"\n",Zamowienie2)
from Library import Library


class Book(Library):
    def __init__(self,library: Library,publication_date,author_name,author_surname,number_of_pages):
        self.library = library
        self.publication_date=publication_date
        self.author_name=author_name
        self.author_surname=author_surname
        self.number_of_pages=number_of_pages

    def __str__(self):
        return f"{self.library} {self.author_name} {self.author_surname}"

bilbioteka1 = Library("Katowice","Bogucicka",44-244,"8-22",555555555)
bilbioteka2 = Library("Zawiercie","Bogucicka",44-444,"8-22",455555555)
Książka1 = Book(bilbioteka1,"1.11.2021r","Adam","Nowak",150)
Książka2 = Book(bilbioteka2,"1.11.2011r","Jan","Nowak",160)
Książka3 = Book(bilbioteka1,"1.11.1995r","Adam","Kowalski",170)
Książka4 = Book(bilbioteka2,"1.11.2001r","Jan","Kowalski",180)
Książka5 = Book(bilbioteka1,"1.11.2000r","Patryk","Nowak",190)

print(Książka1)
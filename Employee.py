class Employee:
    def __init__(self,first_name,last_name,hire_date,birth_date,city,street,zip_code,phone):
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.birth_date=birth_date
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.phone=phone

    def __str__(self):
        return f"{self.city} {self.first_name} {self.last_name} {self.street} {self.phone} {self.zip_code} {self.birth_date}"
Pracownik1 = Employee("Patryk","Lech","12.10.2018r","22.12.2020r","Katowice","Bogucicka",32-345,555555555)
Pracownik2 = Employee("Patryk","Piotrowski","12.10.2014r","22.12.2010r","Katowice","Bogucicka",32-335,5555555555)
Pracownik3 = Employee("Kinga","Lech","12.10.2007r","22.12.2021r","Zawiercie","Bogucicka",32-325,55555555)

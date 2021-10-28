class Library:
    def __init__(self,city,street,zip_code,open_hours:str,phone):
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.open_hours=open_hours
        self.phone=phone

    def __str__(self):
        return f"{self.city} {self.street} {self.phone}, {self.open_hours}, {self.zip_code}"

bilbioteka1 = Library("Katowice","Bogucicka",44-244,"8-22",555555555)
bilbioteka2 = Library("Zawiercie","Bogucicka",44-444,"8-22",455555555)

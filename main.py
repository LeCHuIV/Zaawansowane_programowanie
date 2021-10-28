class Student:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name

    def is_passed(self) -> bool:
        if (self.marks>50):
            return True
        else:
            return False
    def __str__(self):
        return f"{self.marks} {self.name}"
Student1 = Student("Patryk",55)
Student2 = Student("Bartek",42)
Student3 = Student("Kinga",98)
print(Student1.is_passed())
print(Student2.is_passed())
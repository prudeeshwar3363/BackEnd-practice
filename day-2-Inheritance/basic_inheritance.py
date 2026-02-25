class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
    
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    
    def display_info(self):
        super().display_info()
        print("Marks:", self.marks)
    
s1 = Student("John", 20, 90)
s1.display_info()
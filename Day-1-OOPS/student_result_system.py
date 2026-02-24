class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.total = None
        self.average = None
        self.pass_fail = None
    
    def calculate_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3
    
    def calculate_average(self):
        self.average = self.total / 3
    
    def check_pass_fail(self):
        if self.average >= 40:
            self.pass_fail = "PASS"
        else:
            self.pass_fail = "FAIL"
    
    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Total: {self.total}")
        print(f"Average: {self.average}")
        print(f"Result: {self.pass_fail}")

name = input("Name: ")
marks1 = int(input("Marks 1: "))
marks2 = int(input("Marks 2: "))
marks3 = int(input("Marks 3: "))

s1 = Student(name, marks1, marks2, marks3)
s1.calculate_total()
s1.calculate_average()
s1.check_pass_fail()
s1.display_result()
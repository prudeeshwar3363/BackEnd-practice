from datetime import datetime

class Car:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.age = None

    def calculate_age(self):
        current_year = datetime.now().year
        self.age = current_year - self.year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        if self.age is not None:
            print(f"Age: {self.age} years")

brand = input("Brand: ")
model = input("Model: ")
year = int(input("Year: "))

c1 = Car(brand, model, year)
c1.calculate_age()
c1.display_info()
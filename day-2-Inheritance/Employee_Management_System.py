class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, base_salary=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

fte = FullTimeEmployee("Alice", 50000, 5000)
pte = PartTimeEmployee("Bob", 20, 80)

print(fte.calculate_salary())
print(pte.calculate_salary())
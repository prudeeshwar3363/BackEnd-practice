def safe_calculator(a, b):
    try:
        division = a/b
        print(division)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid Input")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

safe_calculator(a, b)
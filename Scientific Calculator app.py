import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def calculate():
    print("Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        print("Exiting the calculator...")
        return

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    elif choice in ('6', '7', '8', '9'):
        num = float(input("Enter the number: "))

        if choice == '6':
            print("Result:", sqrt(num))
        elif choice == '7':
            print("Result:", sin(num))
        elif choice == '8':
            print("Result:", cos(num))
        elif choice == '9':
            print("Result:", tan(num))
    else:
        print("Invalid input. Please try again.")

    print()
    calculate()

calculate()

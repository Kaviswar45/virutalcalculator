import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero!")

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        print("Error: Square root of a negative number!")

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        print("Error: Invalid logarithm input!")

def factorial(x):
    if x >= 0 and x.is_integer():
        return math.factorial(int(x))
    else:
        print("Error: Invalid factorial input!")

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def inverse_sin(x):
    return math.degrees(math.asin(x))

def inverse_cos(x):
    return math.degrees(math.acos(x))

def inverse_tan(x):
    return math.degrees(math.atan(x))

def absolute_value(x):
    return abs(x)

print("Welcome to the Virtual Calculator!")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Logarithm")
    print("9. Factorial")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Inverse Sine")
    print("14. Inverse Cosine")
    print("15. Inverse Tangent")
    print("16. Absolute Value")
    print("17. Exit")

    choice = input("Enter choice (1-17): ")

    if choice == '17':
        print("Exiting the calculator...")
        break

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = power(num1, num2)
        elif choice == '6':
            result = modulus(num1, num2)

        print("The result is:", result)

    elif choice == '7':
        num = float(input("Enter a number: "))
        result = square_root(num)
        if result is not None:
            print("The square root is:", result)

    elif choice == '8':
        num = float(input("Enter a number: "))
        base = float(input("Enter the base: "))
        result = logarithm(num, base)
        if result is not None:
            print("The logarithm is:", result)

    elif choice == '9':
        num = float(input("Enter a non-negative integer: "))
        result = factorial(num)
        if result is not None:
            print("The factorial is:", result)

    elif choice == '10':
        num = float(input("Enter an angle in degrees: "))
        result = sin(num)
        print("The sine is:", result)

    elif choice == '11':
        num = float(input("Enter an angle in degrees: "))
        result = cos(num)
        print("The cosine is:", result)

    elif choice == '12':
        num = float(input("Enter an angle in degrees: "))
        result = tan(num)
        print("The tangent is:", result)

    elif choice == '13':
        num = float(input("Enter a value between -1 and 1: "))
        result = inverse_sin(num)
        print("The inverse sine is:", result, "degrees")

    elif choice == '14':
        num = float(input("Enter a value between -1 and 1: "))
        result = inverse_cos(num)
        print("The inverse cosine is:", result, "degrees")

    elif choice == '15':
        num = float(input("Enter a value: "))
        result = inverse_tan(num)
        print("The inverse tangent is:", result, "degrees")

    elif choice == '16':
        num = float(input("Enter a number: "))
        result = absolute_value(num)
        print("The absolute value is:", result)

    else:
        print("Invalid input. Please try again.")

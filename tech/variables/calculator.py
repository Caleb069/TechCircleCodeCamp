def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Operations available: + (addition), - (subtraction), * (multiplication), / (division)")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"The result of {num1} {operation} {num2} is: {result}")
        
        except ValueError as ve:
            print(f"Error: {ve}. Please enter valid numbers.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the calculator!")
            break

# Uncomment the line below to run the calculator
calculator()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        # Get user input
        operation = input("Enter the number corresponding to the operation: ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '1':
            print(f"The result is: {add(num1, num2)}")
        elif operation == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif operation == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif operation == '4':
            print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid operation choice. Please choose a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

if __name__ == "__main__":
    main()

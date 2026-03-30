import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(x)
    
def percentage(x, y):
        return (x / 100) * y
    
def calculator():
    print("--- Basic Python Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Percentage (x% of y)")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                # Square root only requires one input
                if choice == '6':
                    num1 = float(input("Enter the number: "))
                else:
                    num1 = float(input("Enter the first number (base/percentage): "))
                    num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':   
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':   
                print(f"Result: √{num1} = {square_root(num1)}") 
            elif choice == '7':   
                print(f"Result: {num1}% of {num2} = {percentage(num1, num2)}")
            
            print("-" * 30)
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    calculator()

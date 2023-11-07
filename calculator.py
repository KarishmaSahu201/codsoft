# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function to prompt the user and perform the calculation
def calculator():
    while True:
        # Prompt the user for input
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        
        choice = input("Enter your choice: ")
        
        # Check if the user wants to quit
        if choice == 'quit':
            exit()
        
        # Check if the choice is a valid operation
        if choice in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 'add':
                result = add(num1, num2)
            elif choice == 'subtract':
                result = subtract(num1, num2)
            elif choice == 'multiply':
                result = multiply(num1, num2)
            elif choice == 'divide':
                result = divide(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid input. Please try again.")

# Run the calculator program
calculator()

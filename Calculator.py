#!/usr/bin/env python3
"""
Calculator CLI App
A command-line calculator supporting basic arithmetic operations.
Author: Python Developer Intern
"""

def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation with zero division handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("       CALCULATOR CLI APP")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def get_operation_choice():
    """Get valid operation choice from user"""
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice! Please select 1-5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")

def perform_calculation(choice, num1, num2):
    """Perform calculation based on user choice"""
    operations = {
        1: (add, "+"),
        2: (subtract, "-"),
        3: (multiply, "*"),
        4: (divide, "/")
    }
    
    operation_func, symbol = operations[choice]
    
    try:
        result = operation_func(num1, num2)
        print(f"\nResult: {num1} {symbol} {num2} = {result}")
        return result
    except ValueError as e:
        print(f"\nError: {e}")
        return None

def main():
    """Main function to run the calculator"""
    print("Welcome to the Calculator CLI App!")
    
    while True:
        display_menu()
        choice = get_operation_choice()
        
        if choice == 5:
            print("\nThank you for using the Calculator CLI App!")
            print("Goodbye! 👋")
            break
        
        # Get numbers from user
        print(f"\nYou selected: {['', 'Addition', 'Subtraction', 'Multiplication', 'Division'][choice]}")
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        # Perform calculation
        result = perform_calculation(choice, num1, num2)
        
        # Ask if user wants to continue
        while True:
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
            if continue_calc in ['y', 'yes']:
                break
            elif continue_calc in ['n', 'no']:
                print("\nThank you for using the Calculator CLI App!")
                print("Goodbye! 👋")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()
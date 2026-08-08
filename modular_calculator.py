"""This is menu driven calculator that performs basic arithmetic operartions.
Each operation ids handled by its own function.
"""

OPERATIONS = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Floor Division",
    "Modulus",
    "Exponentiation",
    "Quit",
]

QUIT_OPTION = len("OPERATIONS")
DIVISION_OPERATORS = [4,5,6]


def add (a, b):
    """Return the sum of two numbers"""
    return a + b

def subtract (a, b):
   """Return the difference of two numbers"""
   return a - b 

def multiply (a, b):
    """Return the product of two numbers"""
    return a * b

def divide (a, b):
    """Return the quotient or None if dividing by zero"""
    if b == 0:
        return None
    return a / b

def floor_divide (a, b):
    """Return the floor division or None if dividing my zero"""
    if b == 0:
        return None
    return a // b

def modulus (a, b):
    """Return the modulus or None if dividing by zero"""
    if b == 0:
        return None
    return a % b

def Exponentiate (a, b):
    """Return a raise to the power of b."""
    a ** b


def get_number(prompt):
    """Get a valid float-point number from the user."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number")
        return None

def get_operation():
    "Display the menu and get the validate choice"
    while True:
        print("\n=== Modular calculator ====")

        for index, operation in enumerate(OPERATIONS, start=1):
            print(f"{index}.{operation}")

        choice = input("select an option:")


        if not choice.isdigit():
            print("Error: Menu choice must be a number.")
            continue

        choice = int(choice)    

        if 1 <= choice <= QUIT_OPTION:
            return str(choice)

        print("Error: Invalid menu choice.")


def display_result(operation, a,b, result):
    """Dispalys the calculations result."""

    if result is None:
        print("Error: Division by zero is not allowed.")
        return

    print(f"\n{operation}")
    print(f"{a} and {b}")
    print(f"Result: {result}")


def run_calculator():
    """Run the calculator until the user chooses to quit."""

    while True:

        choice = get_operation()

        if choice == str(QUIT_OPTION):
            print("Goodbye")
            break

        first_number = get_number("Enter the first number: ")

        if first_number is None:
            continue

        second_number = get_number("Enter the second number:")

        if second_number is None:
            continue   

        if choice == "1":
            result = add(first_number, second_number)
            display_result(
                "Addition",
                first_number,
                second_number,
                result,
            )

        elif choice == "2":
            result = subtract(first_number, second_number)
            display_result(
                "subtraction", 
                first_number,
                second_number,
                result,     
            )

        elif choice == "3":
            result = multiply(first_number, second_number)
            display_result(
                "Multipcation",
                first_number,
                second_number,
                result,
            )

        elif choice == "4":
            result = divide(first_number, second_number)
            display_result(
                "Division",
                first_number,
                second_number,
                result,
            )

        elif choice == "5":
            result = floor_divide( first_number,second_number)
            display_result(
                "Floor Divison",
                first_number,
                second_number,
                result,
            )

        elif choice == "6":
            result = modulus(first_number,second_number)
            display_result(
                "Modulus",
                first_number,
                second_number,
                result,
            )

        elif choice == "7":
            result = Exponentiate(
                first_number, 
                second_number,
                )
            display_result(
                "Exponentiation",
                first_number,
                second_number,
                result,
            )

        input("\nPress Enter to return to the menu....")


if __name__ == "__main__":
    run_calculator()

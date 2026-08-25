"""A layered menu-driven calculator."""


OPTIONS = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Floor Division",
    "Modulus",
    "Exponentiation",
    "Quit",
]


# Calculation layer

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient or None when b is zero."""
    if b == 0:
        return None
    return a / b


def floor_divide(a, b):
    """Return floor division or None when b is zero."""
    if b == 0:
        return None
    return a // b


def modulus(a, b):
    """Return the remainder or None when b is zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b


# Utility layer

def display_error(message):
    """Display an error message."""
    print(f"Error: {message}")


def get_number(prompt):
    """Return a valid float or None for invalid input."""
    try:
        return float(input(prompt))
    except ValueError:
        display_error("Please enter a valid number.")
        return None


def validate_divisor(b):
    """Return True when the divisor is not zero."""
    return b != 0


def display_menu(options):
    """Display the numbered calculator menu."""
    print("\n=== Menu Calculator ===")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


def display_result(operation, a, b, result):
    """Display a calculation result or division error."""
    if result is None:
        display_error("Cannot divide by zero.")
        return
    print(f"{operation}: {a} and {b} = {result}")


# Feature layer

def get_operation(options):
    """Display the menu and return a valid choice."""
    display_menu(options)
    choice = input("Select an option: ")

    if not choice.isdigit():
        display_error("Menu choice must be a number.")
        return None

    choice = int(choice)
    if choice < 1 or choice > len(options):
        display_error("Invalid menu choice.")
        return None

    return choice


def get_inputs():
    """Return two valid numbers or None."""
    first_number = get_number("Enter the first number: ")
    if first_number is None:
        return None

    second_number = get_number("Enter the second number: ")
    if second_number is None:
        return None

    return first_number, second_number


def run_operation(operation, a, b):
    """Route the selected operation to its calculation."""
    calculations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: floor_divide,
        6: modulus,
        7: exponentiate,
    }

    if operation in (4, 5, 6) and not validate_divisor(b):
        return None

    calculation = calculations.get(operation)
    if calculation is None:
        return None

    return calculation(a, b)


# Entry layer

def main():
    """Run the calculator menu and coordinate program flow."""
    while True:
        operation = get_operation(OPTIONS)

        if operation is None:
            continue

        if operation == 8:
            print("Goodbye!")
            break

        inputs = get_inputs()
        if inputs is None:
            continue

        a, b = inputs
        result = run_operation(operation, a, b)

        if result is None:
            display_error("Cannot divide by zero.")
            continue

        display_result(OPTIONS[operation - 1], a, b, result)


if __name__ == "__main__":
    main()

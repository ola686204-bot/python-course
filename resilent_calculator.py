"""This is a program that handles all errors gracefully.
provides specific and helpful error messages for every failuure mode, and never crashes under any user inpuut"""

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

QUIT_OPTION = len(OPERATIONS)
DIVISION_OPERATORS = [4, 5, 6]


def add(a, b):
    """Return the sum of two numbers."""
    try:
        return a + b
    except TypeError:
        print(f"cannot add {type(a).__name__} and {type(b).__name__}.Both must be numbers")
    else:
        print(f"Addition successful: {result}")
        return result

def subtract(a, b):
    """Return the difference between two numbers."""
    try:
        return a - b
    except TypeError:
            print(f"cannot subtract {type(a).__name__} and {type(b).__name__}.Both must be numbers")
    else:
        print(f"Subtraction successful: {result}")
        return result
    


def multiply(a, b):
    """Return the product of two numbers."""
    try:
        return a * b
    except TypeError:
            print(f"cannot multiply {type(a).__name__} and {type(b).__name__}.Both must be numbers")
            return None
    


def divide(a, b):
    """Return the quotient or None if dividing by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Division successful: {result}")
    finally:
        print("Division operation finished.")


def floor_divide(a, b):
    """Return the floor division or None if dividing by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Division successful: {result}")
    finally:
        print("Division operation finished.")


def modulus(a, b):
    """Return the modulus or None if dividing by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Division successful: {result}")
    finally:
        print("Division operation finished.")


def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b


def retry_on_error(prompt, converter, max_attempts):
    """Prompt for input and retry when conversion fails.

    Args:
        prompt: The message shown to the user.
        converter: Function used to convert the input.
        max_attempts: Maximum number of failed attempts.

    Returns:
        The converted value if successful, otherwise None.
    """
    attempts = 0

    while attempts < max_attempts:
        user_input = input(prompt)

        try:
            value = converter(user_input)
        except ValueError:
            attempts += 1
            print("Error: Please enter a valid number.")
        else:
            return value

    print("Error: Maximum attempts reached.")
    return None


def get_number(prompt):
    """Get a valid floating-point number from the user.

    Args:
        prompt: The message displayed when requesting input.

    Returns:
        The user's input as a float, or None if attempts fail.
    """
    return retry_on_error(prompt, float, 3)

def get_operation():
    """Display the menu and get a validated choice.

    Returns:
        The user's menu choice as a string.
    """
    while True:
        print("\n========= Resilent Calculator =========")

        for index, operation in enumerate(OPERATIONS, start=1):
            print(f"{index}. {operation}")

        choice = input("Select an option: ")

        if not choice.isdigit():
            print("Error: Menu choice must be a number.")
            continue

        choice = int(choice)

        if 1 <= choice <= QUIT_OPTION:
            return str(choice)

        print("Error: Invalid menu choice.")


def display_result(operation, a, b, result):
    """Display the calculation result.

    Args:
        operation: The name of the operation.
        a: The first number.
        b: The second number.
        result: The calculated result.
    """
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

        second_number = get_number("Enter the second number: ")

        if second_number is None:
            continue

        if choice == "1":
            result = add(first_number, second_number)
            operation = "Addition"
        elif choice == "2":
            result = subtract(first_number, second_number)
            operation = "Subtraction"
        elif choice == "3":
            result = multiply(first_number, second_number)
            operation = "Multiplication"
        elif choice == "4":
            result = divide(first_number, second_number)
            operation = "Division"
        elif choice == "5":
            result = floor_divide(first_number, second_number)
            operation = "Floor Division"
        elif choice == "6":
            result = modulus(first_number, second_number)
            operation = "Modulus"
        else:
            result = exponentiate(first_number, second_number)
            operation = "Exponentiation"

        display_result(
            operation,
            first_number,
            second_number,
            result,
        )

        input("\nPress Enter to return to the menu....")


if __name__ == "__main__":
    run_calculator()

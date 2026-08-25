"""Provide a continuous menu-driven calculator."""


def get_number(prompt):
    """Validate numeric input and return a float.

    Args:
        prompt: The message displayed when requesting input.

    Returns:
        The user's number as a float, or None if the input is invalid.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def get_divisor(prompt):
    """Validate divisor input and prevent division by zero.

    Args:
        prompt: The message displayed when requesting the divisor.

    Returns:
        The divisor as a float, or None if the input is invalid or zero.
    """
    try:
        divisor = float(input(prompt))

        if divisor == 0:
            print("Error: Division by zero is not allowed.")
            return None

        return divisor

    except ValueError:
        print("Error: Please enter a valid number.")
        return None


operations = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Floor Division",
    "Modulus",
    "Exponentiation",
    "Quit",
]


while True:
    print("\n=== Continuous Calculator ===")

    for index, operation in enumerate(operations, start=1):
        print(f"{index}. {operation}")

    choice = input("Select an option from the menu: ")

    if not choice.isdigit():
        print("Error: Menu choice must be a number.")
        continue

    choice = int(choice)

    if choice < 1 or choice > len(operations):
        print("Error: Invalid menu choice.")
        continue

    if choice == 8:
        print("Goodbye!")
        break

    first_number = get_number("Enter the first number: ")

    if first_number is None:
        continue

    if choice in [4, 5, 6]:
        second_number = get_divisor("Enter the second number: ")
    else:
        second_number = get_number("Enter the second number: ")

    if second_number is None:
        continue

    if choice == 1:
        result = first_number + second_number
    elif choice == 2:
        result = first_number - second_number
    elif choice == 3:
        result = first_number * second_number
    elif choice == 4:
        result = first_number / second_number
    elif choice == 5:
        result = first_number // second_number
    elif choice == 6:
        result = first_number % second_number
    elif choice == 7:
        result = first_number ** second_number
    else:
        print("Error: Unknown operation.")
        continue

    print(f"\nResult: {result}")
    input("\nPress Enter to return to the operation menu...")

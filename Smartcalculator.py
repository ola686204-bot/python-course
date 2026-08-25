"""Provide a smart calculator with input validation."""


def validate_menu_choice(choice):
    """Validate that the menu choice is an allowed option.

    Args:
        choice: The menu choice entered by the user.

    Returns:
        The choice if valid, otherwise None.
    """
    valid_choices = ["1", "2", "3", "4", "5", "6", "7"]

    if choice not in valid_choices:
        print(
            "Error: Invalid choice. Please select a number "
            "between 1 and 7."
        )
        return None

    return choice


def validate_number(value, is_second=False, operation=None):
    """Validate a number and prevent division by zero.

    Args:
        value: The value entered by the user.
        is_second: Whether the value is the second number.
        operation: The selected calculator operation.

    Returns:
        The number as a float if valid, otherwise None.
    """
    if value.strip() == "":
        print("Error: Input cannot be empty.")
        return None

    try:
        num = float(value)
    except ValueError:
        print("Error: Please enter a valid numeric value.")
        return None

    if is_second and operation in ["4", "5"] and num == 0:
        print("Error: Division or floor division by zero is not allowed.")
        return None

    return num


def main():
    """Run the Smart Calculator program."""
    print("=== Smart Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")

    choice = validate_menu_choice(
        input("Enter your choice (1-7): ")
    )

    if choice is None:
        return

    num1 = validate_number(
        input("Enter the first number: ")
    )

    if num1 is None:
        return

    num2 = validate_number(
        input("Enter the second number: "),
        is_second=True,
        operation=choice,
    )

    if num2 is None:
        return

    if choice == "1":
        result = num1 + num2
        label = "Sum"
    elif choice == "2":
        result = num1 - num2
        label = "Difference"
    elif choice == "3":
        result = num1 * num2
        label = "Product"
    elif choice == "4":
        result = num1 / num2
        label = "Quotient"
    elif choice == "5":
        result = num1 // num2
        label = "Floor Division Result"
    elif choice == "6":
        result = num1 % num2
        label = "Remainder"
    else:
        result = num1 ** num2
        label = "Power Result"

    if isinstance(result, float):
        print(f"{label}: {round(result, 2)}")
    else:
        print(f"{label}: {result}")


if __name__ == "__main__":
    main()

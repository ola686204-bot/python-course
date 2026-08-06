DECIMAL_PLACES = 2


def get_number(prompt):
    """Get a valid floating-point number from the user."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def validate_number(number):
    """Display whether the value is a valid number."""
    if isinstance(number, (int, float)):
        print(f"{number} is a valid number.")
    else:
        print(f"{number} is not a valid number.")


def calculate_results(first_number, second_number):
    """Perform all arithmetic operations."""
    return {
        "Addition": first_number + second_number,
        "Subtraction": first_number - second_number,
        "Multiplication": first_number * second_number,
        "Division": (
            first_number / second_number
            if second_number != 0
            else None
        ),
        "Exponentiation": first_number ** second_number,
        "Modulus": (
            first_number % second_number
            if second_number != 0
            else None
        ),
        "Floor Division": (
            first_number // second_number
            if second_number != 0
            else None
        ),
    }


def display_result(label, value):
    """Display one calculation result."""
    if value is None:
        print(f"{label}: Undefined (division by zero)")
        return

    print(f"{label}: {round(value, DECIMAL_PLACES)}")


def display_results(results):
    """Display all arithmetic results."""

    display_result(
        "The sum of two numbers is",
        results["Addition"],
    )

    display_result(
        "The subtraction of two numbers is",
        results["Subtraction"],
    )

    display_result(
        "The multiplication of two numbers is",
        results["Multiplication"],
    )

    display_result(
        "The division of two numbers is",
        results["Division"],
    )

    display_result(
        "The exponentiation of two numbers is",
        results["Exponentiation"],
    )

    display_result(
        "The modulus of two numbers is",
        results["Modulus"],
    )

    display_result(
        "The floor division of two numbers is",
        results["Floor Division"],
    )


def display_summary(results):
    """Display summary statistics."""

    values = [
        value
        for value in results.values()
        if value is not None
    ]

    print(f"\nCount of values in the summary is: {len(values)}")
    print(f"The maximum value in the summary is: {max(values)}")
    print(f"The minimum value in the summary is: {min(values)}")


def main():
    """Run the calculator."""

    first_number = get_number("Enter a number: ")

    if first_number is None:
        return

    second_number = get_number("Enter another number: ")

    if second_number is None:
        return

    validate_number(first_number)
    validate_number(second_number)

    results = calculate_results(
        first_number,
        second_number,
    )

    print()

    display_results(results)

    display_summary(results)


if __name__ == "__main__":
    main()



    
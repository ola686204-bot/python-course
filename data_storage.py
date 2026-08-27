"""Calculator program with operation history management."""


def add_to_history(history, operation, a, b, result):
    """Add a calculator operation to the history.

    Args:
        history: The list containing calculator history.
        operation: The arithmetic operator used.
        a: The first number.
        b: The second number.
        result: The calculation result.

    Returns:
        The updated history list.
    """
    entry = f"{a} {operation} {b} = {result}"
    history.append(entry)
    return history


def view_history(history):
    """Display all entries in the calculator history.

    Args:
        history: The list containing calculator history.
    """
    if not history:
        print("History is empty.")
        return

    print("\n=== Calculator History ===")

    for index, entry in enumerate(history, start=1):
        print(f"{index}. {entry}")


def search_history(history, keyword):
    """Search history entries for a keyword.

    Args:
        history: The list containing calculator history.
        keyword: The word or symbol to search for.

    Returns:
        A list containing all matching history entries.
    """
    keyword = keyword.lower()

    return [
        entry for entry in history
        if keyword in entry.lower()
    ]


def delete_entry(history, index):
    """Remove an entry from history using its index.

    Args:
        history: The list containing calculator history.
        index: The index of the entry to remove.

    Returns:
        The removed entry, or None if the index is invalid.
    """
    if index < 0 or index >= len(history):
        print("Error: History index is out of range.")
        return None

    return history.pop(index)


def summarize_history(history):
    """Calculate statistics from calculator history.

    Args:
        history: The list containing calculator history.

    Returns:
        A dictionary containing total, highest, lowest, and
        average results, or None if history is empty.
    """
    if not history:
        return None

    results = []

    for entry in history:
        result_text = entry.split("=")[-1].strip()
        results.append(float(result_text))

    return {
        "total_operations": len(results),
        "highest_result": max(results),
        "lowest_result": min(results),
        "average_result": sum(results) / len(results),
    }


def clear_history(history):
    """Remove all entries from the history.

    Args:
        history: The list containing calculator history.

    Returns:
        An empty history list.
    """
    history.clear()
    return history


def calculate(a, b, operation):
    """Perform an arithmetic calculation.

    Args:
        a: The first number.
        b: The second number.
        operation: The arithmetic operator.

    Returns:
        The calculation result, or None for an invalid operation.
    """
    if operation == "+":
        return a + b

    if operation == "-":
        return a - b

    if operation == "*":
        return a * b

    if operation == "/":
        if b == 0:
            print("Error: Cannot divide by zero.")
            return None
        return a / b

    if operation == "//":
        if b == 0:
            print("Error: Cannot divide by zero.")
            return None
        return a // b

    if operation == "%":
        if b == 0:
            print("Error: Cannot divide by zero.")
            return None
        return a % b

    if operation == "**":
        return a ** b

    print("Error: Invalid operation.")
    return None


def run_history_manager(history):
    """Run the calculator history management menu.

    Args:
        history: The list containing calculator history.
    """
    while True:
        print("\n=== Calculator History Manager ===")
        print("1. Calculate")
        print("2. View history")
        print("3. Search history")
        print("4. Delete entry")
        print("5. Summarize history")
        print("6. Clear history")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            try:
                first_number = float(
                    input("Enter the first number: ")
                )

                operation = input(
                    "Enter operation (+, -, *, /, //, %, **): "
                )

                second_number = float(
                    input("Enter the second number: ")
                )

                result = calculate(
                    first_number,
                    second_number,
                    operation,
                )

                if result is not None:
                    add_to_history(
                        history,
                        operation,
                        first_number,
                        second_number,
                        result,
                    )

                    print(f"Result: {result}")
                    print(f"Saved: {history[-1]}")

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "2":
            view_history(history)

        elif choice == "3":
            keyword = input("Enter keyword to search: ")

            matches = search_history(
                history,
                keyword,
            )

            if matches:
                print("\n=== Search Results ===")

                for index, entry in enumerate(
                    matches,
                    start=1,
                ):
                    print(f"{index}. {entry}")
            else:
                print("No matching entries found.")

        elif choice == "4":
            if not history:
                print("History is empty.")
                continue

            try:
                index = int(
                    input("Enter history entry number to delete: ")
                )

                removed = delete_entry(
                    history,
                    index - 1,
                )

                if removed is not None:
                    print(f"Removed: {removed}")

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "5":
            summary = summarize_history(history)

            if summary is None:
                print("History is empty.")
            else:
                print(
                    f"Total operations: "
                    f"{summary['total_operations']}"
                )
                print(
                    f"Highest result: "
                    f"{summary['highest_result']}"
                )
                print(
                    f"Lowest result: "
                    f"{summary['lowest_result']}"
                )
                print(
                    f"Average result: "
                    f"{summary['average_result']}"
                )

        elif choice == "6":
            clear_history(history)
            print("History has been cleared.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Error: Invalid menu choice.")


def main():
    """Initialize the history list and start the program."""
    history = []
    run_history_manager(history)


if __name__ == "__main__":
    main()

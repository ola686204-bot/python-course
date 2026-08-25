"""Compare recursive and iterative solutions."""


def factorial_recursive(n):
    """Return n factorial using recursion.

    Base case: 0! and 1! return 1.
    Recursive case: n is multiplied by factorial(n - 1).
    """
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Return n factorial using a loop.

    The loop multiplies each number from 2 through n.
    """
    if n == 0 or n == 1:
        return 1

    result = 1

    for number in range(2, n + 1):
        result *= number

    return result


def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion.

    Base case: 0 returns 0 and 1 returns 1.
    Recursive case: add the two previous Fibonacci numbers.
    """
    # Base case
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Recursive case
    return (
        fibonacci_recursive(n - 1)
        + fibonacci_recursive(n - 2)
    )


def fibonacci_iterative(n):
    """Return the nth Fibonacci number using a loop.

    The loop repeatedly updates the previous two Fibonacci values.
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


def sum_recursive(numbers):
    """Return the sum of a list using recursion.

    Base case: an empty list returns 0.
    Recursive case: add the first number to the remaining list.
    """
    # Base case
    if len(numbers) == 0:
        return 0

    # Recursive case
    return numbers[0] + sum_recursive(numbers[1:])


def sum_iterative(numbers):
    """Return the sum of a list using a loop.

    The loop adds each number to a running total.
    """
    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    return total


def run_comparisons():
    """Compare recursive and iterative results."""
    print("RECURSION VS ITERATION")
    print("-" * 65)
    print(
        f"{'Problem':<15}"
        f"{'Input':<15}"
        f"{'Recursive':<15}"
        f"{'Iterative':<15}"
    )
    print("-" * 65)

    factorial_inputs = [0, 1, 5]
    for number in factorial_inputs:
        recursive = factorial_recursive(number)
        iterative = factorial_iterative(number)
        assert recursive == iterative
        print(
            f"{'Factorial':<15}"
            f"{number:<15}"
            f"{recursive:<15}"
            f"{iterative:<15}"
        )

    fibonacci_inputs = [0, 1, 10]
    for number in fibonacci_inputs:
        recursive = fibonacci_recursive(number)
        iterative = fibonacci_iterative(number)
        assert recursive == iterative
        print(
            f"{'Fibonacci':<15}"
            f"{number:<15}"
            f"{recursive:<15}"
            f"{iterative:<15}"
        )

    sum_inputs = [[], [1], [1, 2, 3, 4, 5]]
    for numbers in sum_inputs:
        recursive = sum_recursive(numbers)
        iterative = sum_iterative(numbers)
        assert recursive == iterative
        print(
            f"{'List Sum':<15}"
            f"{str(numbers):<15}"
            f"{recursive:<15}"
            f"{iterative:<15}"
        )


if __name__ == "__main__":
    run_comparisons()

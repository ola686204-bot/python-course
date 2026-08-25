"""Provide a robust calculator for two numbers.

The program validates user input, performs arithmetic operations,
and displays a summary of the results.
"""

try:
    x_float = float(input("Enter a number: "))
    y_float = float(input("Enter another number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    x_float = None
    y_float = None

if isinstance(x_float, (int, float)):
    print(f"{x_float} is a valid number.")
else:
    print(f"{x_float} is not a valid number.")

if isinstance(y_float, (int, float)):
    print(f"{y_float} is a valid number.")
else:
    print(f"{y_float} is not a valid number.")

if x_float is not None and y_float is not None:
    result_add = x_float + y_float
    result_sub = x_float - y_float
    result_mul = x_float * y_float

    if y_float != 0:
        result_div = x_float / y_float
        result_mod = x_float % y_float
        result_floor_div = x_float // y_float
    else:
        result_div = None
        result_mod = None
        result_floor_div = None

    result_exp = x_float ** y_float

    print(f"The sum of two numbers is: {round(result_add, 2)}")
    print(f"The subtraction of two numbers is: {round(result_sub, 2)}")
    print(
        f"The multiplication of two numbers is: "
        f"{round(result_mul, 2)}"
    )

    if result_div is not None:
        print(f"The division of two numbers is: {round(result_div, 2)}")
        print(f"The modulus of two numbers is: {round(result_mod, 2)}")
        print(
            f"The floor division of two numbers is: "
            f"{round(result_floor_div, 2)}"
        )
    else:
        print("Division by zero is not allowed.")
        print("Modulus by zero is not allowed.")
        print("Floor division by zero is not allowed.")

    print(
        f"The exponentiation of two numbers is: "
        f"{round(result_exp, 2)}"
    )

    score = [
        result_add,
        result_sub,
        result_mul,
        result_div,
        result_exp,
        result_mod,
        result_floor_div,
    ]

    valid_scores = [value for value in score if value is not None]

    count = len(valid_scores)

    print(f"Count of values in the summary is: {count}")
    print(f"The maximum value in the summary is: {max(valid_scores)}")
    print(f"The minimum value in the summary is: {min(valid_scores)}")

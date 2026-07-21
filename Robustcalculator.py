'''This is a robust calculator
 that performs basic arithmetic operations
   on two numbers and validates all inputs,
   inspects their types,
     perform type casting where necessary,
       and uses built-in functions
         to produce an enriched summary of results. '''

try:
    x_float = float(input("Enter a number:"))
    y_float = float(input("Enter another number:"))
except ValueError:
    print("Invalid input. Please enter a valid number.")

if isinstance(x_float,(int,float)):
    print(f'{x_float} is a valid number.')
else:
    print(f'{x_float} is not a valid number.')

if isinstance(y_float,(int,float)):
    print(f'{y_float} is a valid number.')
else:
    print(f'{y_float} is not a valid number.')

result_add = x_float + y_float
result_sub = x_float - y_float
result_mul = x_float * y_float
result_div = x_float / y_float
result_exp = x_float ** y_float
result_mod = x_float % y_float
result_floor_div = x_float // y_float

print(f'The sum of two numbers is: {round(result_add,2)}')
print(f'The subtraction of two numbers is: {round(result_sub,2)}')
print(f'The multiplication of two numbers is: {round(result_mul,2)}')
print(f'The division of two numbers is: {round(result_div,2)}')
print(f'The exponentiation of two numbers is: {round(result_exp,2)}')
print(f'The modulus of two numbers is: {round(result_mod,2)}')
print(f'The floor division of two numbers is: {round(result_floor_div,2)}')

Score= [result_add, result_sub, result_mul, result_div, result_exp, result_mod, result_floor_div]
count = len(Score)
print(f'count of values in the summary is: {count}')
print(f'The maximum value in the summary is: {max(Score)}')
print(f'The minimum value in the summary is: {min(Score)}')
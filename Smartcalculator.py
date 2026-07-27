'''This is a smart  calculator
 that uses conditional execution  and 
     input validation to allow user
       to handle all interactions safely
         and informatively.'''

def validate_menu_choice(choice):
    '''Validate that the menu choice is one of the allowed options.'''
    valid_choices = ["1","2","3","4","5","6","7"]
    if choice not in valid_choices:
        print("Error: Invalid choice. please select a number between 1 and 7.")
        return None
    return choice

def validate_number(value, is_second= "false", operation=None):
    '''Validate that the input is a non-empty, numeric value.For division and floor division, ensure the seconnd number is not zero.'''
    if value.strip() == "":
        print("Error: Input cannot be empty. Please enter a valid number.")
        return None
    
    try: 
        num= float(value)
    except ValueError: 
        print("Error: Please enter a valid numeric value.")
        return None
    if is_second and (operation in ["4","5"]) and num == 0:
        print("Error: Division or floor division by zero is not allowed.")
        return None
    
    return num

# Main program Logic

def main():
    print("=== Smart Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("4. Multiplication")
    print("5. Division")
    print("6. Modulus")
    print("7. Exponentiation")

     # Get and validate menu choice

    choice = validate_menu_choice(input("Enter your choice (1-7):"))
    if choice is None:
        return # Exit if invalid choice
    
    # Get and validate first number 

    num1 = validate_number(input("Enter the first number:"))
    if num1 is None:
        return
    
    # Get and validate second number 

    num2 = validate_number(input("Enter the  second number:"), is_second=True, operation=choice)
    if num2 is None:
        return
    
    # Perform operation using if/elif/else

    if choice == "1":
        result = num1 + num2
        label = "sum"
    elif choice == "2":
        result = num1 - num2
        label = "Difference"
    elif choice == "3":
        result = num1 * num2
        label = "product"
    elif choice == "4":
        result = num1  / num2
        label = "Qoutient"
    elif choice == "5":
        result = num1 // num2
        label = "Floor Division Result"
    elif choice =="6":
        result = num1 % num2
        label= "Remainder"
    else: choice == "7"
    result = num1 ** num2
    label = "power Result"

# Display result (round if float) 

if isinstance("result", float):
    print(f"{"label"}: {round("result", 2)}")
else:
    print(f"{"label"}:{"result"}")

    # Entry point
    if __name__ == "__main__":
        main()

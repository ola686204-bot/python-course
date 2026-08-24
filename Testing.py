"""This is a simple calculator
   that performs arithmetic operation."""
try:
    num_1 = float(input("Enter The first Number:"))
    num_2 = float(input("Enter The Second Number:"))
except ValueError:
    print("Invalid Input, Please enter a valid number")

if isinstance (num_1, (float,int)):
    print(f"(num_1) is a valid number." )
else:
    print(f"(num_1) is not a valid number.")

if isinstance (num_2, (float,int)):
    print(f"(num_2) is a valid number.")
else:
    print(f"(num_2) is not a valid number.")

Result_add = num_1 + num_2
Result_sub = num_1 - num_2
Result_mul = num_1 * num_2
Result_div = num_1 / num_2
Result_Floor_div = num_1 // num_2
Result_Expo = num_1 ** num_2
Result_Mod = num_1 % num_2

print(f"The sum of two numbers is: {round(Result_add,2)}")
print(f"The subtraction of two numbers is: {round(Result_sub,2)}")  
print(f"The multiplication of two numbers is: {round(Result_mul,2)}")
print(f"The Division of two numbers is: {round(Result_div,2)}")
print(f"The Floor_Division of two numbers is: {round(Result_Floor_div,2)}")
print(f"The Exponentiation of two numbers is: {round(Result_Expo,2)}")
print(f"The Modudlus of two numbers is: {round(Result_Mod,2)}")
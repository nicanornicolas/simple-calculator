# simple calculator program.

print("---Basic Calculator---")
print("Enter two numbers and an operation (+,-,*,/) \n")

# First step: Getting the user's input

# get the first number and convert it from a string to a float
num1 = float(input("Enter the first number: "))

# get the mathematical operation
operator = input("Enter the operation (+,-,*,/):")

# get the second number and convert it from a string to a float
num2 = float(input("Enter the second number: "))

# Second step: perform the calculation using if/else/elif

if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    result = num1 / num2

else:
    # if the operator is not one of the above, set the result to an error message
    result = "Error: Invalid operation"

# Third step: display the result

# check if the result is a number before printing the formatted equation.
# using the 'isinstance()' function checks if a variable is of a certain type.
if isinstance(result, (int, float)):
    # The f-string (f"...") makes it easy to format the output string
    print(f"\nResult: {num1} {operator} {num2} = {result}")
else:
    # If 'result' contains the error message, just print that
    print(f"\n{result}")
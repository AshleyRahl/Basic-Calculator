# Get user input for the first number
num1 = float(input("Enter the first number: "))
# Get user input for the second number
num2 = float(input("Enter the second number: "))

# Get user input for the operator
operator = input("Enter the operator (+, -, *, /): ")

result = 0

# Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result =num1 - num2
elif operator == "*":
    result =num1 * num2
elif operator == "/":
    result =num1 / num2
else:
    print(f"Invalid operator: '{operator}'")
    print("Use one of +, -, *, /")

num_decimal = int(input("Round my result to given decimals: "))
if num_decimal == 0:
    print(round(result))
else:
    print(round(result, num_decimal))

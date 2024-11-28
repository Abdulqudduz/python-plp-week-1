# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operation == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif operation == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif operation == "/":
    if num2 != 0:  # Check for division by zero
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use +, -, *, or /.")

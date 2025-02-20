# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        input("Press Enter to exit...")  # Added this line to keep window open
        exit()
else:
    print("Invalid operation!")
    input("Press Enter to exit...")  # Added this line to keep window open
    exit()

# Display result
print(f"{num1} {operation} {num2} = {result}")
input("Press Enter to exit...")  # Added this line to keep window open
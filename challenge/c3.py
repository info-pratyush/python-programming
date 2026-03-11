# SIMPLE CALCULATOR

#This simple calculator can perform basic arithmetic operations like addition, subtration, multiplication and division.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /): ")

while True:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Undefined (division by zero)"
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")
    
    again = input("Do You Want To Calculate Again? (yes/no)")
    if again == "no":
        break
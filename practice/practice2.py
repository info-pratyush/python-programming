# Ask the user to enter two numbers. Print their sum, difference, product, and quotient.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Undefined (division by zero)"
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)


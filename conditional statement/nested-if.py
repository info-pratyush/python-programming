# You can have if statement inside if statement. This is called Nested if statement.

x = int(input("Enter a number : "))

if x > 40:
  print("The number is above 10")
  if x > 20:
    print("The number is also above 20")
else:
  print("not above 20")    
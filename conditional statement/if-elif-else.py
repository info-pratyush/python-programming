# the elif keyword allow you to check multiple expression for true and executes a block of code as soon as one of the expression executes to TRUE

age = int(input("Enter Your Age : "))

if age <18:
  print("Too Young To Get License")

elif age >= 18 and age <= 60:
  print("Eligible To Get License")

else :
  print("To Old To Get License")
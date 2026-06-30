#a.) Standard Deviation 

n = int(input("Enter the number for the operation: ")) 
numbers = [] 

for i in range(n): 
  value = int(input("Enter the numbers: ")) 

numbers.append(value) 
print("The numbers are: ", numbers) 

# Mean 
total = 0 
for i in numbers: 
  total = total + i 
average = total / n 
print("The average of the numbers is: ", average) 

# Variance 
sum_sq = 0 
for i in numbers: 
  diff = i - average 
sum_sq = sum_sq + diff * diff 
variance = sum_sq / n 
std_dev = variance ** 0.5 

print("Variance: ", variance) 
print("Standard Deviation: ", std_dev)


#b.) Roots of Quadratic Equation 

print("This program checks quadratic equations") 
a = int(input("Enter the coefficient of X^2: ")) 
b = int(input("Enter the coefficient of x : ")) 
c = int(input("Enter the constant term : ")) 
d = b*b - 4*a*c 
print("Discriminant  :  ", d) 

if d > 0: 
  x1 = (-b + d**0.5) / (2*a) 
  x2 = (-b - d**0.5) / (2*a) 
  print("first real root ", x1) 
  print("second real root ", x2) 

elif d == 0: 
 x1 = -b / (2*a) 
 x2 = -b / (2*a) 
 print("roots are equal and real :  ") 
 print(x1, x2) 
else: 
  print("Roots are imaginary")
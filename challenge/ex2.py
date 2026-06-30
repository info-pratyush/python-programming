#1.Arithmetic Operators  

a=10  
b=4 
print("Addition :  ", a + b) 
print("Subtraction : ",a - b) 
print("Multiplication :  ",a * b) 
print("Division :  ",a / b) 
print("Modulo :  ",a % b) 
print("Floor Division :  ",a // b) 
print("Exponent :  ",a ** b) 

#2. Relational Operators  

c=20 
d=8 

print("Greater than :  ",c > d) 
print("Less than : ",c < d) 
print("Greater than Equal to :  ",c>=d) 
print("Less than Equal to :  ",c <= d) 
print("Equal to :  ",a == b) 
print("Not Equal to :  ",a != b)

#3. Logical Operators    

e = 25  
f = 12 

print("e > 5 and f > 15 : ", e > 5 and f>15) 
print("e > 15 or e > 15: ", e > 15 or f >15)  
print("not(e > 5): ", not(e > 5))   

#4. Assignment Operators   

g = 10 
print("Initial value: ",g) 
g += 5 
print("After +=  : ", g) 
g -= 3 
print("After -=  : ", g) 
g *= 2 
print("After *= : ", g)  
g /= 4 
print("After /=  :", g)  

#5. Bitwise Operators  

i = 5   # binary 0101 
j = 3   # binary 0011 

print("i & j : ", i & j) 
print("i | j : ", i | j) 
print("i ^ j : ", i ^ j) 
print("~i : ", ~a) 
print("i << 1 : ", i << 1) 
print("j >> 1 : ", j >> 1) 

#6. Membership Operators  

list1 = [10, 20, 30, 40] 

print(20 in list1) 
print(50 not in list1)   

#7. Identity Operators  

h = 10 
k = 10 
l = 20 

print("h is k : ", h is k)  
print("h is l : ", h is k) 
print("h is not l:", h is not l)  
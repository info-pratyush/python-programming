print("Library Fine Calculator") 

days = int(input("Enter The number Of Days Of Late Book Submission : ")) 
if days <= 5: 
   fine = days * 0.50 
   print("Pay Fine :", fine) 
elif days <= 10: 
   fine = days * 1.0 
   print("Pay Fine :", fine) 
elif days <= 30: 
   fine = days * 5.0  
   print("Pay Fine :", fine) 
else: 
   print("Your Membership cancelled")
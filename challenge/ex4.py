print("Notes Calculator") 
total_amount = float(input("Enter the amount (In Hundred) : ")) 

hundreds = total_amount // 100 
remaining_amount = total_amount % 100 
fifties = remaining_amount // 50 
remaining_amount = remaining_amount % 50 
tens = remaining_amount // 10 
remaining_amount = total_amount % 10 

print("Total Amount : ", total_amount) 
print("Total Hundred Notes : ", hundreds) 
print("Total Fifties Notes : ", fifties) 
print("Total Tens Notes : ", tens) 
print("Remaining Amount Left : ", remaining_amount)
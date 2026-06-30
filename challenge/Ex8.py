student_profile = { 
"name": "Pratyush", 
"roll": 11252627, 
"branch" : "CSE" 
} 
print("Student Profile: ", student_profile) 
print("Name: ", student_profile["name"]) 
student_profile["year"] = 1 
print("After adding year: ", student_profile) 
student_profile["branch"] = " CSE AI/ML" 
print("After updating branch: ", student_profile) 
del student_profile["roll"] 
print("After deleting roll: ", student_profile)

print("\n")

# Part 2


telephone_directory = {}

telephone_directory["Pratyush"] = "8226962113"
telephone_directory["Robert"] = "6290000866"
telephone_directory["Sam"] = "4574548820"

print("Telephone Directory: ", telephone_directory)
print("\n")

find = input("Enter Name To Search: ")

if find in telephone_directory:
    print("Phone Number is: ", telephone_directory[find])
else:
   print("Contact not found")

update = input("Enter the name you want to update number: ") 

if update in telephone_directory:
   new_number = input("Enter new number: ")

   telephone_directory[update] = new_number
   print("updated directory: ", telephone_directory)

else: 
   print("Contact not found")
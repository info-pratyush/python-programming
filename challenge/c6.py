# experiment number 9 


file = open("student_record.txt", "w")

name = input("Enter Student Name: ")
roll = input("Enter Student Roll Number: ") 
session = input("Enter Student Session: ")
branch = input("Enter Student Branch: ")



file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Session: " + session + "\n") 
file.write("Branch: " + branch + "\n")
file.close()

file = open("student_record.txt", "r")
print("Student Record: \n") 
print(file.read())
file.close()


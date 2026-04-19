my_dict = {
    "name" : "Pratyush",
    "age" : 18, 
    "city" : "Ambala"
}

for key in my_dict:
    print(key, my_dict[key]) 

# Better way to loop through a dictionary

for key, value in my_dict.items():
    print(key, value)
        
my_dict = {
    "name" : "Pratyush",
    "age" : 18,
    "city" : "Ambala"
}

my_dict.pop("age") 
print(my_dict) 

my_dict.popitem()
print(my_dict)

my_dict.clear()
print(my_dict)

dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
del dict1["model"]
print(dict1)

del dict1
# print(dict1) # This will raise an error because dict1 has been deleted.
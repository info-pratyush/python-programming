my_dict = {
    "name" : "Pratyush",
    "age" : 18,
    "city" : "Ambala"
}
# Accessing Items
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.get("city"))
print(my_dict.get("country", "Not Found")) # This will return "Not Found" because "country" key does not exist in the dictionary.
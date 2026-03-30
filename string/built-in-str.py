name ="Roger was a good man"

print("string in lower-case")
x = name.lower()
print(x)

print("\nString in upper-case")
x = name.upper()
print(x)

print("\nCapitalized version of string")
x = name.title()
print(x)

print("\nFirst character to upper case")
x = name.capitalize()
print(x)

print("\nTo append new letter to a string")
x = "-".join(name)
print(x)

print("\nFind the position of a sub-string")
x = name.find("good")
print(x)

print("\nTrim the whitespace from a string")
x = name.strip()
print(x)

print("\nFormate the specified value in a string")
txt = "Only for {price:.2f} rupees !"
print(txt.format(price = 99))






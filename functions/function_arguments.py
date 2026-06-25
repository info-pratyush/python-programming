# Arguments are the values that you can pass to a function when you call it. They are used to provide input to the function, which can then use that input to perform its task. In Python, you can define a function with parameters, which are placeholders for the arguments that will be passed when the function is called.

# Example of a function with parameters and arguments:

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")
greet("Pratyush")  # "Pratyush" is an argument passed to the function

# Postional arguments 

def show(a, b):
    print(a, b)

show(5, 10)

# Keyword arguments
show(a=5, b=10)

# Default arguments

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Uses default argument "Guest"
greet("Pratyush")  # Overrides default 

# Variable-length arguments 
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

# Keyword-only arguments 
def display_info(name, age, *, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

display_info("Pratyush", 18, city="Ambala")



# Decorator is a function that takes another function as input and returns a new function that adds some functionality to the original function.

def decorator(func):
    def inner():
        return func() + 1
    return inner

@decorator
def original_function():
    return 1

print(original_function())  # Output: 2

# multiple decorators
def decorator1(fun):
    def inside():
        return fun() + 1
    return inside

@decorator1
def originalfunction():
    return 1

@decorator1
def second_function():
    return 2
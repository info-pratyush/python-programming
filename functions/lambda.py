# A Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

x = lambda a : a + 5

print(x(10)) # Output: 15

y = lambda a, b : a * b

print(y(5, 6)) # Output: 30


#############################

def func(n):
    return lambda a : a * n

double = func(2)
triple = func(3)

print(double(5)) # Output: 10

print(triple(5)) # Output: 15

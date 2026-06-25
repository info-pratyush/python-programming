# A variable is only accessible within the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300
  print(x)

myfunc()

# The variable x is not available outside the function, and this will raise an error:

# print(x)

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope. Global variables are available from within any scope, global and local.

y = 300

def myfunc():
  print(y)
myfunc()

print(y)
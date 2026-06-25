# global keyword makes a variable global

def myfunc():
  global z
  z = 300
myfunc()

print(z)

# To change the value of a global variable inside a function, refer to variable by using the gloable keyword.

x = 300

def myfunc():
  global x
  x = 200 
myfunc()

print(x)
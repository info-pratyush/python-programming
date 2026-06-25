# Passing Arguments by References

""" A variable in python is a reference to the object memory. So, both formal and actual arguments refers to the same object in memory."""

# the id() function returns the memory address of the object.

def myfunction(newlist):
    print("List accessed in function: ", "id: ", id (newlist))
    return

mylist = [10, 20, 30, 40, 50]
print("List before passing to the function: ", "id: ", id(mylist))

myfunction(mylist)


""" If we modify the list object inside the function and display its contents after function is completed, changes are reflected outside the function as well."""
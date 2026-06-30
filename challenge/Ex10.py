#Inheritance 
print("\n-----INHERITANCE----\n")
class college:
    def display(self):
        print("This is a college class.")

class department(college):
    def dept(self):
        print("This is a department class.")
    

show = department()
show.display()  
show.dept()

#function overloading 

print("\n----FUNCTION OVERLOADING----\n")
class calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = calculator()
print(calc.add(5, 10))        
print(calc.add(5, 10, 15))   

#opertator overloading  

print("\n----OPERATOR OVERLOADING----\n")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2

print("Result of addition: ({}, {})".format(result.x, result.y))


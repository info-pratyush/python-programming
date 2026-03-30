#Identity operator used to compare the objects, not if they are equal but if they are the same object in memory.

print("Identity Operators")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b ->", a is b)  # True, because a and b refer to the same object

print("a is c ->", a is c)  # False, because a and c are different objects in memory

print("a == c ->", a == c)  # True, because a and c have the same content

print("a is not c ->", a is not c)  # True, because a and c are different objects 
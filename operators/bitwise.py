#Bitwise operators are used to compare binary number bit by bit.

print("Bitwise Operators")

a = 5  # In binary: 0101
b = 3  # In binary: 0011

print("a =", a, "- ", bin(a))
print("b =", b, "- ", bin(b))

print("a & b ->", a & b, "- ", bin(a & b))  # Bitwise AND

print("a | b ->", a | b, "- ", bin(a | b))  # Bitwise OR

print("a ^ b ->", a ^ b, "- ", bin(a ^ b))  # Bitwise XOR

print("~a ->", ~a, "- ", bin(~a))  # Bit wise NOT

print("a << 1 ->", a << 1, "- ", bin(a << 1))  # Left shift

print("a >> 1 ->", a >> 1, "- ", bin(a >> 1))  # Right shift



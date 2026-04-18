# Check if a string is a palindrome or not.
# Same forward and backward.

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
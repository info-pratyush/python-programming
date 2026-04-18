# slicing allows you to get a portion of a list. The syntax is list[start:stop:step].

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:5])  # Output: [2, 3, 4]
print(my_list[:5])   # Output: [0, 1, 2, 3, 4]
print(my_list[5:])   # Output: [5, 6, 7, 8, 9]
print(my_list[::2])  # Output: [0, 2, 4, 6, 8]
print(my_list[1::2]) # Output: [1, 3, 5, 7, 9]
print(my_list[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 

# You can also use negative indices to slice from the end of the list.
print(my_list[-5:-2])  # Output: [5, 6, 7]
print(my_list[-2:])    # Output: [8, 9] 


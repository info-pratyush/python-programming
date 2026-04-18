# Tuples are immutable, but we can covert a tuple to a list, remove the item from the list, and convert it back to a tuple.

my_tuple = ("apple", "banana", "cherry")
# Convert tuple to list
my_list = list(my_tuple)
# Remove item from list
my_list.remove("banana")

# Convert list back to tuple
my_tuple = tuple(my_list)
print(my_tuple)

# del keyword can be used to delete the entire tuple, but we cannot delete a specific item from the tuple using del keyword.

t = (1, 2, 3, 4, 5)
del t
print(t) # This will raise an error because the tuple has been deleted.


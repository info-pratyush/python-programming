# A Tuple is ordered and immutable collection of items. It is defined by enclosing the items in parentheses (). It allows duplicate members. Tuple can contain items of different data types.

# Creating a Tuple

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)


# Tuple length
print(len(my_tuple))

tuple1 = tuple(("apple", "banana", "cherry")) #tuple constructor
print(tuple1)

# Creating tuple with one item, we have to add a comma after the item, otherwise it will be considered as a string.

tuple2 = ("Hello",)
print(tuple2)
# Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.

# Create a Set:

my_set = {"apple", "banana", "cherry"}
print(my_set)

# True and 1, False and 0 are considered the same value in a set, and are treated as duplicates:

# No duplicates in sets are allowed.

set1 = {0, 1, 2, 3, True, False}
print(set1)

print(len(set1)) # Output: 4, because True and 1 are considered the same, and False and 0 are considered the same


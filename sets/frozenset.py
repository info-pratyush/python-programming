# A frozenset is an immutable version of a set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

# A fronset can be used as a key in a dictionary, while a set cannot be used as a key in a dictionary.

# Create a frozenset:

my_frozenset = frozenset(["apple", "banana", "cherry"])
print(my_frozenset)

# frozenset methods

set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

print(set1 | set2) # Union of sets set1 and set2
print(set1 & set2) # Intersection of sets set1 and set2
print(set1 - set2) # Difference of sets set1 and set2 (elements in set1 but not in set2)
print(set1 ^ set2) # Symmetric difference of sets set1 and set2 

#isdisjoint() method returns True if two sets have a null intersection.

set3 = frozenset([7, 8, 9])
print(set1.isdisjoint(set3)) # Output: True, because set1 and set3 have no common elements

#issubset() method returns True if all items in the set are present in the specified set.

print(set1.issubset(set2)) # Output: False, because not all items in set1 are present in set2

#issuperset() method returns True if all items in the specified set are present in the original set.

print(set1.issuperset(set2)) # Output: False, because not all items in set2 are present in set1



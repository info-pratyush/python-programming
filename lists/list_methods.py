my_list = [1, 2, 3, 4, 5]

print(my_list) # printing original list

print(len(my_list)) #  length of the list
print(max(my_list)) # maximum value in the list
print(min(my_list)) # minimum value in the list

my_list.append(6) # adding an element to the end of the list
print(my_list) # printing updated list

my_list.insert(1, 10) # inserting an element at index 1
print(my_list) # printing updated list

my_list.remove(3) # removing the element with value 3
print(my_list) # printing updated list

my_list.pop() # removing the last element
print(my_list) # printing updated list

my_list.pop(2) # removing the element at index 2
print(my_list) # printing updated list

my_list.clear() # clearing the list
print(my_list) # printing the empty list

list1 = [1, 2, 3]
print(list1) # printing list1

list1.reverse() # reversing the list
print(list1) # printing reversed list1

list1.sort() # sorting the list
print(list1) # printing sorted list1

list1.extend([4, 5, 6]) # extending list1 with another list
print(list1) # printing extended list1

list2 = list1.copy() # copying list1 to list2
print(list2) # printing copied list2

list2.count(2) # counting the occurrences of 2 in list2
print(list2.count(2)) # printing the count of 2 in list2
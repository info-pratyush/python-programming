a = [10, 35, 40, 80, 25, 90, 45]
print("List: ", a)

largest = a[0]

for i in a:
  if i > largest:
    largest = i

print("Largest element in the list is: ", largest)    
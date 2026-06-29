# The filter() function is used to filter the given iterable. With the help of a function that tests each element in the iterable to be true or not.

num = [1, 2, 3, 4, 5]

odd_num = list(filter(lambda x : x % 2 != 0, num))

print(odd_num)


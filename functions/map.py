 # the map() function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator). 

num = [1, 2, 3, 4, 5]

double = list(map(lambda x : x * 2, num))

print(double) 

#output : [2, 4, 6, 8, 10]
 
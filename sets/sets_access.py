# You can not access a set by index, but you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

this_set = {"Google", "Microsoft", "Apple"}

for x in this_set:
  print(x)

for x in this_set:
  if x == "Microsoft":
    print("Microsoft is present in the set.")
s = { 1, 2, 3, 4}

s.remove(4) # error if 4 is not present

s.discard(3) # does not raise an error if 3 is not present

s.pop() # removes a random item from the set, and returns it

print(s)
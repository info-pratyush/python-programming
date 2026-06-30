# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

import sys

print(sys.getrecursionlimit())

""" One can increase the deeper recursion, but this may cause crashes.

import sys

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

"""
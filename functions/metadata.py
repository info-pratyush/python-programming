def myfun():
   return "hello pratyush!"

print(myfun.__name__)

#output: myfun

# But when function is decorated metadata is lost. To preserve the metadata of the original function, we can use functools.wraps decorator.

import functools
 
def changecase(func):
   @functools.wraps(func)

   def inner():
        return func ().upper()
   return inner  

@changecase
def myfun():
    return "hello pratyush!"

print(myfun.__name__)
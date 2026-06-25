# nonlocal keyword is used to work with variables inside nested functions.

def myfunc1():
  x = "Pratyush"
  def myfunc2():
    nonlocal x
    x = "kumar"
  myfunc2()
  return x

print(myfunc1())
#import firstModule

#You can create an alias when you import a module, by using the as keyword

import firstModule as fm

fm.greetings("Pratyush")

a = fm.person1["age"]
print(a)

import platform

x = dir(platform)
print(x)
import demopkg2
print('demopkg2:', demopkg2.__file__)

print('demopkg2.overloaded:', b1.chapter19.demopkg2.overloaded.__file__)
print()
b1.chapter19.demopkg2.overloaded.func()

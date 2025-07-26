import weakref

class ExpensiveObject:
    def _del_(self) :
        print('(Deleting {})'.format(self))


obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():’, r ())
print(’deleting obj’)
del obj
printCr():’, r())
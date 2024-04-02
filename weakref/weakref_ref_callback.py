import weakref

class ExpensiveObject:

    def __del__(self):
        print(f'Deleting {self}')

def callback(reference):
    """Вызывается при удалении цулевого объекта"""
    print(f'callback({reference})')

obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj: ', obj)
print('ref: ', r)
print('r()', r())

print('deleting obj')
del obj
print('r(): ', r())

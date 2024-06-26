import weakref

class ExspensiveObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'Deleting {self}')


obj = ExspensiveObject('My Object')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('via obj: ', obj.name)
print('via.ref: ', r().name)
print('via proxy: ', p.name)
del obj
print('via proxy: ', p.name)

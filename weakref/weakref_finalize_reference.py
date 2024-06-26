import gc
import weakref

class ExspensiveObject:
    def __del__(self):
        print(f'Deleting {self}')

def on_finalize(*args):
    print(f'on_finalize({args})')

obj = ExspensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj, on_finalize, obj)
f.atexit = False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')

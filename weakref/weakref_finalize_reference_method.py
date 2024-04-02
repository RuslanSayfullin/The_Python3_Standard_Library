import gc
import weakref

class ExspensiveObject:
    def __del__(self):
        print(f'Deleting {self}')

    def do_finalize(self):
        print('do finalize')


obj = ExspensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj, obj.do_finalize)
f.atexit = False


for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')

import weakref

class ExspensiveObject:

    def __del__(self):
        print(f'deleting{self}')

def on_finalize(*args):
        print(f'on_finalize({args})')


obj = ExspensiveObject()

weakref.finalize(obj, on_finalize, 'extra argument')

del obj

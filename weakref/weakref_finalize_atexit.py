import weakref
import sys

class ExspensiveObject:

    def __del__(self):
        print(f'Deleting {self}')

def on_finalize(*args):
        print(f'on_finalize({args})')


obj = ExspensiveObject()

f = weakref.finalize(obj, on_finalize, 'extra argument')

f.atexit = bool(int(sys.argv[1]))

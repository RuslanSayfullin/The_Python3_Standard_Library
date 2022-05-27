import inspect
import l33_example


for name, data in inspect.getmembers(l33_example, inspect.isclass):
    print('{} : {!r}'.format(name, data))
    
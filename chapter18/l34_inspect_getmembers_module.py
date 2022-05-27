import inspect

import l33_example

for name, data in inspect.getmembers(l33_example):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))
    
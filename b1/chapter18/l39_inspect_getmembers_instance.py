import inspect
from pprint import pprint

import l33_example
a = l33_example.A(name='inspect_getmembers')
pprint(inspect.getmembers(a, inspect.ismethod))

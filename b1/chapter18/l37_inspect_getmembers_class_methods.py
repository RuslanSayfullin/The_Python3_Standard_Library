import inspect
from pprint import pprint

import l33_example
pprint(inspect.getmembers(l33_example.A, inspect.isfunction))

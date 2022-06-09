from pprint import pprint
from l76_pprint_data import data


for width in [80, 5]:
    print('WIDTH =', width)
    pprint(data, width=width)
    print()
    
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print(m.maps)
print('Before: {}'.format(m['c']))

a['c'] = 'E'
print(m.maps)
print('After : {}'.format(m['c']))
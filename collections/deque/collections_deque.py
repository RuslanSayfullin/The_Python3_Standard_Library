import collections

d = collections.deque('abcdefg')
print('deque: ', d)
print('Lenght: ', len(d))
print('Left end: ', d[0])
print('Right end: ', d[-1])

d.remove('c')
print('remove(c): ', d)

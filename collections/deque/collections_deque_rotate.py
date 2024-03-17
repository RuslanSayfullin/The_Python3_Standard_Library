import collections

d = collections.deque(range(10))
print('Normal: ', d)

d2 = collections.deque(range(10))
d2.rotate(2)
print('Right rotation: ', d2)
d3 = collections.deque(range(10))
d3.rotate(-2)
print('Left rotation: ', d3)

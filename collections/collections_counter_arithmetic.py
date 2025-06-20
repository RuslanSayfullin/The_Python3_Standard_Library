import collections
cl = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1:', cl)
print('C2:', c2)
print('\nCombined counts:')
print(cl + c2)
print('XnSubtraction:')
print(cl - c2)
print('\nIntersection (taking positive minimums):')
print(cl & c2)
print('XnUnion (taking maximums):')
print(cl | c2)
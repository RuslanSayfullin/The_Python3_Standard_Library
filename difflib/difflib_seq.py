import difflib

sl = [1, 2, 3, 5, 6, 4]
s2 = [2, 3, 5, 4, 6, 1]

print('Initial data:')
print('sl =', sl)
print('s2 =', s2)
print('sl == s2:', sl == s2)
print()

matcher = difflib.SequenceMatcher(None, sl, s2)
for tag, il, i2, jl, j2 in reversed(matcher.get_opcodes()):
    
    if tag == 'delete':
        print('Remove {} frompositions [{}:{}]'.format(sl[il:i2], il, i2))
        print(' before =', sl)
        del sl[il:i2]
    elif tag == 'equal':
        print('sl[{}:{}] and s2[{}:{}] are the same'.format(il, i2, jl, j2))
    elif tag == 'insert':
        print('Insert {} from s2[{}:{}] into sl at {}'.format(s2[jl:j2], jl, j2, il))
        print(' before =', sl)
        sl[il:i2] = s2[jl:j2]
    elif tag == 'replace':
        print(('Replace {} from sl[{}:{}] with {} from s2[{}:{}]').format(sl[il:i2], il, i2, s2[jl:j2], jl, j2))
        print(' before =', sl)
        sl[il:i2] = s2[jl:j2]
    
    print(' after =', sl, '\n')

print('sl == s2:', sl == s2)

# Этот пример основан на исходном коде difflib.py.

from difflib import SequenceMatcher

def show_results(match):
    print(' а = {}'.format(match.a))
    print(' b = {}'.format(match.b))
    print(' size = {}'.format(match.size))
    i, j, k = match
    print(' A[a:a+size] = {!r}'.format(A[i:i + k]))
    print(' B[b:b+size] = {!r}'.format(B[j:j + k]))

A = " abcd"
B = "abcd abcd"
print('A = {!r}'.format(A))
print('B = {!r}'.format(B))
print('\nWithout junk detection:')
sl = SequenceMatcher(None, A, B)
matchl = sl.find_longest_match(0, len(A), 0, len(B))
show_results(matchl)
print('\nTreat spaces as junk:')
s2 = SequenceMatcher(lambda x: x == " ", A, B)
match2 = s2.find_longest_match(0, len(A), 0, len(B))
show_results(match2)
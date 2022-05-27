import inspect
import l33_example


class C(object):
    pass


class C_First(C, l33_example.B):
    pass


class B_First(l33_example.B, C):
    pass


print('B_First:')
for c in inspect.getmro(B_First):
    print(' {}'.format(c.__name__))
print()
print('C_First:')
for c in inspect.getmro(C_First):
    print(' {}'.format(c.__name__))

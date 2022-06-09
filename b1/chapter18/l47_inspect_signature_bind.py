import inspect
import l33_example

sig = inspect.signature(l33_example.module_level_function)

bound = sig.bind(
    'this is arg1',
    'this is arg2',
    'this is an extra positional argument',
    extra_named_arg='value',
)
print('Arguments:')
for name, value in bound.arguments.items():
    print('{} = {!r}'.format(name, value))

print('\nCalling:')
print(l33_example.module_level_function(*bound.args, **bound.kwargs))

import string

"""
Метод safe_substitute() позволяет избежать возникновения исклю­чений в тех случаях,
когда не все значения, в которых нуждаются шаблоны, пред­ставлены аргументами.
"""

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute(): ', t.substitute(values))
except KeyError as err:
    print('ERROR: ', str(err))

print('safe_substitute(): ', t.safe_substitute(values))
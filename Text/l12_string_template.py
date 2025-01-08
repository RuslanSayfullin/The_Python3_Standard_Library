import string

values = {'var': 'foo'}

"""Пример, позволяющий сравнить три подхода к форматирова­
нию одной и той же строки: 
 - с помощью простого шаблона
 - оператора %
 - нового синтаксиса форматирующей строки с использованием метода str.format().
"""

t = string.Template("""
Variable    : $var
Escape      : $$
Variable in text:   ${var}iable
""")

print('TEMPLATE: ', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

f = """
Variable    : {var}
Escape      : {{}}
Variable in text:   {var}iable
"""

print('FORMAT: ', f.format(**values))